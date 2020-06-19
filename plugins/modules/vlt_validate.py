#!/usr/bin/python
# -*- coding: utf-8 -*-
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__copyright__ = "(c) 2020 Dell Inc. or its subsidiaries. All rights reserved."

__metaclass__ = type

DOCUMENTATION = '''
module: vlt_validate
author: "Senthil Kumar Ganesan (@skg-net)"
short_description: Validate the vlt info, raise an error if peer is not in up state
description:

  - Troubleshoot the show vlt info and raise an error if peer is not up.

options:
    show_vlt:
        description:
            - show vlt output
        type: 'list'
        required: True
    show_system_network_summary:
         description:
            - show system summary output
         type: 'list'
         required: True
    intended_vlt_pairs:
         description:
            - intended vlt pair intput to verify with actual
         type: 'list'
         required: True

'''
EXAMPLES = '''
Copy below YAML into a playbook (e.g. play.yml) and run as follows:

#$ ansible-playbook -i inv play.yml
name: show system Configuration
hosts: localhost
connection: local
gather_facts: False
tasks:
 - name: "Get Dell EMC OS10 Show run vlt"
   os10_command:
     commands:
       - command: "show running-configuration vlt | grep vlt-domain"
     provider: "{{ hostvars[item].cli }}"
   with_items: "{{ groups['all'] }}"
   register: show_run_vlt
 - set_fact:
      output_vlt:  "{{ output_vlt|default([])+ [{'host': item.invocation.module_args.provider.host, 'inv_name': item.item,
                                                 'stdout_show_vlt': item.stdout.0}] }}"
   loop: "{{ show_run_vlt.results }}"
 - debug: var=output_vlt
 - name: "Get Dell EMC OS10 Show vlt info"
   os10_command:
     commands:
       - command: "show vlt {{ item.stdout_show_vlt.split()[1] }} | display-xml"
     provider: "{{ hostvars[item.inv_name].cli }}"
   with_items: "{{ output_vlt }}"
   register: show_vlt
 - set_fact:
      vlt_out:  "{{ vlt_out|default([])+ [{'host': item.invocation.module_args.provider.host, 'inv_name': item.item, 'show_vlt_stdout': item.stdout.0}] }}"
   loop: "{{ show_vlt.results }}"
   register: vlt_output
 - name: call lib to convert vlt info from xml to dict format
   base_xml_to_dict:
      cli_responses: "{{ item.show_vlt_stdout }}"
   with_items:
     - "{{ vlt_out }}"
   register: vlt_dict_output
 - name: "Get Dell EMC OS10 Show system"
   import_role:
     name: os10_fabric_summary
   register: show_system_network_summary
 - name: call lib to process
   vlt_validate:
       show_vlt : "{{ vlt_dict_output.results }}"
       show_system_network_summary: "{{ show_system_network_summary.msg.results }}"
       intended_vlt_pairs: "{{ intended_vlt_pairs }}"
   register: show_vlt_info

'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from collections import OrderedDict
import traceback


class VltValidation(object):
    def __init__(self):
        self.module = AnsibleModule(argument_spec=self.get_fields())
        self.show_vlt = self.module.params['show_vlt']
        self.show_system_network_summary = self.module.params['show_system_network_summary']
        self.intended_vlt_pairs = self.module.params['intended_vlt_pairs']
        self.exit_msg = OrderedDict()

    def get_fields(self):
        spec_fields = {
            'show_vlt': {
                'type': 'list',
                'required': True
            },
            'show_system_network_summary': {
                'type': 'list',
                'required': True
            },
            'intended_vlt_pairs': {
                'type': 'list',
                'required': True
            }
        }
        return spec_fields

    # get switch inv name from mac
    def get_switch_inv_name_from_mac(self, mac):
        inv_name = None
        for show_system in self.show_system_network_summary:
            if (str.lower(show_system["node-mac"])) == (str.lower(mac)):
                inv_name = show_system.get("inv_name")
                break
        return inv_name

    def validate_vlt_pairs(self, actual_vlt_dict):
        final_out = list()
        intended_vlt_list = self.intended_vlt_pairs
        for intended_vlt in intended_vlt_list:
            intended_primary = intended_vlt.get("primary")
            intended_secondary = intended_vlt.get("secondary")
            actual_vlt = actual_vlt_dict.get(intended_primary)
            temp_dict = {}
            if actual_vlt is not None:
                actual_secondary = actual_vlt.get("secondary")
                secondary_status = actual_vlt.get("secondary_status")
                if actual_secondary is not None and intended_secondary != actual_secondary:
                    temp_dict["error_type"] = "secondary_mismatch"
                    temp_dict["intended_primary"] = intended_primary
                    temp_dict["intended_secondary"] = intended_secondary
                    temp_dict["secondary"] = actual_secondary
                    reason = "config mismatch as {0} is expected, but the actual secondary is {1} " .format(
                        intended_secondary, actual_secondary)
                    temp_dict["possible_reason"] = reason
                    final_out.append(temp_dict)
                else:
                    if actual_secondary is None:
                        temp_dict["intended_primary"] = intended_primary
                        temp_dict["intended_secondary"] = intended_secondary
                        temp_dict["error_type"] = "peer_missing"
                        reason = "peer info is not configured or peer interface is down"
                        temp_dict["possible_reason"] = reason
                        final_out.append(temp_dict)
                    elif intended_secondary == actual_secondary and secondary_status != "up":
                        temp_dict["intended_primary"] = intended_primary
                        temp_dict["intended_secondary"] = intended_secondary
                        temp_dict["secondary"] = actual_secondary
                        temp_dict["error_type"] = "peer_down"
                        reason = "peer interface is down"
                        temp_dict["possible_reason"] = reason
                        final_out.append(temp_dict)
            else:
                temp_dict["intended_primary"] = intended_primary
                temp_dict["intended_secondary"] = intended_secondary
                temp_dict["error_type"] = "vlt_config_missing"
                temp_dict["possible_reason"] = "vlt is not configured"
                final_out.append(temp_dict)
        return final_out

    def parse_vlt_output(self):
        show_vlt_dict = {}
        for show_list in self.show_vlt:
            source_switch = None
            item = show_list.get("item")
            if item is not None:
                inv_info = item.get("inv_name")
                source_switch = inv_info.get("inv_name")
            msg = show_list.get("msg")
            if msg is not None:
                result = msg.get("result")
                for sub_result in result:
                    vlt_dict = {}
                    rpc_reply = sub_result.get("rpc-reply")
                    data = rpc_reply.get("data")
                    if data is not None:
                        topo_oper_data = data.get("topology-oper-data")
                        if topo_oper_data is not None:
                            vlt_domain = topo_oper_data.get("vlt-domain")
                            if vlt_domain is not None:
                                local_info = vlt_domain.get("local-info")
                                if local_info is not None:
                                    local_role = local_info.get("role")
                                    vlt_dict[local_role] = source_switch
                                    local_mac = local_info.get("system-mac")
                                    vlt_dict[local_role + "_mac"] = local_mac
                                peer_info = vlt_domain.get("peer-info")
                                if peer_info is not None:
                                    peer_mac = peer_info.get("system-mac")
                                    peer_switch = self.get_switch_inv_name_from_mac(
                                        peer_mac)
                                    peer_role = peer_info.get("role")
                                    vlt_dict[peer_role] = peer_switch
                                    vlt_dict[peer_role + "_mac"] = peer_mac
                                    peer_status = peer_info.get("peer-status")
                                    vlt_dict[peer_role +
                                             "_status"] = peer_status
                        if bool(vlt_dict):
                            primary_switch = vlt_dict.get("primary")
                            vlt_data = show_vlt_dict.get(primary_switch)
                            if vlt_data is None:
                                # update database specific to primary, it helps
                                # to avoid to skip duplicate data
                                show_vlt_dict[primary_switch] = vlt_dict
        return show_vlt_dict

    def perform_action(self):
        try:
            actual_vlt_dict = self.parse_vlt_output()
            final_out = self.validate_vlt_pairs(actual_vlt_dict)
            self.exit_msg.update({"results": final_out})
            self.module.exit_json(changed=False, msg=self.exit_msg)
        except Exception as e:
            self.module.fail_json(
                msg=to_native(e),
                exception=traceback.format_exc())


def main():
    module_instance = VltValidation()
    module_instance.perform_action()


if __name__ == '__main__':
    main()

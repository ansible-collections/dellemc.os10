#!/usr/bin/python
# -*- coding: utf-8 -*-
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__copyright__ = "(c) 2020 Dell Inc. or its subsidiaries. All rights reserved."

__metaclass__ = type

DOCUMENTATION = '''
module: mtu_validate
author: "Senthil Kumar Ganesan (@skg-net)"
short_description: Validate the MTU value for lldp neighbors
description:

  - Get the wiring info using lldp output and show system network summary.

options:
    show_lldp_neighbors_list:
        description:
            - show lldp neighbor output
        type: 'list'
        required: True
    show_system_network_summary:
        description:
            - show system network summary output
        type: 'list'
        required: True
    show_ip_intf_brief:
        description:
            - show ip intf brief
        type: 'list'
        required: True
'''
EXAMPLES = '''
Copy below YAML into a playbook (e.g. play.yml) and run follows:

#$ ansible-playbook -i inv play.yml
name: show mtu mismatch info
hosts: localhost
connection: local
gather_facts: False
tasks:
 - name: "Get Dell EMC OS10 MTU mismatch info"
   os10_command:
     commands:
       - command: "show lldp neighbors"
       - command: "show ip interface brief | display-xml"
     provider: "{{ hostvars[item].cli }}"
   with_items: "{{ groups['all'] }}"
   register: show_lldp
 - set_fact:
      output:  "{{ output|default([])+ [{'host': item.invocation.module_args.provider.host, 'inv_name': item.item,
                                         'stdout_show_lldp': item.stdout.0, 'stdout_show_ip': item.stdout.1 }] }}"
   loop: "{{ show_lldp.results }}"
 - debug: var=output
 - local_action: copy content={{ output }} dest=show1
 - name: call lib to convert ip interface info from xml to dict format
   base_xml_to_dict:
      cli_responses: "{{ item.stdout_show_ip }}"
   with_items: "{{ output }}"
   register: show_ip_intf_list
 - local_action: copy content={{ show_ip_intf_list }} dest=show_ip

 - name: "Get Dell EMC OS10 Show system"
   import_role:
     name: os10_fabric_summary
   register: show_system_network_summary
 - debug: var=show_system_network_summary
 - name: call lib to process
   mtu_validate:
     show_lldp_neighbors_list: "{{ output }}"
     show_system_network_summary: "{{ show_system_network_summary.msg.results }}"
     show_ip_intf_brief: "{{ show_ip_intf_list.results }}"
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from collections import OrderedDict
import re
import traceback


class MtuValidation(object):
    def __init__(self):
        self.module = AnsibleModule(argument_spec=self.get_fields())
        self.show_lldp_neighbors_list = self.module.params['show_lldp_neighbors_list']
        self.show_system_network_summary = self.module.params['show_system_network_summary']
        self.show_ip_intf_brief = self.module.params['show_ip_intf_brief']
        self.exit_msg = OrderedDict()

    def get_fields(self):
        spec_fields = {
            'show_lldp_neighbors_list': {
                'type': 'list',
                'required': True
            },
            'show_system_network_summary': {
                'type': 'list',
                'required': True
            },
            'show_ip_intf_brief': {
                'type': 'list',
                'required': True
            }
        }
        return spec_fields

    def get_int_mtu(self, spine, port):
        for show_list in self.show_ip_intf_brief:
            inv_name = show_list["item"]["inv_name"]
            if spine != inv_name:
                continue
            value = show_list["msg"]["result"]
            for data in value:
                intf_list = data["rpc-reply"]["bulk"]["data"]["interface"]
                for val in intf_list:
                    intf_name = val["name"]
                    if intf_name == port:
                        mtu = val["mtu"]
                        return mtu
        return None

    # form actual neighbors per network with help of lldp output and show
    # sytem output
    def get_actual_neigbor(self, lldp_list):
        final_out = list()
        for show_system in self.show_system_network_summary:
            for lldp in lldp_list:
                if show_system["host"] != lldp["host"] and "node-mac" in show_system and "rem_mac" in lldp:
                    rem_host = show_system["host"]
                    loc_host = lldp["host"]
                    # check whether lldp output mac match with system summary
                    # mac and collect port and host info
                    dest_switch = show_system["inv_name"]
                    source_switch = lldp["inv_name"]
                    lldp_mac = lldp["rem_mac"]
                    for index, rem_mac in enumerate(lldp_mac):
                        final_dict = {}
                        if (str.lower(
                                show_system["node-mac"])) == (str.lower(rem_mac)):
                            final_dict["source_switch"] = source_switch
                            final_dict["dest_switch"] = dest_switch
                            final_dict["source_port"] = lldp["loc_port"][index]
                            final_dict["dest_port"] = lldp["rem_port"][index]
                            source_mtu = self.get_int_mtu(
                                source_switch, final_dict["source_port"])
                            dest_mtu = self.get_int_mtu(
                                dest_switch, final_dict["dest_port"])
                            if source_mtu is not None:
                                final_dict["source_mtu"] = source_mtu
                            if dest_mtu is not None:
                                final_dict["dest_mtu"] = dest_mtu
                            final_out.append(final_dict)
        return final_out

    def parse_lldp_output(self):
        nbr_list = list()
        for cli in self.show_lldp_neighbors_list:
            out_dict = {}
            loc_port = list()
            rem_port = list()
            rem_mac = list()
            for key, value in cli.items():
                if key == "host":
                    out_dict[key] = value
                if key == "inv_name":
                    out_dict[key] = value
                if key == "stdout_show_lldp":
                    output = str(value)
                    lldp_regexp = r"(\S+)\s+(\S+)\s+(\S+)\s+(\S+)"
                    lines = output.splitlines()
                    for line in lines:
                        if "Loc PortID" in line:
                            continue
                        match = re.match(lldp_regexp, line)
                        if match:
                            val = match.groups()
                            loc_port.append(val[0])
                            rem_port.append(val[2])
                            rem_mac.append(val[3])
                    out_dict["loc_port"] = loc_port
                    out_dict["rem_port"] = rem_port
                    out_dict["rem_mac"] = rem_mac
            nbr_list.append(out_dict)
        return nbr_list

    def get_mtu_mismatch_info(self, nbr_list):
        mtu_list = list()
        for nbr in nbr_list:
            if nbr["source_mtu"] != nbr["dest_mtu"]:
                nbr["error"] = "mismatch"
                mtu_list.append(nbr)
        return mtu_list

    def perform_action(self):
        try:
            lldp_list = self.parse_lldp_output()
            actual_nbr = self.get_actual_neigbor(lldp_list)
            mtu_mismatch_list = self.get_mtu_mismatch_info(actual_nbr)
            if len(mtu_mismatch_list) > 0:
                self.exit_msg.update({"results": mtu_mismatch_list})
            else:
                self.exit_msg.update(
                    {"results": "There is no MTU mistmatch between neighbors"})
            self.module.exit_json(changed=False, msg=self.exit_msg)
        except Exception as e:
            self.module.fail_json(
                msg=to_native(e),
                exception=traceback.format_exc())


def main():
    module_instance = MtuValidation()
    module_instance.perform_action()


if __name__ == '__main__':
    main()

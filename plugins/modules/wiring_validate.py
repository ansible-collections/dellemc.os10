#!/usr/bin/python
# -*- coding: utf-8 -*-
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__copyright__ = "(c) 2020 Dell Inc. or its subsidiaries. All rights reserved."

__metaclass__ = type

DOCUMENTATION = '''
module: wiring_validate
author: "Senthil Kumar Ganesan (@skg-net)"
short_description: Validate the wiring based on the planned wiring details
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
    planned_neighbors:
        description:
            - planned neighbours input from group_var to compare actual
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
- name: "Get Dell EMC OS10 Show lldp"
  os10_command:
    commands:
      - command: "show lldp neighbors"
    provider: "{{ hostvars[item].cli }}"
  with_items: "{{ groups['all'] }}"
  register: show_lldp
- local_action: copy content={{ show_lldp }} dest=show
- set_fact:
     output_lldp:  "{{ output_lldp|default([])+ [{'host': item.invocation.module_args.provider.host, 'inv_name': item.item,
                                                  'stdout_show_lldp': item.stdout}] }}"
  loop: "{{ show_lldp.results }}"
- debug: var=output_lldp
- name: "Get Dell EMC OS10 Show system"
  import_role:
    name: os10_fabric_summary
  register: show_system_network_summary
- debug: var=show_system_network_summary
- name: call lib to process
  wiring_validate:
    show_lldp_neighbors_list: "{{ output_lldp }}"
    show_system_network_summary: "{{ show_system_network_summary.msg.results }}"
    planned_neighbors: "{{ intended_neighbors }}"
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from collections import OrderedDict
import re
import traceback


class WiringValidation(object):
    def __init__(self):
        self.module = AnsibleModule(argument_spec=self.get_fields())
        self.show_lldp_neighbors_list = self.module.params['show_lldp_neighbors_list']
        self.show_system_network_summary = self.module.params['show_system_network_summary']
        self.planned_neighbors = self.module.params['planned_neighbors']
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
            'planned_neighbors': {
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

    # get service tag for switch

    def get_service_tag_and_mac(self):
        svc_tag_mac = {}
        for show_system in self.show_system_network_summary:
            temp_dict = {}
            temp_dict["svc-tag"] = show_system.get("service-tag")
            temp_dict["node-mac"] = show_system.get("node-mac")
            if bool(temp_dict):
                svc_tag_mac[show_system["inv_name"]] = temp_dict
        return svc_tag_mac

    # form actual neighbors per network with help of lldp output and show
    # sytem output
    def get_actual_neigbor(self, lldp_list):
        final_out = list()
        for lldp in lldp_list:
            # check whether lldp output mac match with system summary mac and
            # collect port and host info
            source_switch = lldp["inv_name"]
            lldp_mac = lldp["rem_mac"]
            for index, rem_mac in enumerate(lldp_mac):
                final_dict = {}
                final_dict["source_switch"] = source_switch
                final_dict["source_port"] = lldp["loc_port"][index]
                final_dict["dest_port"] = lldp["rem_port"][index]
                dest_switch = self.get_switch_inv_name_from_mac(rem_mac)
                if dest_switch is not None:
                    final_dict["dest_switch"] = dest_switch
                else:
                    final_dict["dest_switch"] = "unknown"
                final_out.append(final_dict)
        return final_out

    def parse_lldp_output(self):
        nbr_list = list()
        for item in self.show_lldp_neighbors_list:
            out_dict = {}
            loc_port = list()
            rem_port = list()
            rem_mac = list()
            out_dict["host"] = item.get("host")
            out_dict["inv_name"] = item.get("inv_name")
            show_lldp_output = item.get("stdout_show_lldp")
            if show_lldp_output is not None:
                output = str(show_lldp_output[0])
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
            if bool(out_dict):
                nbr_list.append(out_dict)
        return nbr_list

    def perform_action(self):
        try:
            lldp_list = self.parse_lldp_output()
            actual_nbr = self.get_actual_neigbor(lldp_list)
            svc_tag_mac = self.get_service_tag_and_mac()
            # Validate the planned neighbors with actual neighbors
            mismatch_list = list()
            for planned_neighbors in self.planned_neighbors:
                bflag = False
                if planned_neighbors not in actual_nbr:
                    for actual_neighbors in actual_nbr:
                        if (actual_neighbors["source_switch"] == planned_neighbors["source_switch"]
                                and actual_neighbors["source_port"] == planned_neighbors["source_port"]):
                            if (actual_neighbors["dest_switch"] !=
                                    planned_neighbors["dest_switch"]):
                                bflag = True
                                if (actual_neighbors["dest_switch"]
                                        != "unknown"):
                                    reason = (
                                        "Destination switch is not an expected value, "
                                        "expected switch: {0},port: {1}; actual switch: {2}(svc-tag:{3}, node_mac:{4}), port: {5}" .format(
                                            planned_neighbors["dest_switch"],
                                            planned_neighbors["dest_port"],
                                            actual_neighbors["dest_switch"],
                                            svc_tag_mac.get(
                                                actual_neighbors["dest_switch"]).get("svc-tag"),
                                            svc_tag_mac.get(
                                                actual_neighbors["dest_switch"]).get("node-mac"),
                                            actual_neighbors["dest_port"]))
                                else:
                                    reason = (
                                        "Destination switch is not an expected value, "
                                        "expected switch: {0},port: {1}; actual switch: {2}, port: {3}" .format(
                                            planned_neighbors["dest_switch"],
                                            planned_neighbors["dest_port"],
                                            actual_neighbors["dest_switch"],
                                            actual_neighbors["dest_port"]))
                                planned_neighbors["reason"] = reason
                                planned_neighbors["error_type"] = "link-mismatch"
                                break
                            if(actual_neighbors["dest_port"] != planned_neighbors["dest_port"]):
                                bflag = True
                                reason = (
                                    "Destination switch port is not an expected value, "
                                    "expected port: {0} actual port: {1}" .format(
                                        planned_neighbors["dest_port"],
                                        actual_neighbors["dest_port"]))
                                planned_neighbors["reason"] = reason
                                planned_neighbors["error_type"] = "link-mismatch"
                                break
                    if not bflag:
                        reason = "link is not found for source switch: {0},port: {1}".format(
                            planned_neighbors["source_switch"], planned_neighbors["source_port"])
                        planned_neighbors["reason"] = reason
                        planned_neighbors["error_type"] = "link-missing"
                    mismatch_list.append(planned_neighbors)

            self.exit_msg.update({"results": mismatch_list})
            self.module.exit_json(changed=False, msg=self.exit_msg)
        except Exception as e:
            self.module.fail_json(
                msg=to_native(e),
                exception=traceback.format_exc())


def main():
    module_instance = WiringValidation()
    module_instance.perform_action()


if __name__ == '__main__':
    main()

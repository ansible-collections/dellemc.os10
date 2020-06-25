#!/usr/bin/python
# -*- coding: utf-8 -*-
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__copyright__ = "(c) 2020 Dell Inc. or its subsidiaries. All rights reserved."

__metaclass__ = type

DOCUMENTATION = '''
module: bgp_validate
author: "Senthil Kumar Ganesan (@skg-net)"
short_description: Validate the bgp neighbor state,raise error if it is not in established state
description:

  - Troubleshoot the bgp neighor state info using show ip bgp summary and show ip interface brief.

options:
    show_ip_bgp:
        description:
            - show ip bgp summary output
        type: 'list'
        required: True
    show_ip_intf_brief:
        description:
            - show ip interface brief output
        type: 'list'
        required: True
    bgp_neighbors:
        description:
            - planned neighbours input from group_var to compare actual
        type: 'list'
        required: True
'''
EXAMPLES = '''
Copy below YAML into a playbook (e.g. play.yml) and run as follows:

#$ ansible-playbook -i inv play.yml
name: Validate BGP configuration
hosts: localhost
connection: local
gather_facts: False
tasks:
  - name: "Get Dell EMC OS10 Show ip bgp summary"
    os10_command:
      commands:
        - command: "show ip bgp summary | display-xml"
        - command: "show ip interface brief | display-xml"
      provider: "{{ hostvars[item].cli }}"
    with_items: "{{ groups['all'] }}"
    register: show_bgp
  - set_fact:
       output_bgp:  "{{ output_bgp|default([])+ [{'host': item.invocation.module_args.provider.host, 'inv_name': item.item,
                                                  'stdout_show_bgp': item.stdout.0, 'stdout_show_ip': item.stdout.1}] }}"
    loop: "{{ show_bgp.results }}"
  - debug: var=output_bgp
  - local_action: copy content={{ output_bgp }} dest=show
  - name: call lib to convert bgp info from xml to dict format
    base_xml_to_dict:
       cli_responses: "{{ item.stdout_show_bgp }}"
    with_items:
      - "{{ output_bgp }}"
    register: show_bgp_list
  - name: call lib to convert ip interface info from xml to dict format
    base_xml_to_dict:
       cli_responses: "{{ item.stdout_show_ip }}"
    with_items:
      - "{{ output_bgp }}"
    register: show_ip_intf_list
  - name: call lib for bgp validation
    bgp_validate:
      show_ip_bgp: "{{ show_bgp_list.results  }}"
      show_ip_intf_brief: "{{ show_ip_intf_list.results  }}"
      bgp_neighbors: "{{ intended_bgp_neighbors }}"
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from collections import OrderedDict
import traceback


class BgpValidation(object):
    def __init__(self):
        self.module = AnsibleModule(argument_spec=self.get_fields())
        self.show_ip_bgp = self.module.params['show_ip_bgp']
        self.show_ip_intf_brief = self.module.params['show_ip_intf_brief']
        self.bgp_neighbors = self.module.params['bgp_neighbors']
        self.exit_msg = OrderedDict()

    def get_fields(self):
        spec_fields = {
            'show_ip_bgp': {
                'type': 'list',
                'required': True
            },
            'show_ip_intf_brief': {
                'type': 'list',
                'required': True
            },
            'bgp_neighbors': {
                'type': 'list',
                'required': True
            }
        }
        return spec_fields

    def parse_bgp_output(self):
        show_bgp_dict = {}
        for show_list in self.show_ip_bgp:
            show_bgp_list = list()
            item = show_list.get("item")
            inv_name = None
            if item is not None:
                inv_name = item.get("inv_name")
            msg = show_list.get("msg")
            if msg is not None:
                result = msg.get("result")
                if result is not None:
                    for sub_result in result:
                        bgp_dict = {}
                        rpc_reply = sub_result.get("rpc-reply")
                        if rpc_reply is not None:
                            bulk = rpc_reply.get("bulk")
                            if bulk is not None:
                                data = bulk.get("data")
                                if data is not None and "peer-oper" in data:
                                    peer_oper = data.get("peer-oper")
                                    if peer_oper is not None and "remote-address" in peer_oper:
                                        bgp_dict["remote_address"] = peer_oper.get(
                                            "remote-address")
                                        bgp_dict["bgp-state"] = peer_oper.get(
                                            "bgp-state")
                                        show_bgp_list.append(bgp_dict)
                    show_bgp_dict[inv_name] = show_bgp_list
        return show_bgp_dict

    def parse_ip_intf_output(self):
        show_ip_dict = {}
        for show_list in self.show_ip_intf_brief:
            show_ip_list = list()
            item = show_list.get("item")
            inv_name = None
            if item is not None:
                inv_name = item.get("inv_name")
            msg = show_list.get("msg")
            if msg is not None:
                result = msg.get("result")
                if result is not None:
                    for sub_result in result:
                        rpc_reply = sub_result.get("rpc-reply")
                        if rpc_reply is not None:
                            bulk = rpc_reply.get("bulk")
                            if bulk is not None:
                                data = bulk.get("data")
                                if data is not None:
                                    sub_val = data.get("interface")
                                    if sub_val is not None:
                                        for val in sub_val:
                                            intf_dict = {}
                                            if "ipv4-info" in val:
                                                ipv4_info = val.get(
                                                    "ipv4-info")
                                                if ipv4_info is not None and "addr" in ipv4_info:
                                                    intf_dict["address"] = ipv4_info.get(
                                                        "addr")
                                                    intf_dict["if_name"] = val.get(
                                                        "name")
                                                    intf_dict["oper_status"] = val.get(
                                                        "oper-status")
                                            if bool(intf_dict):
                                                show_ip_list.append(intf_dict)
                    show_ip_dict[inv_name] = show_ip_list
        return show_ip_dict

    def get_intf_info_per_ip(self, intf_dict):
        final_intf_dict = {}
        for key1, value1 in intf_dict.items():
            intf_list = value1
            intf_dict = {}
            for ip in intf_list:
                intf_info = {}
                ip_address = ip.get("address")
                intf_address = ip_address.split('/')
                intf_ip = intf_address[0]
                intf_info["if_name"] = ip.get("if_name")
                intf_info["oper_status"] = ip.get("oper_status")
                intf_info["dest_switch"] = key1
                intf_dict[intf_ip] = intf_info
            if bool(intf_dict):
                final_intf_dict[key1] = intf_dict
        return final_intf_dict

    def get_intf_info_from_neighbor_ip(
            self, source_switch, neighbor_ip, intf_dict):
        final_intf_info = {}
        intf_dict_per_ip = self.get_intf_info_per_ip(intf_dict)
        for key, value in intf_dict_per_ip.items():
            switch_name = key
            if source_switch == switch_name:
                continue
            intf_info = value.get(neighbor_ip)
            if intf_info is None:
                continue
            final_intf_info = intf_info
            break
        return final_intf_info

    def get_bgp_final_nbr_list(self, bgp_dict, intf_dict):
        actual_bgp_dict = {}
        final_bgp_dict = {}
        for key, value in bgp_dict.items():
            actual_bgp_list = list()
            bgp_list = value
            source_switch = key
            for bgp in bgp_list:
                final_dict = {}
                bgp_state = bgp.get("bgp-state")
                remote_address = bgp.get("remote_address")
                reason = "neighbor config missing"
                error_type = "config_missing"
                intf_info = self.get_intf_info_from_neighbor_ip(
                    source_switch, remote_address, intf_dict)
                if bool(intf_info):
                    dest_switch = intf_info.get("dest_switch")
                    remote_port = intf_info.get("if_name")
                    oper_status = intf_info.get("oper_status")
                    final_dict["source_switch"] = source_switch
                    final_dict["bgp_neighbor"] = remote_address
                    final_dict["bgp_state"] = bgp_state
                    if bgp_state != "established":
                        if oper_status != "up":
                            reason = (
                                "remote port {0} {1} is {2}" .format(
                                    dest_switch, remote_port, oper_status))
                            error_type = "remote_port_down"
                        final_dict["error_type"] = error_type
                        final_dict["possible_reason"] = reason
                else:
                    final_dict["source_switch"] = source_switch
                    final_dict["bgp_neighbor"] = remote_address
                    final_dict["bgp_state"] = bgp_state
                    final_dict["error_type"] = error_type
                    final_dict["possible_reason"] = reason
                actual_bgp_list.append(final_dict)
            actual_bgp_dict[source_switch] = actual_bgp_list
        # check actual with intended neighbor to display the result
        intended_list = list()
        for intended_bgp_neighbor in self.bgp_neighbors:
            planned_source_switch = intended_bgp_neighbor.get("source_switch")
            planned_nbr_list = intended_bgp_neighbor.get("neighbor_ip")
            actual_nbr_list = actual_bgp_dict.get(planned_source_switch)
            if planned_nbr_list is None or actual_nbr_list is None:
                continue
            for actual_nbr in actual_nbr_list:
                actual_source_switch = actual_nbr.get("source_switch")
                actual_bgp_neighbor = actual_nbr.get("bgp_neighbor")
                actual_bgp_state = actual_nbr.get("bgp_state")
                if actual_bgp_neighbor in planned_nbr_list:
                    # Don't add established neighbor in result
                    if actual_bgp_state != "established":
                        intended_list.append(actual_nbr)
                    planned_nbr_list.remove(actual_bgp_neighbor)
                else:
                    reason = "neighbor {0} is not an intended, please add this neighbor in the intended_bgp_neighbors".format(
                        actual_bgp_neighbor)
                    actual_nbr["bgp_neighbor"] = "-"
                    actual_nbr["error_type"] = "not_an_intended_neighbor"
                    actual_nbr["possible_reason"] = reason
                    intended_list.append(actual_nbr)
            # Add the missed planned info which are not present in actual
            # results
            for planned_nbr in planned_nbr_list:
                reason = "neighbor config missing"
                temp_dict = {}
                temp_dict["source_switch"] = planned_source_switch
                temp_dict["bgp_neighbor"] = planned_nbr
                temp_dict["error_type"] = "config_missing"
                temp_dict["possible_reason"] = reason
                intended_list.append(temp_dict)
        return intended_list

    def perform_action(self):
        try:
            bgp_dict = self.parse_bgp_output()
            intf_dict = self.parse_ip_intf_output()
            final_bgp_list = self.get_bgp_final_nbr_list(bgp_dict, intf_dict)
            self.exit_msg.update({"results": final_bgp_list})
            self.module.exit_json(changed=False, msg=self.exit_msg)
        except Exception as e:
            self.module.fail_json(
                msg=to_native(e),
                exception=traceback.format_exc())


def main():
    module_instance = BgpValidation()
    module_instance.perform_action()


if __name__ == '__main__':
    main()

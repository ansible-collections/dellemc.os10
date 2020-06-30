#!/usr/bin/python
# -*- coding: utf-8 -*-
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__copyright__ = "(c) 2020 Dell Inc. or its subsidiaries. All rights reserved."

__metaclass__ = type

DOCUMENTATION = '''
module: show_system_network_summary
author: "Senthil Kumar Ganesan (@skg-net)"
short_description: Operations for show_system_network output in json/yaml format.
description:

  - Get the show system inforamtion of a Leaf-Spine.

options:
    output_type:
        type: str
        description:
            - json or yaml
            - Default value is json
        default: json
        required: False
    cli_responses:
        type: list
        required: True
        description:
            - show system command xml output
'''
EXAMPLES = '''
Copy below YAML into a playbook (e.g. play.yml) and run as follows:

#$ ansible-playbook -i inv show.yml
name: show system Configuration
hosts: localhost
connection: local
gather_facts: False
vars:
  cli:
    username: admin
    password: admin
tasks:
- name: "Get Dell EMC OS10 Show system summary"
  os10_command:
    commands: ['show system | display-xml']
    provider: "{{ hostvars[item].cli }}"
  with_items: "{{ groups['all'] }}"
  register: show_system
- set_fact:
     output:  "{{ output|default([])+ [{'inv_name': item.item, 'host': item.invocation.module_args.provider.host, 'stdout_show_system': item.stdout}] }}"
  loop: "{{ show_system.results }}"
- debug: var=output
- name: "show system network call to lib "
  show_system_network_summary:
    cli_responses: "{{ output}} "
    output_type: "{{ output_method if output_method is defined else 'json' }}"
  register: show_system_network_summary
- debug: var=show_system_network_summary
'''

import re
from ansible_collections.dellemc.os10.plugins.module_utils.network.base_network_show import BaseNetworkShow


class ShowSystemNetworkSummary(BaseNetworkShow):
    def __init__(self):
        BaseNetworkShow.__init__(self)
        self.cli_responses = self.module.params['cli_responses']
        self.output_type = self.module.params['output_type']
        self.changed = False

    def get_fields(self):
        spec_fields = {
            'cli_responses': {
                'type': 'list',
                'required': True
            },
            'output_type': {
                'type': 'str',
                'default': "json",
                'required': False
            }
        }
        return spec_fields

    def perform_action(self):
        out = list()
        show_system_summary = self.cli_responses
        if len(show_system_summary) > 0:
            for item in show_system_summary:
                out_dict = {}
                host = item.get("host")
                inv_name = item.get("inv_name")
                show_system_response = item.get("stdout_show_system")
                if show_system_response is not None:
                    result = BaseNetworkShow.xml_to_dict(
                        self, show_system_response[0])
                    rpc_reply = result.get("rpc-reply")
                    if rpc_reply is not None:
                        data = rpc_reply.get("data")
                        if data is not None:
                            out_dict["host"] = host
                            out_dict["inv_name"] = inv_name
                            system_state = data.get("system-state")
                            if system_state is not None:
                                system_status = system_state.get(
                                    "system-status")
                                if system_status is not None:
                                    out_dict["hostname"] = system_status.get(
                                        "hostname")
                            system = data.get("system")
                            if system is not None:
                                node = system.get("node")
                                if node is not None:
                                    out_dict["node-mac"] = node.get("node-mac")
                                    unit = node.get("unit")
                                    if unit is not None:
                                        out_dict["software-version"] = unit.get(
                                            "software-version")
                                    mfg_info = node.get("mfg-info")
                                    if mfg_info is not None:
                                        out_dict["service-tag"] = mfg_info.get(
                                            "service-tag")
                                        out_dict["device type"] = mfg_info.get(
                                            "product-name")
                            if bool(out_dict):
                                out.append(out_dict)
        if self.output_type != "json":
            self.exit_msg.update(
                {"results": (BaseNetworkShow.dict_to_yaml(self, out))})
        else:
            self.exit_msg.update({"results": (out)})
        self.module.exit_json(changed=False, msg=self.exit_msg)


def main():
    module_instance = ShowSystemNetworkSummary()
    module_instance.perform_action()


if __name__ == '__main__':
    main()

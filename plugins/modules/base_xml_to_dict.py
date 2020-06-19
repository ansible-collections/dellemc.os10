#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__copyright__ = "(c) Copyright 2020 Dell Inc. or its subsidiaries. All rights reserved."

__metaclass__ = type


DOCUMENTATION = '''
module: base_xml_to_dict
author: "Senthil Kumar Ganesan (@skg-net)"
short_description: Operations for show command output convertion from xml to json format.
description:

  - Get the show system inforamtion of a Leaf-Spine.

options:
    cli_responses:
        type: str
        description:
            - show command xml output
        required: True
'''
EXAMPLES = '''
Copy below YAML into a playbook (e.g. play.yml) and run as follows:

#$ ansible-playbook -i inv play.yml
name: setup the plabook to get show command output in dict format
hosts: localhost
connection: local
gather_facts: False
vars:
  cli:
    username: admin
    password: admin
tasks:
- name: "Get Dell EMC OS10 Show output in dict format"
  os10_command:
    commands: "{{ command_list }}"
  register: show
- debug: var=show
- name: call to lib to get output in dict
  base_xml_to_dict:
    cli_responses: "{{ item }}"
  loop: "{{ show.stdout }}"
'''

from ansible.module_utils._text import to_native
from ansible.module_utils.basic import AnsibleModule
from collections import OrderedDict
import traceback

LIB_IMP_ERR = None
ERR_MSG = None
try:
    import xmltodict
    HAS_LIB = True
except Exception as e:
    HAS_LIB = False
    ERR_MSG = to_native(e)
    LIB_IMP_ERR = traceback.format_exc()


class XmlToDictAnsibleModule(object):
    """The goal of this class is to convert xml input to dict"""

    def __init__(self):
        self.module = AnsibleModule(argument_spec=self.get_fields())
        self.cli_responses = self.module.params['cli_responses']
        self.exit_msg = OrderedDict()

    def get_fields(self):
        """Return valid fields"""
        base_fields = {
            'cli_responses': {
                'type': 'str',
                'required': True
            }
        }
        return base_fields

    def build_xml_list(self, xml_output):
        xml_str_list = []
        xml_declaration_tag = '<?xml version="1.0"?>\n'
        for data in xml_output.split('<?xml version="1.0"'):
            if not data:
                continue
            xml_data = ''.join(data.splitlines(True)[1:])
            xml_str_list.append(xml_declaration_tag + xml_data)

        return xml_str_list

    def perform_action(self):
        try:
            out = list()
            # the below line should be removed or not valid when the password
            # decrypt issue is resolved
            self.cli_responses = self.cli_responses.replace(
                "*-", '').replace("*", '')
            xml_str_list = self.build_xml_list(self.cli_responses)
            for xml_list in xml_str_list:
                out.append(xmltodict.parse(xml_list))

            self.exit_msg.update({"result": out})
            self.module.exit_json(changed=False, msg=self.exit_msg)
        except Exception as e:
            self.module.fail_json(
                msg=to_native(e),
                exception=traceback.format_exc())


def main():
    module_instance = XmlToDictAnsibleModule()
    if not HAS_LIB:
        module_instance.module.fail_json(msg=ERR_MSG,
                                         exception=LIB_IMP_ERR)
    module_instance.perform_action()


if __name__ == '__main__':
    main()

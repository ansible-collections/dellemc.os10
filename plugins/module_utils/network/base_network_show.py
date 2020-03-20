#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from collections import OrderedDict
import xmltodict

__copyright__ = "(c) Copyright 2020 Dell Inc. or its subsidiaries. All rights reserved."
__metaclass__ = type


class BaseNetworkShow(object):
    """The goal of this class is to extended by other in order to implement show system network view ansible modules"""

    def __init__(self):
        self.module = AnsibleModule(argument_spec=self.get_fields())
        self.exit_msg = OrderedDict()

    def xml_to_dict(self, value):

        return xmltodict.parse(value)

    # import yaml should be added on top to align with standard when yaml
    # format is supported
    def dict_to_yaml(self, value):
        import yaml
        return yaml.safe_dump(value, default_flow_style=False)


if __name__ == '__main__':
    pass

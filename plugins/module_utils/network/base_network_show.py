from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from collections import OrderedDict
import traceback

LIB_IMP_ERR = None
ERR_MSG = None
try:
    import xmltodict
    import yaml
    HAS_LIB = True
except Exception as e:
    HAS_LIB = False
    ERR_MSG = to_native(e)
    LIB_IMP_ERR = traceback.format_exc()

__copyright__ = "(c) Copyright 2020 Dell Inc. or its subsidiaries. All rights reserved."
__metaclass__ = type


class BaseNetworkShow(object):
    """The goal of this class is to extended by other in order to implement show system network view ansible modules"""

    def __init__(self):
        self.module = AnsibleModule(argument_spec=self.get_fields())
        if not HAS_LIB:
            self.module.fail_json(
                msg=ERR_MSG,
                exception=LIB_IMP_ERR)
        self.exit_msg = OrderedDict()

    def xml_to_dict(self, value):

        return xmltodict.parse(value)

    def dict_to_yaml(self, value):
        return yaml.safe_dump(value, default_flow_style=False)


if __name__ == '__main__':
    pass

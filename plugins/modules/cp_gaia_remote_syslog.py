#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Ansible module to manage CheckPoint Firewall (c) 2019
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


DOCUMENTATION = """
author: Majd Sharkia (@chkp-majds)
description:
- Modify remote system log server configuration
module: cp_gaia_remote_syslog
short_description: Modify remote system log server configuration
version_added: '2.0.0'
requirements:
- supported starting from gaia_api >= 1.7
options:

    server_ip:
        description: No Documentation available
        required: False
        type: str
    state:
        description: Ansible state which can be present/absent
        required: False
        type: str
        default: present
    protocol:
        description: Log protocol, Supported starting from R81.20
        required: False
        type: str
    port:
        description: Log port, Supported starting from R81.20
        required: False
        type: str
    level:
        description: No Documentation available
        required: False
        type: str

"""


EXAMPLES = """
- name: Modifying remote syslog messaging level
  cp_gaia_remote_syslog:
    "server_ip": "10.11.2.130"
    "level": "debug"

"""


RETURN = """
remote_syslog:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call


def main():
    # arguments for the module:
    fields = dict(
        server_ip=dict(type="str"),
        state=dict(type="str", default="present"),
        protocol=dict(type="str"),
        port=dict(type="str"),
        level=dict(type="str")
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'set-remote-syslog'
    ansible_release_version = 'v1.6/'

    res = chkp_api_call(module, api_call_object, ansible_release_version)
    module.exit_json(**res)


if __name__ == "__main__":
    main()

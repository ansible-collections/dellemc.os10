os10_fabric_summary
=====================================
This role is used to get show system information of all devices in the fabric. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The Fabric summary role requires an SSH connection for connectivity to a Dell EMC SmartFabric OS10 device. You can use any of the built-in OS connection variables.

Connection variables
--------------------

Ansible Dell EMC network roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories or inventory, or in the playbook itself.

| Key         | Required | Choices    | Description                                         |
|-------------|----------|------------|-----------------------------------------------------|
| ``ansible_host`` | yes      |            | Specifies the hostname or address for connecting to the remote device over the specified transport |
| ``ansible_port`` | no       |            | Specifies the port used to build the connection to the remote device; if value is unspecified, the `ANSIBLE_REMOTE_PORT` option is used; it defaults to 22 |
| ``os10_cli_user`` | no       |            | Specifies the username that authenticates the CLI login for the connection to the remote device; if value is unspecified, the default value is used  |
| ``os10_cli_pass`` | no       |            | Specifies the password that authenticates the connection to the remote device  |
| ``ansible_become`` | no       | yes, no\*   | Instructs the module to enter privileged mode on the remote device before sending any commands; if value is unspecified, the `ANSIBLE_BECOME` environment variable value is used, and the device attempts to execute all commands in non-privileged mode |
| ``ansible_become_method`` | no       | enable, sudo\*   | Instructs the module to allow the become method to be specified for handling privilege escalation; if value is unspecified, the `ANSIBLE_BECOME_METHOD` environment variable value is used |
| ``ansible_become_pass`` | no       |            | Specifies the password to use if required to enter privileged mode on the remote device; if ``ansible_become`` is set to no this key is not applicable |
| ``ansible_network_os`` | yes      | os10, null\*  | Loads the correct terminal and cliconf plugins to communicate with the remote device |

> **NOTE**: Asterisk (*) denotes the default value if none is specified.

Dependencies
------------

- *xmltodict*  library should be installed to get show command output in dict format from XML
- To install the package use the *pip install xmltodict* command

Example playbook
----------------

This example uses the *os10_fabric_summary* role to completely get the show attributes. It creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the ansible_network_os variable with the corresponding Dell EMC OS10 name.

The *os10_fabric_summary* role has a simple playbook that only references the *os10_fabric_summary* role.

**Sample hosts file**

        site1-spine1 ansible_host=10.11.180.21 os10_cli_user=admin os10_cli_pass=admin ansible_network_os=dellemc.os10.os10
        site1-spine2 ansible_host=10.11.180.22 os10_cli_user=admin os10_cli_pass=admin ansible_network_os=dellemc.os10.os10
        site2-spine1 ansible_host=10.11.180.23 os10_cli_user=admin os10_cli_pass=admin ansible_network_os=dellemc.os10.os10
        site2-spine2 ansible_host=10.11.180.24 os10_cli_user=admin os10_cli_pass=admin ansible_network_os=dellemc.os10.os10
        [spine]
        site1-spine1
        site1-spine2
        site2-spine1
        site2-spine2
        [LeafAndSpineSwitch:children]
        spine

**Sample host_vars/site1-spine1**

    
    cli:
       host: "{{ ansible_host }}"
       username: "{{ os10_cli_user | default('admin') }}"
       password: "{{ os10_cli_pass | default('admin') }}"
       timeout: 300
    os10_cli_user: xxxx
    os10_cli_pass: xxxx
    ansible_network_os: dellemc.os10.os10

**Simple playbook to setup fabric summary — provision.yaml**

    ---
    - name:  show system summary command
      hosts: localhost
      gather_facts: False
      connection: local
      roles:
        - os10_fabric_summary

**Run**

    ansible-playbook -i hosts provision.yaml

**Samaple Output**

    "results": [
        {
            "device type": "S6010-ON",
            "host": "10.11.180.21",
            "hostname": "host3",
            "inv_name": "site1-spine1",
            "node-mac": "e4:f0:04:9b:e5:dc",
            "service-tag": "D33FXC2",
            "software-version": "10.4.9999EX"
        },
        {
            "device type": "S6010-ON",
            "host": "10.11.180.22",
            "hostname": "host22",
            "inv_name": "site1-spine2",
            "node-mac": "e4:f0:04:9b:eb:dc",
            "service-tag": "J33FXC2",
            "software-version": "10.4.9999EX"
        },
        {
            "device type": "S6010-ON",
            "host": "10.11.180.24",
            "hostname": "site2-spine1",
            "inv_name": "site2-spine1",
            "node-mac": "e4:f0:04:9b:ee:dc",
            "service-tag": "343FXC2",
            "software-version": "10.4.9999EX"
        },
        {
            "device type": "S6010-ON",
            "host": "10.11.180.23",
            "hostname": "site2-spine2",
            "inv_name": "site2-spine2",
            "node-mac": "e4:f0:04:9b:f1:dc",
            "service-tag": "543FXC2",
            "software-version": "10.4.9999EX"
        }
    ]

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.
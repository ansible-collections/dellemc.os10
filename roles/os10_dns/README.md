DNS role
========

This role facilitates the configuration of the domain name service (DNS). This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The DNS role requires an SSH connection for connectivity to a Dell EMC OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- If `os10_cfg_generate` set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os10_dns keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``name_server`` | list | Configures DNS (see ``name_server.*``) | os10 |
| ``name_server.ip`` | list | Configures the name server IP | os10 |
| ``name_server.vrf`` | list | Configures VRF for each IP | os10 |
| ``name_server.state`` | string: absent,present\* | Deletes the name server IP if set to absent | os10 |
| ``domain_list`` | list | Configures domain-list (see ``domain_list.*``) | os10 |
| ``domain_list.name`` | list | Configures the domain-list name | os10 |
| ``domain_list.vrf`` | list | Configures VRF for each domain-list name | os10 |
| ``domain_list.state`` | string: absent,present\* | Deletes the domain-list if set to absent | os10 |


> **NOTE**: Asterisk (\*) denotes the default value if none is specified.

Connection variables
--------------------

Ansible Dell EMC network roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories or inventory, or in the playbook itself.

| Key         | Required | Choices    | Description                                         |
|-------------|----------|------------|-----------------------------------------------------|
| ``ansible_host`` | yes      |            | Specifies the hostname or address for connecting to the remote device over the specified transport |
| ``ansible_port`` | no       |            | Specifies the port used to build the connection to the remote device; if value is unspecified, the `ANSIBLE_REMOTE_PORT` option is used; it defaults to 22 |
| ``ansible_ssh_user`` | no       |            | Specifies the username that authenticates the CLI login for the connection to the remote device; if value is unspecified, the `ANSIBLE_REMOTE_USER` environment variable value is used  |
| ``ansible_ssh_pass`` | no       |            | Specifies the password that authenticates the connection to the remote device |
| ``ansible_become`` | no       | yes, no\*   | Instructs the module to enter privileged mode on the remote device before sending any commands; if value is unspecified, the `ANSIBLE_BECOME` environment variable value is used, and the device attempts to execute all commands in non-privileged mode |
| ``ansible_become_method`` | no       | enable, sudo\*   | Instructs the module to allow the become method to be specified for handling privilege escalation; if value is unspecified, the `ANSIBLE_BECOME_METHOD` environment variable value is used |
| ``ansible_become_pass`` | no       |            | Specifies the password to use if required to enter privileged mode on the remote device; if ``ansible_become`` is set to no this key is not applicable |
| ``ansible_network_os`` | yes      | os10, null\*  | Loads the correct terminal and cliconf plugins to communicate with the remote device |

> **NOTE**: Asterisk (\*) denotes the default value if none is specified.


Example playbook
----------------

This example uses the *os10_dns* role to completely set up the DNS server configuration. The example creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the `ansible_network_os` variable with corresponding Dell EMC OS10 name.

When `os10_cfg_generate` is set to true, generates the configuration commands as a .part file in *build_dir* path. By default it is set to false. It writes a simple playbook that only references the *os10_dns* role. By including the role, you automatically get access to all of the tasks to configure DNS.

**Sample hosts file**

    leaf1 ansible_host= <ip_address>

**Sample host_vars/leaf1**

    hostname: leaf1
    ansible_become: yes
    ansible_become_method: xxxxx
    ansible_become_pass: xxxxx
    ansible_ssh_user: xxxxx
    ansible_ssh_pass: xxxxx
    ansible_network_os: dellemc.os10.os10
    build_dir: ../temp/temp_os10
	os10_dns:
       domain_lookup: true
       name_server:
         - ip:
            - 3.1.1.1
            - 3.1.1.2
           vrf:
            - test
            - test1
         - ip:
            - 3.1.1.2
           vrf:
            - test1
           state: absent
         - ip:
            - 2.2.2.2
         - ip:
            - 3.3.2.2
           state: absent
       domain_list:
         - name:
            - dname7
            - dname8
           vrf:
            - test
            - test1
         - name:
           - dname7
           vrf:
            - test
            - test1
           state: absent
         - name:
            - dname3
            - dname4
         - name:
            - dname5
            - dname6
           state: absent

> **NOTE**: vrf should be present which can be configured using os10_vrf role

**Simple playbook to setup DNS — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_dns

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.
Prefix-list role
================

This role facilitates the configuration of a prefix-list. It supports the configuration of an IP prefix-list, and assigns the prefix-list to line terminals. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The prefix-list role requires an SSH connection for connectivity to a Dell EMC OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` value
- If `os10_cfg_generate` set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os10_prefix_list keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``type`` | string (required): ipv4,ipv6        | Configures an L3 (IPv4/IPv6) prefix-list | os10 |
| ``name`` | string (required)           | Configures the prefix-list name | os10 |
| ``description`` | string           | Configures the prefix-list description  | os10 |
| ``entries`` | list | Configures rules in the prefix-list (see ``seqlist.*``) | os10 |
| ``entries.number`` | int (required)       | Specifies the sequence number of the prefix-list rule          | os10 |
| ``entries.permit`` | boolean (required): true,false         | Specifies the rule to permit packets if set to true, and specifies to reject packets if set to false | os10 |
| ``entries.net_num`` | string (required)       | Specifies the network number                                         | os10 |
| ``entries.mask`` | string (required)        | Specifies the mask                                                      | os10 |
| ``entries.condition_list`` | list         | Configures conditions to filter packets (see ``condition_list.*``)|  os10 |
| ``condition_list.condition`` | list         | Specifies the condition to filter packets from the source address | os10 |
| ``condition_list.prelen`` | string (required)      | Specifies the allowed prefix length                                      | os10 |
| ``entries.state`` | string: absent,present\*   | Deletes the rule from the prefix-list if set to absent     | os10 |
| ``state`` | string: absent,present\*   | Deletes the prefix-list if set to absent     | os10 |

> **NOTE**: Asterisk (\*) denotes the default value if none is specified. 

Connection variables
--------------------

Ansible Dell EMC network roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories, or inventory or in the playbook itself.

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

This example uses the *os10_prefix_list* role to configure prefix-list for both IPv4 and IPv6. It creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the `ansible_network_os` variable with corresponding Dell EMC OS10 name. 

When `os10_cfg_generate` is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, the variable is set to false. It writes a simple playbook that only references the *os10_prefix_list* role. 

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
    os10_prefix_list:
       - name: testpl
         type: ipv4
         description: pl
         entries:
           - number: 19
             permit: true
             net_num: 20.0.0.0
             mask: 16
             condition_list:
               - condition: ge
                 prelen: 17
               - condition: le
                 prelen: 18
             state: present
         state: present

**Simple playbook to setup system — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_prefix_list

**Run**

    ansible-playbook -i hosts leaf.yaml
    
(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

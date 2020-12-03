Uplink role
===========

This role facilitates the configuration of uplink failure detection feature attributes. It specifically enables configuration of  association between upstream and downstream interfaces known as uplink-state group. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The Uplink role requires an SSH connection for connectivity to a Dell EMC SmartFabric OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os10_uplink keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``uplink_state_group`` | list | Configures the uplink state group (see ``uplink_state_group.*``) | os10 |
| ``uplink_state_group.id`` | integer | Configures the uplink state group instance | os10 |
| ``uplink_state_group.enable`` | boolean: True,False | Enables the uplink state group instance | os10 |
| ``uplink_state_group.defer_time`` | integer | Configures defer timer for the uplink state group | os10 |
| ``uplink_state_group.uplink_type`` | list | Configures the upstream and downstream attribute (see ``uplink_type.*``) | os10 |
| ``uplink_type.type`` | string: upstream,downstream | Configures the uplink type | os10 |
| ``uplink_type.intf`` | string | Configures the uplink interface | os10 |
| ``uplink_type.state`` | string: absent,present\* | Removes the uplink stream if set to absent | os10 |
| ``uplink_state_group.downstream`` | dictionary | Configures downstream information for the uplink state group (see ``downstream.*``) | os10 |
| ``downstream.disable_links`` | integer | Configures number of downstream links to be disabled. String 'all' can be used to disable all downstream links | os10 |
| ``downstream.auto_recover`` | boolean: True,False | Enables or disables auto recover for downstream interfaces | os10 |
| ``uplink_state_group.state`` | string: absent,present\* | Removes the uplink state group instance if set to absent | os10 |

> **NOTE**: Asterisk (\*) denotes the default value if none is specified. 

Connection variables
********************

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

This example uses the *os10_uplink role* to completely set the uplink sate group instance, and upstream, downstream interfaces. It creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the `ansible_network_os` variable with corresponding Dell EMC OS10 name. 

When `os10_cfg_generate` is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, the variable is set to false. The uplink role writes a simple playbook that only references the *os10_uplink* role. By including the role, you automatically get access to all of the tasks to configure uplink features. 

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
    build_dir: ../temp/os10
	  
    os10_uplink:
      uplink_state_group:
        - id: 1
          enable: True
          uplink_type:
            - type: "upstream"
              intf: "port-channel1"
              state: "present"
            - type: "downstream"
              intf: "ethernet1/1/2-1/1/5"
              state: "present"
          state: "present"
          downstream:
            disable_links: all
            auto_recover: false
          defer_time: 50
        - id: 2
          enable: True
          state: "present"

> **NOTE**: Interfaces should be created using the *os10_interface* role.
 
**Simple playbook to setup uplink — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_uplink

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

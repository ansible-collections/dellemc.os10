IPv6 RA uard role
===================

This role facilitates the configuration of IPv6 RA Guard attributes. It specifically enables configuration of IPv6 RA Guard feature enable/disable, IPv6 RA Guard policy definition and policy parameter configuration, and attachment of IPv6 RA Guard policy to an interface. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.  

The IPv6 RA Guard role requires an SSH connection for connectivity to a Dell EMC OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os10_raguard keys**


| Key                                  | Type                    | Description                                              |Support  |
|--------------------------------------|-------------------------|----------------------------------------------------------|---------|
| ``enable``                           | boolean                 | Enables IPv6 RA-Guard feature                             | os10    |
| ``policy``                           | list                    | Configures the IPv6 RA Guard policy (see ``policy.*``)   | os10    |
| ``policy.state``                     | string: absent/present\*| Deletes the policy if set to absent      | os10    |
| ``policy.name``                      | string (required)       | Configures the IPv6 RA Guard policy name                 | os10    |
| ``policy.device_role.value``         | string (required)       | Configures the device role for a policy                  | os10    |
| ``policy.device_role.state``         | string: absent,present\*| Deletes the device role if set to absent                 | os10    |
| ``policy.managed_config_flag.value`` | string                  | Configures the managed config flag param for a policy    | os10    |
| ``policy.managed_config_flag.state`` | string: absent,present\*| Deletes the managed config flag if set to absent         | os10    |
| ``policy.other_config_flag.value``   | string                  | Configures the other config flag param for a policy      | os10    |
| ``policy.other_config_flag.state``   | string: absent,present\*| Deletes the other config flag if set to absent           | os10    |
| ``policy.mtu.value``                 | integer                 | Configures the MTU param for a policy                    | os10    |
| ``policy.mtu.state``                 | string: absent,present\*| Deletes the MTU if set to absent                         | os10    |
| ``policy.reachable_time.value``      | integer                 | Configures the reachable time param for a policy         | os10    |
| ``policy.reachable_time.state``      | string: absent,present\*| Deletes the reachable time if set to absent              | os10    |
| ``policy.retrans_timer.value``       | integer                 | Configures the retransmit timer param for a policy       | os10    |
| ``policy.retrans_timer.state``       | string: absent,present\*| Deletes the retransmit timer if set to absent            | os10    |
| ``policy.router_lifetime.value``     | integer                 | Configures the router lifetime param for a policy        | os10    |
| ``policy.router_lifetime.state``     | string: absent,present\*| Deletes the router lifetime if set to absent             | os10    |
| ``policy.router_preference.value``   | string                  | Configures the router preference param for a policy      | os10    |
| ``policy.router_preference.state``   | string: absent,present\*| Deletes the router preference if set to absent           | os10    |
| ``policy.match``                     | list                    | Configures the prefix/ACL/MAC list param for a policy    | os10    |
| ``policy.match.type``                | string                  | Configures the prefix/ACL/MAC type for a policy          | os10    |
| ``policy.match.name``                | string                  | Configures the prefix/ACL/MAC name for a policy          | os10    |
| ``policy.match.state``               | string: absent,present\*| Deletes the prefix/ACL/MAC if set to absent              | os10    |
| ``intf``                             | dictionary              | Configures IPv6 RA Guard on the interface (see``intf.*``) | os10    |
| ``intf.<interface name>``            | dictionary              | Configures RA Guard on the interface (see``<interface name>.*``)| os10    |
| ``<interface name>.policy_name``     | String                  | Configures RA Guard policy name to be attached on an interface | os10    |
| ``<interface name>.vlan``            | String                  | Configures VLAN name to which policy to be attached on an interface| os10|
| ``<interface name>.state``           | String: absent,present\*| Deletes the policy if set to absent an interface         | os10|

> **NOTE**: Asterisk (\*) denotes the default value if none is specified.

Connection variables
--------------------

Ansible Dell EMC network roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories or inventory or in the playbook itself.

| Key         | Required | Choices    | Description                                           |
|-------------|----------|------------|-------------------------------------------------------|
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

This example uses the *os10_raguard* role to configure the IPv6 RA Guard feature enable/disable, IPv6 RA Guard Policy defination and policy parameter configuration, Attachment of IPv6 RA Guard policy to an interface. It creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the `ansible_network_os` variable with corresponding Dell EMC OS10 name. 

When `os10_cfg_generate` is set to true, it generates the configuration commands as a .part file in *build_dir* path. By default it is set to false. The example writes a simple playbook that only references the *os10_raguard* role. By including the role, you automatically get access to all of the tasks to configure IPv6 RA Guard attributes.

**Sample hosts file**
 
    leaf1 ansible_host= <ip_address> 

**Sample host_vars/leaf1**

    host: leaf1
    ansible_ssh_user: xxxxx
    ansible_ssh_pass: xxxxx
    ansible_network_os: dellemc.os10.os10
    build_dir: ../temp/os10
	  
    os10_raguard:
      enable: true
      policy:
        - policy_name: test
          device_role: 
            value: router
            state: present
          managed_config_flag: 
            value: "on"
            state: present
          mtu: 
            value: 1280
            state: present
          match:
            - type: prefix_list
              name: test_prefix
              state: present
          state: present
      intf:
        ethernet 1/1/2:
          policy_name: test
          vlan: 10
          state: present
 
**Simple playbook to setup IPv6 RA Guard — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_raguard

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

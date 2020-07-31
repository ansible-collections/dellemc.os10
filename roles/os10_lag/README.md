LAG role
========

This role facilitates the configuration of link aggregation group (LAG) attributes, and supports the creation and deletion of a LAG and its member ports. It also supports the configuration of an interface type as a static or dynamic LAG and minimum required link. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The LAG role requires an SSH connection for connectivity to a Dell EMC OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- Object drives the tasks in this role
- `os10_lag` (dictionary) contains the hostname (dictionary)
- Hostname is the value of the *hostname* variable that corresponds to the name of the OS device
- Any role variable with a corresponding state variable setting to absent negates the configuration of that variable
- Setting an empty value to any variable negates the corresponding configuration
- `os10_lag` (dictionary) holds a dictionary with the port-channel ID key in `Po <ID>` format (1 to 128)
- Variables and values are case-sensitive

**port-channel ID keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``type``      | string: static,dynamic      | Configures the interface either as a static or dynamic LAG           | os10 |
| ``min_links`` | integer                       | Configures the minimum number of links in the LAG that must be in *operup* status (1 to 32) | os10 |
| ``max_bundle_size`` | integer | Configures the maximum bundle size for the port channel  | os10 |
| ``lacp_system_priority`` | integer | Configures the LACP system-priority value | os10 |
| ``lacp_fallback_enable`` | boolean | Configures LACP fallback | os10 |
| ``channel_members``  | list  | Specifies the list of port members to be associated to the port-channel (see ``channel_members.*``) | os10 |
| ``channel_members.port`` | string  | Specifies valid interface names to be configured as port-channel members | os10 |
| ``channel_members.mode`` | string: active,passive,on | Configures mode of channel members | os10 |
| ``channel_members.port_priority`` | integer | Configures port priority on devices for channel members | os10 |
| ``channel_members.lacp_rate_fast`` | boolean | Configures the LACP rate as fast if set to true | os10 |
| ``state``  | string: absent,present\*           | Deletes the LAG corresponding to the port-channel ID if set to absent | os10 |

> **NOTE**: Asterisk (\*) denotes the default value if none is specified.

Connection variables
--------------------

Ansible Dell EMC network roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories or inventory, or in the playbook itself.

| Key         | Required | Choices    | Description                                         |
|-------------|----------|------------|-----------------------------------------------------|
| ``ansible_host`` | yes      |            | Specifies the hostname or address for connecting to the remote device over the specified transport |
| ``ansible_port`` | no       |            | Specifies the port used to build the connection to the remote device; if value is unspecified, the `ANSIBLE_REMOTE_PORT` option is used; it defaults to 22 |
| ``ansible_ssh_user`` | no       |            | Specifies the username that authenticates the CLI login for the connection to the remote device; if value is unspecified, the `ANSIBLE_REMOTE_USER` environment variable value is used  |
| ``ansible_ssh_pass`` | no       |            | Specifies the password that authenticates the connection to the remote device  |
| ``ansible_become`` | no       | yes, no\*   | Instructs the module to enter privileged mode on the remote device before sending any commands; if value is unspecified, the `ANSIBLE_BECOME` environment variable value is used, and the device attempts to execute all commands in non-privileged mode |
| ``ansible_become_method`` | no       | enable, sudo\*   | Instructs the module to allow the become method to be specified for handling privilege escalation; if value is unspecified, the `ANSIBLE_BECOME_METHOD` environment variable value is used |
| ``ansible_become_pass`` | no       |            | Specifies the password to use if required to enter privileged mode on the remote device; if ``ansible_become`` is set to no this key is not applicable |
| ``ansible_network_os`` | yes      | os10, null\*  | Loads the correct terminal and cliconf plugins to communicate with the remote device |

> **NOTE**: Asterisk (\*) denotes the default value if none is specified.


Example playbook
----------------

This example uses the *os10_lag* role to setup port channel ID and description, and configures hash algorithm and minimum links for the LAG. Channel members can be configured for the port-channel either in static or dynamic mode. You can also delete the LAG with the port-channel ID or delete the members associated to it. This example creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the `ansible_network_os` variable with corresponding Dell EMC OS10 name.

When `os10_cfg_generate` is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, the variable is set to false. It writes a simple playbook that only references the *os10_lag* role.

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

    os10_lag:
      Po 12:
         type: dynamic
         min_links: 2
         max_bundle_size: 2
         lacp_system_priority: 2
         channel_members:
           - port: ethernet 1/1/31
             mode: "active"
             port_priority: 3
             lacp_rate_fast: true
         state: present

**Simple playbook to setup system — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_lag

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

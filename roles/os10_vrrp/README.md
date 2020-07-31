VRRP role
=========

This role facilitates configuring virtual router redundancy protocol (VRRP) attributes. It supports the creation of VRRP groups for interfaces and setting the VRRP group attributes. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The VRRP role requires an SSH connection for connectivity to a Dell EMC OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- `os10_vrrp` (dictionary) holds a dictionary with the interface name key
- Interface name can correspond to any of the valid OS10 interface with a unique interface identifier name
- Physical interfaces names must be in *<interfacename> <tuple>* format (for example *fortyGigE 1/1*)
- Variables and values are case-sensitive

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``vrrp``    | dictionary  | Configures VRRP commands (see ``vrrp.*``) | os10 |
| ``version``    | dictionary  | Configures VRRP version | os10 |
| ``vrrp_active_active_mode``    | dictionary  | Configures VRRP active-active mode | os10 |
| ``delay_reload``     | integer      | Configures the minimum delay timer applied after boot (0 to 900) | os10 |
| ``vrrp_group``    | list  | Configures VRRP group commands (see ``vrrp_group.*``) | os10 |
| ``vrrp_group.type``  | string: ipv6,ipv4      | Specifies the type of the VRRP group | os10 |
| ``vrrp_group.group_id``    | integer (required)  | Configures the ID for the VRRP group (1 to 255) | os10 |
| ``vrrp_group.virtual_address``  | string          | Configures a virtual-address to the VRRP group (A.B.C.D format) | os10 |
| ``virtual_address.ip``  | string          | Configures a virtual ip address (A.B.C.D format) | os10 |
| ``virtual_address.state``  | string: present\*,absent          | Configures/unconfigures a virtual-address (A.B.C.D format) | os10 |
| ``vrrp_group.preempt``      | boolean: true\*,false          | Configures preempt mode on the VRRP group | os10 |
| ``vrrp_group.priority``      |integer          | Configures priority for the VRRP group (1 to 255; default 100)  | os10 |
| ``vrrp_group.adv_interval_centisecs``      | integer         | Configures the advertisement interval for the VRRP group in centiseconds (25 to 4075; default 100) and in multiple of 25; centisecs gets converted into seconds in version 2 | os10 |
| ``vrrp_group.track_interface``      | list       | Configures the track interface of the VRRP group (see ``track.*``) | os10 |
| ``track_interface.resource_id``      | integer       | Configures the object tracking resource ID of the VRRP group; mutually exclusive with *track.interface* | os10 |
| ``track_interface.interface``      | string       | Configures the track interface of the VRRP group (<interface name> <interface number> format) | os10 |
| ``track_interface.priority_cost``      | integer       | Configures the priority cost for track interface of the VRRP group (1 to 254; default 10) | os10 |
| ``track_interface.state``       | string: present\*,absent          | Deletes the specific track interface from the VRRP group if set to absent | os10 |
| ``vrrp_group.track_interface.state``       | string: present*,absent          | Deletes all track interfaces from the VRRP group if set to absent | os10 |
| ``vrrp_group.state``       | string: present\*,absent          | Deletes the VRRP group from the interface if set to absent | os10 |
                                                                                                 
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

This example uses the *os10_vrrp* role to configure VRRP commands at the interfaces. It creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the `ansible_network_os` variable with corresponding Dell EMC OS10 name. 

When `os10_cfg_generate` is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, the variable is set to false. It writes a simple playbook that only references the *os10_vrrp* role.

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
    os10_vrrp:
        vrrp:
          delay_reload: 2
          version: 3
        ethernet1/1/1:
          vrrp_group:
            - group_id: 2
              type: ipv6
              priority: 120
              preempt: false
              track_interface:
                - resource_id: 3
                  priority_cost: 25
                  state: present
              virtual_address:
                - ip: 2001:4828:5808:ffa3::9
                  state: present
                - ip: 3001:4828:5808:ffa3::9
                  state: present
                - ip: 4001:4828:5808:ffa3::9
                  state: absent
              adv_interval_centisecs: 200
              state: present
            - group_id: 4
              virtual_address:
                - ip: 4.1.1.1
                  state: present
                - ip: 4.1.1.2
                  state: present
                - ip: 4.1.1.3
                  state: absent
              priority: 120
              preempt: false
              track_interface:
                - resource_id: 3
                  priority_cost: 25
                  state: present
              adv_interval_centisecs: 200
              state: present
        vlan100:
          vrrp_active_active_mode: true

> **NOTE**: Interface VRRP cannot exist with L2 modes and can be configured using the *os10_interface* role.

**Simple playbook to setup system — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_vrrp
                
**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

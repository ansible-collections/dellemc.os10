VRF role
========

This role facilitates to configure the basics of virtual routing and forwarding (VRF) that helps in the partition of physical routers to multiple virtual routers. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The VRF role requires an SSH connection for connectivity to a Dell EMC SmartFabric OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the variable `ansible_network_os` that can take the `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os10_vrf keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``vrfdetails`` | list              | Configures the list of VRF instances (see ``instances.*``)  | os10 |
| ``vrfdetails.vrf_name``      | string         | Specifies the VRF instance name (default is management)  | os10 |
| ``vrfdetails.state``       | string    | Deletes the VRF instance name if set to absent | os10 |
| ``vrfdetails.ip_route_import``  | string    | Configures VRF IP subcommands | os10 |
| ``ip_route_import.community_value``  | string    | Configures the route community value | os10 |
| ``ip_route_import.route_map_value``  | string    | Configures the route-map value | os10 |
| ``ip_route_import.state``  | string    | Deletes the IP configuration if set to absent | os10 |
| ``vrfdetails.ip_route_export``  | string    | Configures VRF IP subcommands | os10 |
| ``ip_route_export.community_value``  | string    | Configures the route community value | os10 |
| ``ip_route_export.route_map_value``  | string    | Configures the route-map value | os10 |
| ``ip_route_export.state``  | string    | Deletes the IP config if set to absent | os10 |
| ``vrfdetails.ipv6_route_import``  | string    | Configures VRF IPv6 subcommands | os10 |
| ``ipv6_route_import.community_value``  | string    | Configures the route community value | os10 |
| ``ipv6_route_import.route_map_value``  | string    | Configures the route-map value | os10 |
| ``ipv6_route_import.state``  | string    | Deletes the IP config if set to absent | os10 |
| ``vrfdetails.ipv6_route_export``  | string    | Configures VRF IPv6 subcommands | os10 |
| ``ipv6_route_import.community_value``  | string    | Configures the route community value | os10 |
| ``ipv6_route_export.route_map_value``  | string    | Configures the route-map value | os10 |
| ``ipv6_route_import.state``  | string    | Deletes the IP config if set to absent | os10 |
| ``vrfdetails.map_ip_interface``  | list        | Specifies a list of valid interface names | os10 |
| ``map_ip_interface.intf_id``  | string    | Specifies a valid interface name | os10 |
| ``map_ip_interface.state``  | string    | Deletes VRF association in the interface if set to absent | os10 |
| ``upd_src_ip_loopback_id``  | string    |  Configures the source IP for any leaked route in VRF from the provided loopback ID, delete if empty string| os10 |

> **NOTE**: Asterisk (\*) denotes the default value if none is specified.

Connection variables
--------------------

Ansible Dell EMC network roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories, or inventory or in the playbook itself.

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

Dependencies
------------

The *os10_vrf* role is built on modules included in the core Ansible code. These modules were added in ansible version 2.2.0

Example playbook
----------------

This example uses the *os10_vrf* role to setup a VRF and associate it to an interface. It creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the `ansible_network_os` variable with corresponding Dell EMC OS10 name.

When `os10_cfg_generate` is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, the variable is set to false. It writes a  simple playbook that references the *os10_vrf* role. 
*upd_src_ip_loopback_id* has an dependency with association of the interface in a VRF, and the *os10_vrf* role needs to be invoked twice with different input dictionary one for the create and one for *upd_src_ip_loopback_id*.

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
    os10_vrf:
        vrfdetails:
          - vrf_name: "os10vrf" 
            state: "present"
            ip_route_import:
              community_value: "10:20"
              state: "present"
              route_map_value: "test4"
            ip_route_export:
              community_value: "30:40"
              state: "present"
              route_map_value: "test3"
            ipv6_route_import:
              community_value: "40:50"
              state: "absent"
              route_map_value: "test2"
            ipv6_route_export:
              community_value: "60:70"
              state: "absent"
              route_map_value: "test2"
            map_ip_interface:
             - intf_id : "loopback11"
               state   : "present"

    os_vrf_upd_src_loopback:
        vrfdetails:
          - vrf_name: "os10vrf"
            state: "present"
            upd_src_ip_loopback_id: 11

**Simple playbook to setup system — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_vrf

**Simple playbook with `upd_src_ip_loopback_id` — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_vrf
    - hosts: leaf1
      vars:
         os10_vrf: "{{ os_vrf_upd_src_loopback }}"
      roles:
         - dellemc.os10.os10_vrf

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

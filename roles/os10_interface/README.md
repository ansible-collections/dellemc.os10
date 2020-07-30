Interface role
==============

This role facilitates the configuration of interface attributes. It supports the configuration of admin state, description, MTU, IP address, IP helper, suppress_ra, and port mode. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The Interface role requires an SSH connection for connectivity to a Dell EMC OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable setting to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- `os10_interface` (dictionary) holds a dictionary with the interface name; interface name can correspond to any of the valid OS interfaces with the unique interface identifier name
- For physical interfaces, the interface name must be in *<interfacename> <tuple>* format; for logical interfaces, the interface must be in *<logical_interfacename> <id>* format; physical interface name can be *ethernet 1/1/32*
- For interface ranges, the interface name must be in *range <interface_type> <node/slot/port[:subport]-node/slot/port[:subport]>* format; *range ethernet 1/1/1-1/1/4*
- Logical interface names can be *vlan 1* or *port-channel 1*
- Variables and values are case-sensitive

> **NOTE**: Only define supported variables for the interface type, and do not define the *switchport* variable for a logical interface.

**interface name keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``desc``  | string         | Configures a single line interface description  | os10 |
| ``portmode`` | string | Configures port-mode according to the device type | os10  |
| ``switchport`` | boolean: true,false\*  | Configures an interface in L2 mode | os10 |
| ``admin``      | string: up,down\*              | Configures the administrative state for the interface; configuring the value as administratively "up" enables the interface; configuring the value as administratively "down" disables the interface | os10 |
| ``mtu``        | integer                       | Configures the MTU size for L2 and L3 interfaces (1280 to 65535) | os10 |
| ``fanout``     | string:dual, single; string:10g-4x, 40g-1x, 25g-4x, 100g-1x, 50g-2x (os10)   | Configures fanout to the appropriate value | os10 |
| ``suppress_ra`` | string; present,absent     | Configures IPv6 router advertisements if set to present | os10 |
| ``ip_type_dynamic`` | boolean: true,false           | Configures IP address DHCP if set to true (*ip_and_mask* is ignored if set to true) | os10 |
| ``ipv6_type_dynamic`` | boolean: true,false           | Configures an IPv6 address for DHCP if set to true (*ipv6_and_mask* is ignored if set to true) | os10 |
| ``ipv6_autoconfig`` | boolean: true,false           | Configures stateless configuration of IPv6 addresses if set to true (*ipv6_and_mask* is ignored if set to true) | os10 |
| ``vrf`` | string | Configures the specified VRF to be associated to the interface | os10 |
| ``min_ra`` | string | Configures RA minimum interval time period | os10 |
| ``max_ra`` | string | Configures RA maximum interval time period | os10 |
| ``ip_and_mask`` | string | Configures the specified IP address to the interface | os10 |
| ``ipv6_and_mask`` | string | Configures a specified IPv6 address to the interface | os10 |
| ``virtual_gateway_ip``     | string     | Configures an anycast gateway IP address for a VxLAN virtual network as well as VLAN interfaces| os10  |
| ``virtual_gateway_ipv6``     | string     | Configures an anycast gateway IPv6 address for VLAN interfaces| os10  |
| ``state_ipv6`` | string: absent,present\* | Deletes the IPV6 address if set to absent           | os10 | 
| ``ip_helper`` | list | Configures DHCP server address objects (see ``ip_helper.*``) | os10 |
| ``ip_helper.ip`` | string (required)         | Configures the IPv4 address of the DHCP server (A.B.C.D format)  | os10 |
| ``ip_helper.state`` | string: absent,present\* | Deletes the IP helper address if set to absent           | os10 |
| ``flowcontrol`` | dictionary | Configures the flowcontrol attribute (see ``flowcontrol.*``) | os10 |
| ``flowcontrol.mode`` | string:   receive,transmit  | Configures the flowcontrol mode   | os10 |
| ``flowcontrol.enable`` | string:   on,off  | Configures the flowcontrol mode on  | os10 |
| ``flowcontrol.state`` | string: absent,present\* | Deletes the flowcontrol if set to absent   | os10 |
| ``ipv6_bgp_unnum`` | dictionary | Configures the ipv6 bgp unnum attributes (see ``ipv6_bgp_unnum.*``) below | os10 |
| ``ipv6_bgp_unnum.state`` | string: absent,present\* | Disable auto discovery of BGP unnumbered peer if set to absent | os10 |
| ``ipv6_bgp_unnum.peergroup_type`` | string: ebgp,ibgp | Specify the type of template to inherit from | os10 |

> **NOTE**: Asterisk (*) denotes the default value if none is specified.

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

> **NOTE**: Asterisk (*) denotes the default value if none is specified.


Example playbook
----------------

This example uses the *os10_interface* role to set up description, MTU, admin status, port mode, and switchport details for an interface. The example creates a *hosts* file with the switch details and orresponding variables. The hosts file should define the `ansible_network_os` variable with corresponding Dell EMC OS10 name.

When `os10_cfg_generate` is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, this variable is set to false. The example writes a simple playbook that only references the *os10_interface* role.

**Sample hosts file**

    leaf3 ansible_host= <ip_address>
 
**Sample host_vars/leaf3**

    hostname: "leaf3"
    ansible_become: yes
    ansible_become_method: xxxxx
    ansible_become_pass: xxxxx
    ansible_ssh_user: xxxxx
    ansible_ssh_pass: xxxxx
    ansible_network_os: dellemc.os10.os10
    build_dir: ../temp/temp_os10

    os10_interface:
        ethernet 1/1/32:
                desc: "Connected to Core 2"
                mtu: 2500    
                portmode:
                admin: up
                switchport: False
                ip_and_mask: 
                ip_type_dynamic: True
                ipv6_type_dynamic: True
        ethernet 1/1/12:
                desc: "ipv6 auto config"
                switchport: False
                mtu: 2500
                admin: up
                ipv6_autoconfig: True
        ethernet 1/1/14:
                fanout: 10g-4x
        ethernet 1/1/13:
                desc: "set ipv6 address"
                switchport: False
                admin: up
                ipv6_and_mask: 2001:4898:5809:faa2::10/126
                state_ipv6: present
        ethernet 1/1/1:
                desc: "Connected to Leaf1"
                portmode: "trunk"
                switchport: True
                suppress_ra: present
                admin: up
        ethernet 1/1/3:
                desc: site2-spine2
                ip_and_mask: 10.9.0.4/31
                mtu: 9216
                switchport: False
                admin: up
                flowcontrol:
                  mode: "receive"
                  enable: "on"
                  state: "present"

        vlan 100:
                ip_and_mask: 
                ipv6_and_mask: 2001:4898:5808:ffaf::1/64
                state_ipv6: present
                ip_helper:
                   - ip: 10.0.0.33
                     state: present
                admin: up
        range ethernet 1/1/1-1/1/32:
                mtu: 2500
        port-channel 10:
                admin: up
                switchport: False
                suppress_ra:
                ipv6_bgp_unnum:
                    state: present
                    peergroup_type: ebgp
        vlan 10:
                ip_and_mask: "10.1.1.1/24"
                virtual_gateway_ip: "10.1.1.254"
                virtual_gateway_ipv6: "10:1:1::254"
                admin: up

**Simple playbook to setup system — leaf.yaml**

    - hosts: leaf3
      roles:
         - dellemc.os10.os10_interface
 
**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

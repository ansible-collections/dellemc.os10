VXLAN role
========

This role facilitates the configuration of  virtual extensible LAN (VXLAN) attributes. It supports the configuration of Virtual Networks, Ethernet Virtual Private Network (evpn) and Network Virtualization Edge (nve). This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The VXLAN role requires an SSH connection for connectivity to a Dell EMC PowerSwitch platform running Dell EMC SmartFabric OS10. You can use any of the built-in OS connection variables.

Role variables
--------------
 
- Role is abstracted using the *ansible_network_os* variable that can take dellemc_networking.os10.os10 value
- If variable *os10_cfg_generate* is set to true, it generates the role configuration commands in a file
- Any role variable with a corresponding state variable setting to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os10_vxlan keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``anycast_gateway_mac`` | string | Configures an anycast gateway IP address for a VXLAN virtual network | os10 |
| ``loopback`` | dictionary | Configures the loopback interface (see ``loopback.*``) | os10 |
| ``loopback.loopback_id`` | integer | Configures the loopback interface number  0 to 16383 | os10 |
| ``loopback.description`` | string | Configures the interface description | os10 |
| ``loopback.ip_address`` | string | Configure the ip address | os10 |
| ``loopback.state`` | string: absent,present\* | Removes loopback interface if set to absent | os10 |
| ``nve`` | dictionary | Configures Network Virtualization Edge (see ``nve.*``) | os10 |
| ``nve.source_interface`` | integer | Configures source loopback interface | os10 |
| ``nve.controller`` | dictionary | Configures controller (OS10 supports only one controller connection at a time)(see ``controller.*``)  | os10 |
| ``controller.name`` | string: NSX, ovsdb | Configures the nve controller | os10 |
| ``controller.max_backoff`` | integer | Configures max_backoff value (Setting an empty value negates the corresponding configuration) | os10 |
| ``controller.control_cfg`` | list | Configures the controller ip and port (see ``control_cfg.*``) | os10 |
| ``control_cfg.ip_addr`` | string | Configures the controller ip | os10 |
| ``control_cfg.port`` | integer | Configures the controller port | os10 |
| ``control_cfg.state`` | string: absent,present\* | Removes the controller ip and port configuration if set to absent   | os10 |
| ``controller.state`` | string: absent,present\* | Removes the controller if set to absent | os10 |
| ``nve.state`` | string: absent,present\* | Removes the Network Virtualization Edge if set to absent | os10 |
| ``evpn`` | dictionary | Enable the evpn in control plane (see ``evpn.*``)  | os10 |
| ``evpn.autoevi`` | boolean: True, False | Configures auto-evi (No further manual configuration is allowed in auto-EVI mode) | os10 |
| ``evpn.rmac`` | string | Configures router mac address | os10 |
| ``evpn.evi`` | list | Configures EVPN instance (see ``evi.*``)| os10 |
| ``evpn.dis_rt_asn`` | boolean | Enable/Disable AS number usage in route target | os10 |
| ``evpn.vrf`` | dictionary | Enable VRF for EVPN| os10 |
| ``vrf.name`` | string | Configures VRF name | os10 |
| ``vrf.vni`` | integer | Configures vni for the VRF | os10 |
| ``vrf.rd`` | string | Configures RD for the VRF | os10 |
| ``vrf.route_target`` | dictionary | Enable Route Target for the VRF | os10 |
| ``route_target.type`` | string (manual, auto) | Configure Route Target type | os10 |
| ``route_target.asn_value`` | string | Configure AS number | os10 |
| ``route_target.state`` | string (present,absent) | Configure/Unconfigure Route Target | os10 |
| ``route_target.route_target_type`` | string | Configure Route Target type | os10 |
| ``vrf.adv_ipv4`` | dictionary | Enable IPv4 advertisement VRF | os10 |
| ``adv_ipv4.type`` | string | Configure IPv4 advertisement type | os10 |
| ``adv_ipv4.rmap_name`` | string | Configure route map for advertisement | os10 |
| ``adv_ipv4.unconfig`` | boolean | Configure/unconfigure route map for advertisement | os10 |
| ``evi.id`` | integer | Configures the EVPN instance id (The range is from 1 to 65535) | os10 |
| ``evi.rd`` | string |  Configure the Route  Distinguisher | os10 |
| ``evi.vni`` | dictionary | Configures vni value (see ``vni.*``) | os10 |
| ``vni.id`` | integer | Configures vni value (You must configure the same VNI value that you configure for the VXLAN virtual network) | os10 |
| ``vni.state`` | string: absent,present\* | Removes the vni if set to absent | os10 |
| ``evi.route_target`` | list | Configures route target (see ``route_target.*``) | os10 |
| ``route_target.type`` | string: manual,auto  | Configures the route target (auto mode auto-configures an import and export value for EVPN routes) | os10 |
| ``route_target.asn_value`` | string | Configures the route target asn value | os10 |
| ``route_target.route_target_type`` | string: import,export,both  | Configures the route target type | os10 |
| ``route_target.state`` | string: absent,present\* | Removes the route target if set to absent  | os10 |
| ``evi.state`` | string: absent,present\*     | Removes EVPN instance id if set to absent  | os10 |
| ``evpn.state`` | string: absent,present\* | Removes the EVPN configuration if set to absent | os10 |
| ``virtual_network`` | dictionary | Configures the virtual network attributes (see ``virtual_network.*``) | os10 |
| ``virtual_network.untagged_vlan`` | integer  | Configures the  reserved untagged VLAN ID, from 1 to 4093  | os10 |
| ``virtual_network.virtual_net`` | list  | Configures the virtual network attributes for VXLAN tunneling (see ``virtual_net.*``) | os10 |
| ``virtual_net.id`` | integer | Configures a virtual network ( virtual-network ID, from 1 to 65535) | os10 |
| ``virtual_net.description`` | string | Configures the Description for Virtual Network | os10 |
| ``virtual_net.vlt_vlan_id`` | integer | Configures  VLTi VLAN ID | os10 |
| ``virtual_net.member_interface`` | list | Configures the trunk member interface attributes to the virtual network (see ``member_interface.*``) | os10 |
| ``member_interface.ifname`` | string | Configures interface name to provision the virtual network member interface |  os10 |
| ``member_interface.type`` | string: tagged,untagged | Configures the type to provision the virtual network member interface |  os10 |
| ``member_interface.vlanid`` | integer | Configures the VLAN ID to provision the virtual network member interface |  os10 |
| ``member_interface.state`` | string: absent,present\* | Removes the virtual network member interface if set to absent  |  os10 |
| ``virtual_net.vxlan_vni`` | dictionary | Configures the  VXLAN attributes to  virtual network (see ``vxlan_vni.*``) | os10 |
| ``vxlan_vni.id`` | integer | Configures the VXLAN ID to a virtual network   | os10 |
| ``vxlan_vni.remote_endpoint`` | list | Configures the IP address of a remote tunnel endpoint in a VXLAN network (see ``remote_endpoint.*``) | os10 |
| ``remote_endpoint.ip`` | string | Configures the IP address of a remote tunnel endpoint (1.1.1.1)  | os10 |
| ``remote_endpoint.state`` | string: absent,present\* | Removes the remote tunnel endpoint in a VXLAN network if set to absent | os10 |
| ``vxlan_vni.state`` | string: absent,present\* | Removes the VXLAN ID if set to absent   | os10 |
| ``virtual_net.state`` | string: absent,present\* | Removes a virtual network if set to absent | os10 |
| ``vlan_association`` | list | Configures the  vlan association with virtual network  (see ``vlan_association.*``) | os10 |
| ``vlan_association.vlan_id`` | integer | Specifies the VLAN ID    | os10 |
| ``vlan_association.virtual_net`` | integer | Specifies the virtual netwrok id which is to be associated with vlan  | os10 |


> **NOTE**: Asterisk (\*) denotes the default value if none is specified.

Connection variables
--------------------

Ansible Dell EMC Networking roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories or inventory, or in the playbook itself.

| Key         | Required | Choices    | Description                                         |
|-------------|----------|------------|-----------------------------------------------------|
| ``ansible_host`` | yes      |            | Specifies the hostname or address for connecting to the remote device over the specified transport |
| ``ansible_port`` | no       |            | Specifies the port used to build the connection to the remote device; if value is unspecified, the ANSIBLE_REMOTE_PORT option is used; it defaults to 22 |
| ``ansible_ssh_user`` | no       |            | Specifies the username that authenticates the CLI login for the connection to the remote device; if value is unspecified, the ANSIBLE_REMOTE_USER environment variable value is used  |
| ``ansible_ssh_pass`` | no       |            | Specifies the password that authenticates the connection to the remote device |
| ``ansible_become`` | no       | yes, no\*   | Instructs the module to enter privileged mode on the remote device before sending any commands; if value is unspecified, the ANSIBLE_BECOME environment variable value is used, and the device attempts to execute all commands in non-privileged mode |
| ``ansible_become_method`` | no       | enable, sudo\*   | Instructs the module to allow the become method to be specified for handling privilege escalation; if value is unspecified, the ANSIBLE_BECOME_METHOD environment variable value is used |
| ``ansible_become_pass`` | no       |            | Specifies the password to use if required to enter privileged mode on the remote device; if ``ansible_become`` is set to no this key is not applicable |
| ``ansible_network_os`` | yes      | os10, null\*  | Loads the correct terminal and cliconf plugins to communicate with the remote device |
 
> **NOTE**: Asterisk (\*) denotes the default value if none is specified.

Dependencies
------------

The *os10_vxlan* role is built on modules included in the core Ansible code. These modules were added in Ansible version 2.2.0.

Example playbook
----------------

This example uses the *os10_vxlan* role to configure the VXLAN network, source ip address on VXLAN tunnel endpoint and virtual networks. It creates a *hosts* file with the switch details, a *host_vars* file with connection variables and the corresponding role variables.

When *os10_cfg_generate* is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, the variable is set to false. This example writes a simple playbook that only references the *os10_vxlan* role. The sample host_vars given below is for OS10. 

**Sample hosts file**
    
    leaf1 ansible_host= <ip_address> 

**Sample host_vars/leaf1**

    hostname: leaf1
    ansible_become: yes
    ansible_become_method: xxxxx
    ansible_become_pass: xxxxx
    ansible_ssh_user: xxxxx
    ansible_ssh_pass: xxxxx
    ansible_network_os: dellemc_networking.os10.os10
    build_dir: ../temp/os10
	  
    os10_vxlan:
        anycast_gateway_mac: "00:22:33:44:55:66"
        loopback:
          loopback_id: 10
          description: "HARDWARE_VXLAN"
          ip_address: "10.8.0.1/32"
          state: "present"
        nve:
          source_interface: 10
          controller:
            name: "ovsdb"
            max_backoff: 2000
            control_cfg:
              - ip_addr: "1.2.3.4"
                port: 30
                state: "present"
            state: "present"
          state: "present"
        evpn:
          autoevi: False
          evi:
            - id: 111
              rd: "auto"
              vni:
                id: 111
                state: "present"
              route_target:
                - type: "manual"
                  asn_value: "111:111"
                  route_target_type: "both"
                  state: "present"
                - type: "manual"
                  asn_value: "11:11"
                  route_target_type: "export"
                  state: "present"
              state: "present"
            - id: 222 
              rd: "2.2.2.2:222"
              vni:
                id: 222
                state: "present"
              route_target:
                - type: "auto"
                  asn_value:
                  route_target_type: 
                  state: "present"
              state: "present"
          vrf:
            - name: "test"
              vni: 1000
              adv_ipv4:
                - type: "connected"
                  state: "present"
                - type: "bgp"
                  state: "present"
              route_target:
                - type: "manual"
                  asn_value: "65530:65534"
                  route_target_type: "both"
                  state: "present"
          rmac: 00:11:11:11:11:11
          dis_rt_asn: "true"
          state: "present"
        virtual_network:
          untagged_vlan: 1001
          virtual_net:
            - id: 111
              description: "NSX_Cluster_VNI_111"
              vlt_vlan_id: 11
              member_interface:
                - ifname: "ethernet 1/1/15"
                  type: "tagged"
                  vlanid: 15
                  state: "present"
                - ifname: "port-channel 12"
                  type: "tagged"
                  vlanid: 11
                  state: "present"
              vxlan_vni:
                id: 111
                remote_endpoint:
                  - ip: "1.1.1.1"
                    state: "present"
                  - ip: "11.11.11.11"
                    state: "present"
                  - ip: "111.111.111.111"
                    state: "present"
                state: "present"
              state: "present" 
            - id: 222
              description: "NSX_Cluster_VNI_222"
              vlt_vlan_id: 22
              member_interface:
                - ifname: "ethernet 1/1/16"
                  type: "tagged"
                  vlanid: 16
                  state: "present"
              vxlan_vni:
                id: 222
                remote_endpoint:
                  - ip: "2.2.2.2"
                    state: "present"
                  - ip: "22.22.22.22"
                    state: "present"
                state: "present"
              state: "present" 
        vlan_association:
          - vlain_id: 111
            virtual_net: 111

> **NOTE**: Member interfaces should be in switchport trunk mode which can be configured using os10_interface role
 
**Simple playbook to configure VXLAN - leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc_networking.os10.os10_vxlan

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2020 Dell Inc. or its subsidiaries. All Rights Reserved.

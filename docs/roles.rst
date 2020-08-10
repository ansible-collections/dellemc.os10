##############################################################
Ansible Network Collection Roles for Dell EMC SmartFabric OS10 
##############################################################

The roles facilitate provisioning of devices running Dell EMC SmartFabric OS10. This document describes each of the roles.

AAA role
--------

The `os10_aaa <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_aaa/README.md>`_ role facilitates the configuration of Authentication Authorization and Accounting (AAA), and supports the configuration of TACACS and RADIUS server and AAA.


ACL role
--------

The `os10_acl <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_acl/README.md>`_ role facilitates the configuration of Access Control lists. It supports the configuration of different types of ACLs (standard and extended) for both IPv4 and IPv6, and assigns the access-class to line terminals.


BFD role
--------

The `os10_bfd <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_bfd/README.md>`_ role facilitates the configuration of BFD global attributes. It specifically enables configuration of BFD interval , min_rx, multiplier, and role.


BGP role
--------

The `os10_bgp <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_bgp/README.md>`_ role facilitates the configuration of border gateway protocol (BGP) attributes, and supports router ID, networks, neighbors, and maximum path configurations.


Copy configuration role
-----------------------

The `os10_copy_config <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_copy_config/README.md>`_ role pushes the backup running configuration into a device. This role merges the configuration in the template file with the running configuration of the Dell EMC Networking OS10 device.


DNS role
--------

The `os10_dns <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_dns/README.md>`_ role facilitates the configuration of domain name service (DNS).


ECMP role
---------

The `os10_ecmp <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_ecmp/README.md>`_ role facilitates the configuration of equal cost multi-path (ECMP). It supports the configuration of ECMP for IPv4.


Fabric-summary role
-------------------

The `os10_fabric_summary <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_fabric_summary/README.md>`_ role facilitates to get show system information of all the switches in the fabric.


Flow-monitor role
-----------------

The `os10_flow_monitor <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_flow_monitor/README.md>`_ role facilitates the configuration of ACL flow-based monitoring attributes. In Flow-based mirroring, the ingress traffic, matching the specified policies are mirrored to a destination port. Port-based mirroring maintains a database that contains all monitoring sessions, including port monitor sessions.


Image-upgrade role
------------------

The `os10_image_upgrade <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_image_upgrade/README.md>`_ role facilitates installation of OS10 software images.


Interface role
--------------

The `os10_interface <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_interface/README.md>`_ role facilitates the configuration of interface attributes. It supports the configuration of administrative state, description, MTU, IP address, IP helper, and port mode. 


LAG role
--------

The `os10_lag <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_lag/README.md>`_ role facilitates the configuration of link aggregation group (LAG) attributes. This role supports the creation and deletion of a LAG and its member ports, and supports the configuration of type (static/dynamic), hash scheme, and minimum required link.


LLDP role
---------

The `os10_lldp <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_lldp/README.md>`_ role facilitates the configuration of link layer discovery protocol (LLDP) attributes at global and interface level. This role supports the configuration of hello, mode, multiplier, advertise tlvs, management interface, fcoe, iscsi at global and interface levels.


Logging role
------------

The `os10_logging <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_logging/README.md>`_ role facilitates the configuration of global logging attributes, and supports the configuration of logging servers. 


Network-Validation role
-----------------------

The `os10_network_validation <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_network_validation/README.md>`_ role facilitates to verify the Networks. It validates networking features of wiring connection, BGP neighbors, MTU between neighbors and VLT pair.


NTP role
--------

The `os10_ntp <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_ntp/README.md>`_ role facilitates the configuration of network time protocol attributes.


Prefix-list role
----------------

The `os10_prefix_list <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_prefix_list/README.md>`_ role facilitates the configuration of a prefix-list, supports the configuration of IP prefix-list, and assigns the prefix-list to line terminals.


QoS role
--------

The `os10_qos <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_qos/README.md>`_ role facilitates the configuration of quality of service attributes including policy-map and class-map.


RA Guard role
-------------

The `os10_raguard <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_raguard/README.md>`_ role facilitates the configuration of IPv6 RA Guard attributes.


Route-map role
--------------

The `os10_route_map <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_route_map/README.md>`_ role facilitates the configuration of route-map attributes.


SNMP role
---------

The `os10_snmp <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_snmp/README.md>`_ role facilitates the configuration of global snmp attributes. It supports the configuration of SNMP server attributes like users, group, community, location, traps, and so on.


System role
-----------

The `os10_system <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_system/README.md>`_ role facilitates the configuration of global system attributes. This role specifically enables configuration of hostname and hashing algorithm for OS10.


TEMPLATE role
-------------

The `os10_template <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_template/README.md>`_ role facilitates the TEXTFSM parsing engine. TextFSM is a template based state machine . It takes the raw string input from the CLI of network devices OS10, run them through a TEXTFSM template and return structured text in the form of a Python dictionary.


UPLINK role
-----------

The `os10_uplink <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_uplink/README.md>`_ role facilitates the configuration of uplink attributes, and is abstracted for OS10. It specifically enables configuration of association between upstream and downstream interfaces known as uplink-state group.


Users role
----------

The `os10_users <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_users/README.md>`_ role facilitates the configuration of global system user attributes. This role supports the configuration of CLI users.


VLAN role
---------

The `os10_vlan <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_vlan/README.md>`_ role facilitates configuring virtual LAN (VLAN) attributes. This role supports the creation and deletion of a VLAN and its member ports.


VLT role
--------

The `os10_vlt <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_vlt/README.md>`_ role facilitates the configuration of the basics of virtual link trunking (VLT) to provide a loop-free topology.


VRF role
--------

The `os10_vrf <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_vrf/README.md>`_ role facilitates the configuration of basic virtual routing and forwarding (VRF) that helps in the partition of physical routers to multiple virtual routers.


VRRP role
---------

The `os10_vrrp <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_vrrp/README.md>`_ role facilitates configuration of virtual router redundancy protocol (VRRP) attributes. This role supports the creation of VRRP groups for interfaces, and setting the VRRP group attributes.


VXLAN role
----------

The `os10_vxlan <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_vxlan/README.md>`_ role facilitates the configuration of virtual extensible LAN (VXLAN) attributes. It supports the configuration of virtual networks, Ethernet virtual private network (EVPN), and network virtualization edge (NVE).


xSTP role
---------

The `os10_xstp <https://github.com/ansible-collections/dellemc.os10/blob/master/roles/os10_xstp/README.md>`_ role facilitates the configuration of xSTP attributes. This role supports multiple version of spanning-tree protocol (STP), rapid spanning-tree (RSTP) protocol, multiple spanning-tree (MST), and per-VLAN spanning-tree (PVST). This role supports the configuration of bridge priority, enabling and disabling spanning-tree, creating and deleting instances, and mapping virtual LAN (VLAN) to instances.


\(c) 2020 Dell Inc. or its subsidiaries. All Rights Reserved.

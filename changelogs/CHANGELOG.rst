======================================================================
Ansible Network Collection for Dell EMC SmartFabric OS10 Release Notes
======================================================================

.. contents:: Topics

v1.0.1
======

Release Summary
---------------

Added changelog.

v1.0.0
======

New Plugins
-----------

Cliconf
~~~~~~~

- os10 - Use OS10 cliconf to run commands on Dell EMC PowerSwitch devices.

New Modules
-----------

- os10_command - Run commands on devices running Dell EMC SmartFabric OS1O.
- os10_config - Manage configuration on devices running OS10.
- os10_facts - Collect facts from devices running OS10.

New Roles
---------

- os10_aaa - Facilitates the configuration of Authentication Authorization and Accounting (AAA), TACACS and RADIUS server.
- os10_acl - Facilitates the configuration of Access Control lists.
- os10_bfd - Facilitates the configuration of BFD global attributes.
- os10_bgp - Facilitates the configuration of border gateway protocol (BGP) attributes.
- os10_copy_config - This role pushes the backup running configuration into a OS10 device.
- os10_dns - Facilitates the configuration of domain name service (DNS).
- os10_ecmp - Facilitates the configuration of equal cost multi-path (ECMP) for IPv4.
- os10_fabric_summary - Facilitates to get show system information of all the OS10 switches in the fabric.
- os10_flow_monitor - Facilitates the configuration of ACL flow-based monitoring attributes.
- os10_image_upgrade - Facilitates installation of OS10 software images.
- os10_interface - Facilitates the configuration of interface attributes.
- os10_lag - Facilitates the configuration of link aggregation group (LAG) attributes.
- os10_lldp - Facilitates the configuration of link layer discovery protocol (LLDP) attributes at global and interface level.
- os10_logging - Facilitates the configuration of global logging attributes and logging servers.
- os10_network_validation - Facilitates validation of wiring connection, BGP neighbors, MTU between neighbors and VLT pair.
- os10_ntp - Facilitates the configuration of network time protocol (NTP) attributes.
- os10_prefix_list - Facilitates the configuration of IP prefix-list.
- os10_qos - Facilitates the configuration of quality of service attributes including policy-map and class-map.
- os10_raguard - Facilitates the configuration of IPv6 RA Guard attributes.
- os10_route_map - Facilitates the configuration of route-map attributes.
- os10_snmp - Facilitates the configuration of  global SNMP attributes.
- os10_system - Facilitates the configuration of hostname and hashing algorithm.
- os10_template - The role takes the raw string input from the CLI of OS10 device, and returns a structured text in the form of a Python dictionary.
- os10_uplink - Facilitates the configuration of uplink attributes like uplink-state group.
- os10_users - Facilitates the configuration of global system user attributes.
- os10_vlan - Facilitates the configuration of virtual LAN (VLAN) attributes.
- os10_vlt - Facilitates the configuration of virtual link trunking (VLT).
- os10_vrf - Facilitates the configuration of virtual routing and forwarding (VRF).
- os10_vrrp - Facilitates the configuration of virtual router redundancy protocol (VRRP) attributes.
- os10_vxlan - Facilitates the configuration of virtual extensible LAN (VXLAN) attributes.
- os10_xstp - Facilitates the configuration of xSTP attributes.

\(c) 2020 Dell Inc. or its subsidiaries. All Rights Reserved.

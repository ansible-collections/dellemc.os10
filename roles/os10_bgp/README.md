BGP role
========

This role facilitates the configuration of border gateway protocol (BGP) attributes. It supports the configuration of router ID, networks, neighbors, and maximum paths. This role is abstracted for Dell EMC PowerSwitch platforms running SmartFabric OS10.

The BGP role requires an SSH connection for connectivity to a Dell EMC SmartFabric OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, it generates the role configuration commands in a file
- Any role variable with a corresponding state variable setting to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os10_bgp keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``asn`` | string (required) | Configures the autonomous system (AS) number of the local BGP instance | os10 |
| ``router_id`` | string | Configures the IP address of the local BGP router instance | os10 |
| ``graceful_restart`` | boolean | Configures graceful restart capability | os10 |
| ``maxpath_ibgp`` | integer | Configures the maximum number of paths to forward packets through iBGP (1 to 64; default 1) | os10 |
| ``maxpath_ebgp`` | integer | Configures the maximum number of paths to forward packets through eBGP (1 to 64; default 1) | os10 |
| ``log_neighbor_changes`` | boolean | Configures log neighbors up/down | os10 |
| ``fast_ext_fallover`` | boolean | Configures a reset session if a link to a directly connected external peer goes down | os10 |
| ``always_compare_med`` | boolean | Configures comparing MED from different neighbors | os10 |
| ``default_loc_pref`` | integer | Configures the default local preference value | os10 |
| ``as_notation`` | string | Configures AS number notation format | os10 |
| ``enforce_first_as`` | boolean | Configures the first AS for eBGP routes | os10 |
| ``non_deterministic_med`` | boolean | Configures nondeterministic path selection algorithm | os10 |
| ``outbound_optimization`` | boolean | Configures outbound optimization for iBGP peer-group members | os10 |
| ``confederation`` | dictionary | Configures AS confederation parameters (see ``confederation.*``) | os10 |
| ``confederation.identifier`` | integer | Configures the routing domain confederation AS | os10 |
| ``confederation.peers`` | string | Configures the peer AS in BGP confederation | os10 |
| ``confederation.peers_state`` | string: absent,present\* | Deletes the peer AS in BGP confederation if set to absent   | os10 |
| ``route_reflector`` | dictionary | Configures route reflection parameters (see ``route_reflector.*``) | os10 |
| ``route_reflector.client_to_client`` | boolean | Configures client-to-client route reflection | os10 |
| ``route_reflector.cluster_id`` | string | Configures the route reflector cluster-id | os10 |
| ``address_family_ipv4`` | dictionary | Configures IPv4 address family parameters (see ``address_family_ipv4.*``) | os10 |
| ``address_family_ipv4.aggregate_addr`` | list | Configures IPv4 BGP aggregate entries (see ``aggregate_addr.*``) | os10 |
| ``aggregate_addr.ip_and_mask`` | string | Configures the IPv4 BGP aggregate address | os10 |
| ``aggregate_addr.adv_map`` | string | Configures the advertise map for IPv4 BGP aggregate address | os10 |
| ``aggregate_addr.attr_map`` | string | Configures the attribute map for IPv4 BGP aggregate address | os10 |
| ``aggregate_addr.suppress_map`` | string | Configures the suppress map for IPv4 BGP aggregate address | os10 |
| ``aggregate_addr.summary_only`` | boolean | Sets address to summary only if true | os10 |
| ``aggregate_addr.state`` | string: absent,present\* | Deletes an IPv4 BGP aggregate entry if set to absent   | os10 |
| ``address_family_ipv4.dampening`` | dictionary | Configures route-flap dampening (see ``dampening.*``) | os10 |
| ``dampening.value`` | dictionary | Configures dampening values (<half-life time> <start value to reuse> <start value to suppress> <max duration> format; default 15 750 2000 60) | os10 |
| ``dampening.route_map`` | string | Configures the route-map to specify criteria for dampening | os10 |
| ``dampening.state`` | string: absent,present\* | Deletes dampening if set to absent   | os10 |
| ``address_family_ipv4.ibgp_redist_internal`` | dictionary | Configures internal BGP reditribution (see ``ibgp_redist_internal.*``) | os10 |
| ``ibgp_redist_internal.state`` | boolean | Configures the internal BGP redistribution for an IPv4 address family | os10 |
| ``address_family_ipv4.default_metric`` | integer | Configures the metric of redistributed routes for IPv4 address family | os10 |
| ``address_family_ipv4.distance_bgp`` | dictionary | Configures BGP distances (see ``distance_bgp.*``) | os10 |
| ``distance_bgp.value`` | dictionary | Configures the BGP administrative distance for IPv4 address family (<routes external to AS> <routes internal to AS> <local routes> format; distance bgp 2 3 4) | os10 |
| ``distance_bgp.state`` | string: absent,present\* | Deletes distance BGP if set to absent   | os10 |
| ``address_family_ipv6`` | dictionary | Configures IPv6 address family parameters (see ``address_family_ipv6.*``) | os10 |
| ``address_family_ipv6.aggregate_addr`` | list | Configures IPv6 BGP aggregate entries (see ``aggregate_addr.*``) | os10 |
| ``aggregate_addr.ip_and_mask`` | string | Configures the IPv6 BGP aggregate address | os10 |
| ``aggregate_addr.adv_map`` | string | Configures the advertise map for IPv6 BGP aggregate address | os10 |
| ``aggregate_addr.attr_map`` | string | Configures the attribute map for IPv6 BGP aggregate address | os10 |
| ``aggregate_addr.suppress_map`` | string | Configures the suppress map for IPv6 BGP aggregate address | os10 |
| ``aggregate_addr.summary_only`` | boolean | Sets address to summary-only if true | os10 |
| ``aggregate_addr.state`` | string: absent,present\* | Deletes an IPv6 BGP aggregate entry if set to absent   | os10 |
| ``address_family_ipv6.dampening`` | dictionary | Configures route-flap dampening (see ``dampening.*``) | os10 |
| ``dampening.value`` | dictionary | Configures dampening values (<half-life time> <start value to reuse> <start value to suppress> <max duration> format; default 15 750 2000 60) | os10 |
| ``dampening.route_map`` | string | Configures the route-map to specify criteria for dampening | os10 |
| ``dampening.state`` | string: absent,present\* | Deletes dampening if set to absent   | os10 |
| ``address_family_ipv6.ibgp_redist_internal`` | dictionary | Configures iBGP reditribution (see ``ibgp_redist_internal.*``) | os10 |
| ``ibgp_redist_internal.state`` | boolean | Configures the iBGP redistribution for an IPv6 address family | os10 |
| ``address_family_ipv6.default_metric`` | integer | Configures the metric of redistributed routes for IPv6 address family | os10 |
| ``address_family_ipv6.distance_bgp`` | dictionary | Configures BGP distances (see ``distance_bgp.*``) | os10 |
| ``distance_bgp.value`` | dictionary | Configures the BGP administrative distance for an IPv6 address family (<routes external to AS> <routes internal to AS> <local routes> format; distance bgp 2 3 4) | os10 |
| ``distance_bgp.state`` | string: absent,present\* | Deletes distance BGP if set to absent   | os10 |
| ``best_path`` | list | Configures the default best-path selection (see ``best_path.*``) | os10 |
| ``best_path.as_path`` | string (required): ignore,multipath-relax     | Configures the AS path used for the best-path computation   | os10 |
| ``best_path.as_path_state`` | string: absent,present\*     | Deletes the AS path configuration if set to absent  | os10 |
| ``best_path.ignore_router_id`` | boolean: true,false | Ignores the router identifier in best-path computation if set to true | os10 |
| ``best_path.med`` | list | Configures the MED attribute (see ``med.*``) | os10 |
| ``med.attribute`` | string (required): confed,missing-as-best     | Configures the MED attribute used for the best-path computation   | os10 |
| ``med.state`` | string: absent,present\* | Deletes the MED attribute if set to absent | os10 |
| ``ipv4_network`` | list | Configures an IPv4 BGP networks (see ``ipv4_network.*``) | os10 |
| ``ipv4_network.address`` | string (required)         | Configures the IPv4 address of the BGP network (A.B.C.D/E format)   | os10 |
| ``ipv4_network.state`` | string: absent,present\* | Deletes an IPv4 BGP network if set to absent | os10 |
| ``ipv6_network`` | list | Configures an IPv6 BGP network (see ``ipv6_network.*``) | os10 |
| ``ipv6_network.address`` | string (required)         | Configures the IPv6 address of the BGP network (2001:4898:5808:ffa2::1/126 format)  | os10 |
| ``ipv6_network.state`` | string: absent,present\* | Deletes an IPv6 BGP network if set to absent | os10 |
| ``neighbor`` | list | Configures IPv4 BGP neighbors (see ``neighbor.*``) | os10 |
| ``neighbor.ip`` | string (required)         | Configures the IPv4 address of the BGP neighbor (10.1.1.1)  | os10 |
| ``neighbor.interface`` | string      | Configures the BGP neighbor interface details | os10  |
| ``neighbor.name`` | string (required)         | Configures the BGP peer-group with this name; supported only when the neighbor is a peer group; mutually exclusive with *neighbor.ip* | os10 |
| ``neighbor.type`` | string (required): ipv4,ipv6,peergroup       | Specifies the BGP neighbor type   | os10 |
| ``neighbor.auto_peer`` |string:  unnumbered-auto | Enables auto discovery of neighbors | os10 |
| ``neighbor.password`` | string      | Configures the BGP neighbor password  | os10  |
| ``neighbor.peergroup_type`` | string (ibgp, ebgp)   | Configures the BGP neighbor peer-group type| os10  |
| ``neighbor.ebgp_peergroup`` | string | Configures the peer-group to all auto-discovered external neighbors | os10 |
| ``neighbor.ebgp_peergroup_state`` | string: present,absent | Removes the peer-group from all auto-discovered external neighbors | os10 |
| ``neighbor.ibgp_peergroup`` | string | Configures the peer-group to all auto-discovered internal neighbors | os10 |
| ``neighbor.ibgp_peergroup_state`` | string: present,absent | Removes the peer-group from all auto-discovered internal neighbors | os10 |
| ``neighbor.route_reflector_client`` | boolean      | Configures router reflector client on the BGP neighbor | os10  |
| ``neighbor.local_as`` | integer     | Configures the local AS for the BGP peer | os10  |
| ``neighbor.weight`` | integer     | Configures the default weight for routes from the neighbor interface | os10  |
| ``neighbor.send_community`` | list | Configures the send community attribute to the BGP neighbor (see ``send_community.*``) | os10 |
| ``send_community.type`` | string (required)         | Configures the send community attribute to the BGP neighbor | os10 |
| ``send_community.state`` | string: absent,present\* | Deletes the send community attribute of the BGP neighbor if set to absent | os10 |
| ``neighbor.address_family`` | list | Configures address family commands on the BGP neighbor (see ``address_family.*``)| os10 |
| ``address_family.type`` | string (required): ipv4,ipv6,l2vpn         | Configures IPv4/IPv6/EVPN address family command mode on the BGP neighbor  | os10 |
| ``address_family.activate`` | boolean   | Configures activation/deactivation of IPv4/IPv6 address family command mode on the BGP neighbor  | os10 |
| ``address_family.sender_loop_detect`` | boolean   | Enables/disables the sender-side loop detection process for a BGP neighbor of IPv4/IPv6/l2vpn address family  | os10 |
| ``address_family.allow_as_in`` | integer  | Configures the local AS number in the as-path | os10 |
| ``address_family.next_hop_self`` | boolean   | Configures disabling the next-hop calculation for the neighbor | os10 |
| ``address_family.soft_reconf`` | boolean   | Configures per neighbor soft reconfiguration | os10 |
| ``address_family.add_path`` | string  | Configures send or receive multiple paths (value can be 'both <no of paths>', 'send <no of paths>', 'receive')| os10 |
| ``address_family.route_map`` | list   | Configures the route-map on the BGP neighbor (see ``route_map.*``) | os10 |
| ``route_map.name`` | string  | Configures the name of the route-map for the BGP neighbor   | os10 |
| ``route_map.filter`` | string  | Configures the filter for routing updates   | os10 |
| ``route_map.state`` | string, choices: absent,present\* | Deletes the route-map of the BGP neighbor if set to absent | os10 |
| ``address_family.max_prefix`` | dictionary | Configures maximum-prefix parameters (see ``max_prefix.\*``) | os10 |
| ``max_prefix.count`` | integer | Configures maximum number of prefix accepted from the peer | os10 |
| ``max_prefix.state`` | string: absent,present | Deletes maximum prefix configured for the peer | os10 |
| ``max_prefix.threshold`` | integer | Configures threshold percentage at which warning log is thrown | os10 |
| ``max_prefix.warning``| boolean | Configures a warning without dropping the session when maximum limit exceeds if set to true | os10|
| ``address_family.default_originate`` | dictionary | Configures default-originate parameters (see ``default_originate.\*``) | os10 |
| ``default_originate.route_map`` | string  | Configures the name of the route-map to specify criteria to originate default   | os10 |
| ``default_originate.state`` | string, choices: absent,present\* | Deletes the default-originate if set to absent | os10 |
| ``address_family.distribute_list`` | list | Configures the distribute list to filter networks from routing updates (see ``distribute_list.*``) | os10 |
| ``distribute_list.in`` | string       | Configures the name of the prefix-list to filter incoming packets  | os10 |
| ``distribute_list.in_state`` | string: absent,present\* | Deletes the filter at incoming packets if set to absent           | os10 |
| ``distribute_list.out`` | string       | Configures the name of the prefix-list to filter outgoing packets   | os10 |
| ``distribute_list.out_state`` | string: absent,present\* | Deletes the filter at outgoing packets if set to absent          | os10 |
| ``address_family.state`` | string: absent,present\* | Deletes the address family command mode of the BGP neighbor if set to absent | os10 |
| ``neighbor.remote_asn`` | string (required)         | Configures the remote AS number of the BGP neighbor  | os10 |
| ``neighbor.remote_asn_state`` | string: absent,present\* | Deletes the remote AS number from the peer group if set to absent; supported only when *neighbor.type* is "peergroup" | os10 |
| ``neighbor.timer`` | string          | Configures neighbor timers; 5 10, where 5 is the keepalive interval and 10 is the holdtime | os10 |
| ``neighbor.peergroup`` | string          | Configures neighbor to BGP peer-group (configured peer-group name) | os10 |
| ``neighbor.peergroup_state`` | string: absent,present\* | Deletes the IPv4 BGP neighbor from the peer-group if set to absent | os10 |
| ``neighbor.distribute_list`` | list | Configures the distribute list to filter networks from routing updates (see ``distribute_list.*``) | os10 |
| ``distribute_list.in`` | string       | Configures the name of the prefix-list to filter incoming packets  | os10 |
| ``distribute_list.in_state`` | string: absent,present\* | Deletes the filter at incoming packets if set to absent           | os10 |
| ``distribute_list.out`` | string       | Configures the name of the prefix-list to filter outgoing packets   | os10 |
| ``distribute_list.out_state`` | string: absent,present\* | Deletes the filter at outgoing packets if set to absent          | os10 |
| ``neighbor.admin`` | string: up,down       | Configures the administrative state of the neighbor  | os10 |
| ``neighbor.adv_interval`` | integer       | Configures the advertisement interval of the neighbor  | os10 |
| ``neighbor.adv_start`` | integer       | Set the advertisement start of the neighbor  | os10 |
| ``neighbor.adv_start_state`` | string: absent,present\* | Configures or unconfigures the advertisement start of a neighbor  | os10 |
| ``neighbor.conn_retry_timer`` | integer    | Configures the peer connection retry timer  |  os10 |
| ``neighbor.remove_pri_as`` | string: absent,present       | Configures the remove private AS number from outbound updates  |  os10 |
| ``neighbor.fall_over`` | string: absent,present       | Configures the session fall on peer-route loss  |  os10 |
| ``neighbor.sender_loop_detect`` | boolean: true,false         | Enables or disables the sender-side loop detect for neighbors | os10 |
| ``neighbor.src_loopback`` | integer         | Configures the source loopback interface for routing packets | os10  |
| ``neighbor.ebgp_multihop`` | integer | Configures the maximum-hop count value allowed in eBGP neighbors that are not directly connected (default 255) | os10 |
| ``neighbor.listen`` | list | Configures listen commands on the BGP template (see ``listen.*``)| os10 |
| ``listen.subnet`` | string (required)         | Configures the passive BGP neighbor IPv4/IPv6 to this subnet | os10 |
| ``listen.subnet_state`` | string: absent,present\* | Deletes the subnet range set for dynamic IPv4/IPv6  BGP neighbor if set to absent            | os10 |
| ``listen.limit`` | integer    | Configures maximum dynamic peers count (key is required together with ``neighbor.subnet``) | os10 |
| ``neighbor.bfd`` | boolean | Enables BFD for neighbor | os10 |
| ``neighbor.description`` | string | Configures neighbor description | os10 |
| ``neighbor.state`` | string: absent,present\* | Deletes the IPv4 BGP neighbor if set to absent | os10 |
| ``redistribute`` | list | Configures the redistribute list to get information from other routing protocols (see ``redistribute.*``) | os10 |
| ``redistribute.route_type`` | string (required): static,connected,imported_bgp,l2vpn,ospf        | Configures the name of the routing protocol to redistribute | os10 |
| ``redistribute.route_map_name`` | string        | Configures the route-map to redistribute | os10 |
| ``redistribute.imported_bgp_vrf_name`` | string        | Configures the redistribute imported BGP VRF name | os10 |
| ``redistribute.ospf_id`` | string        | Configures the redistribute OSPF | os10 |
| ``redistribute.address_type`` | string (required): ipv4,ipv6                  | Configures the address type of IPv4 or IPv6 routes | os10 |
| ``redistribute.state`` | string: absent,present\* | Deletes the redistribution information if set to absent | os10 |
| ``bfd_all_neighbors`` | dictionary | Enables BFD for all BGP neighbors | os10 |
| ``bfd_all_neighbors.interval`` | integer: 100 to 1000 | Configures time interval for sending control packets to BFD peers in ms| os10 |
| ``bfd_all_neighbors.min_rx`` | integer: 100 to 1000 | Configures maximum waiting time for receiving control packets from BFD peers in ms| os10 |
| ``bfd_all_neighbors.multiplier`` | integer: 3 to 50 | Configures maximum number of consecutive packets that are not received from BFD peers before session state changes to Down| os10 |
| ``bfd_all_neighbors.role``| string: active, passive | Configures BFD role | os10 |
| ``bfd_all_neighbors.state`` |string: absent,present\*    | Deletes BFD for all neighbors if set to absent | os10 |
| ``vrfs`` | list | Enables VRF under BGP | os10 |
| ``vrf.name`` | string (Required)| Configures VRF name | os10 |
| ``vrf.router_id`` | string | Configures the IP address of the local BGP router instance in VRF | os10 |
| ``vrf.graceful_restart`` | boolean | Configures graceful restart capability in VRF | os10 |
| ``vrf.maxpath_ibgp`` | integer | Configures the maximum number of paths to forward packets through iBGP (1 to 64; default 1) in VRF | os10 |
| ``vrf.maxpath_ebgp`` | integer | Configures the maximum number of paths to forward packets through eBGP (1 to 64; default 1) in VRF | os10 |
| ``vrf.log_neighbor_changes`` | boolean | Configures log neighbors up/down in VRF | os10 |
| ``vrf.fast_ext_fallover`` | boolean | Configures a reset session if a link to a directly connected external peer goes down in VRF | os10 |
| ``vrf.always_compare_med`` | boolean | Configures comparing MED from different neighbors in VRF | os10 |
| ``vrf.default_loc_pref`` | integer | Configures the default local preference value in VRF | os10 |
| ``vrf.as_notation`` | string | Changes the AS number notation format in VRF | os10 |
| ``vrf.enforce_first_as`` | boolean | Configures the first AS for eBGP routes in VRF | os10 |
| ``vrf.non_deterministic_med`` | boolean | Configures nondeterministic path selection algorithm in VRF | os10 |
| ``vrf.outbound_optimization`` | boolean | Configures outbound optimization for iBGP peer-group members in VRF | os10 |
| ``vrf.route_reflector`` | dictionary | Configures route reflection parameters (see ``route_reflector.*``) in VRF | os10 |
| ``vrf.route_reflector.client_to_client`` | boolean | Configures client-to-client route reflection in VRF | os10 |
| ``vrf.route_reflector.cluster_id`` | string | Configures the route-reflector cluster-id in VRF | os10 |
| ``vrf.address_family_ipv4`` | dictionary | Configures IPv4 address family parameters in VRF (see ``address_family_ipv4.*``) in VRF | os10 |
| ``address_family_ipv4.aggregate_addr`` | list | Configures IPv4 BGP aggregate entries (see ``aggregate_addr.*``) in VRF | os10 |
| ``aggregate_addr.ip_and_mask`` | string | Configures the IPv4 BGP aggregate address in VRF | os10 |
| ``aggregate_addr.adv_map`` | string | Configures the advertise map for IPv4 BGP aggregate address | os10 |
| ``aggregate_addr.attr_map`` | string | Configures the attribute map for IPv4 BGP aggregate address | os10 |
| ``aggregate_addr.suppress_map`` | string | Configures the suppress map for IPv4 BGP aggregate address | os10 |
| ``aggregate_addr.summary_only`` | boolean | Sets address to summary-only if true in VRF | os10 |
| ``aggregate_addr.state`` | string: absent,present\* | Deletes an IPv4 BGP aggregate entry if set to absent in VRF  | os10 |
| ``address_family_ipv4.dampening`` | dictionary | Configures route-flap dampening (see ``dampening.*``) | os10 |
| ``dampening.value`` | dictionary | Configures dampening values (<half-life time> <start value to reuse> <start value to suppress> <max duration> format; default 15 750 2000 60) | os10 |
| ``dampening.route_map`` | string | Configures the route-map to specify criteria for dampening | os10 |
| ``dampening.state`` | string: absent,present\* | Deletes dampening if set to absent   | os10 |
| ``address_family_ipv4.ibgp_redist_internal`` | dictionary | Configures iBGP reditribution (see ``ibgp_redist_internal.*``) | os10 |
| ``ibgp_redist_internal.state`` | boolean | Configures the iBGP redistribution for a IPV4 address family | os10 |
| ``address_family_ipv4.default_metric`` | integer | Configures the metric of redistributed routes for IPV4 address family | os10 |
| ``address_family_ipv4.distance_bgp`` | dictionary | Configures BGP distances (see ``distance_bgp.*``) | os10 |
| ``distance_bgp.value`` | dictionary | Configures the BGP administrative distance for IPV4 address family (<routes external to AS> <routes internal to AS> <local routes> format; distance bgp 2 3 4) | os10 |
| ``distance_bgp.state`` | string: absent,present\* | Deletes distance BGP if set to absent   | os10 |
| ``vrf.address_family_ipv6`` | dictionary | Configures IPv6 address family parameters in VRF (see ``address_family_ipv6.*``) | os10 |
| ``address_family_ipv6.aggregate_addr`` | list | Configures IPv6 BGP aggregate entries (see ``aggregate_addr.*``) | os10 |
| ``aggregate_addr.ip_and_mask`` | string | Configures the IPv6 BGP aggregate address | os10 |
| ``aggregate_addr.adv_map`` | string | Configures the advertise map for IPv6 BGP aggregate address | os10 |
| ``aggregate_addr.attr_map`` | string | Configures the attribute map for IPv6 BGP aggregate address | os10 |
| ``aggregate_addr.suppress_map`` | string | Configures the suppress map for IPv6 BGP aggregate address | os10 |
| ``aggregate_addr.summary_only`` | boolean | Sets address to summary-only if true | os10 |
| ``aggregate_addr.state`` | string: absent,present\* | Deletes an IPv6 BGP aggregate entry if set to absent   | os10 |
| ``address_family_ipv6.dampening`` | dictionary | Configures route-flap dampening (see ``dampening.*``) | os10 |
| ``dampening.value`` | dictionary | Configures dampening values (<half-life time> <start value to reuse> <start value to suppress> <max duration> format; default 15 750 2000 60) | os10 |
| ``dampening.route_map`` | string | Configures the route-map to specify criteria for dampening | os10 |
| ``dampening.state`` | string: absent,present\* | Deletes dampening if set to absent   | os10 |
| ``address_family_ipv6.ibgp_redist_internal`` | dictionary | Configures iBGP reditribution (see ``ibgp_redist_internal.*``) | os10 |
| ``ibgp_redist_internal.state`` | boolean | Configures the iBGP redistribution for a IPv6 address family | os10 |
| ``address_family_ipv6.default_metric`` | integer | Configures the metric of redistributed routes for IPv6 address family | os10 |
| ``address_family_ipv6.distance_bgp`` | dictionary | Configures BGP distances (see ``distance_bgp.*``) | os10 |
| ``distance_bgp.value`` | dictionary | Configures the BGP administrative distance for IPv6 address family (<routes external to AS> <routes internal to AS> <local routes> format; distance bgp 2 3 4) | os10 |
| ``distance_bgp.state`` | string: absent,present\* | Deletes distance BGP if set to absent   | os10 |
| ``vrf.best_path`` | list | Configures the default best-path selection in VRF (see ``best_path.*``) | os10 |
| ``best_path.as_path`` | string (required): ignore,multipath-relax     | Configures the AS path used for the best-path computation   | os10 |
| ``best_path.as_path_state`` | string: absent,present\*     | Deletes the AS path configuration if set to absent  | os10 |
| ``best_path.ignore_router_id`` | boolean: true,false | Ignores the router identifier in best-path computation if set to true | os10 |
| ``best_path.med`` | list | Configures the MED attribute (see ``med.*``) | os10 |
| ``med.attribute`` | string (required): confed,missing-as-best     | Configures the MED attribute used for the best-path computation   | os10 |
| ``med.state`` | string: absent,present\* | Deletes the MED attribute if set to absent | os10 |
| ``vrf.ipv4_network`` | list | Configures an IPv4 BGP networks (see ``ipv4_network.*``) | os10 |
| ``ipv4_network.address`` | string (required)         | Configures the IPv4 address of the BGP network (A.B.C.D/E format)   | os10 |
| ``ipv4_network.state`` | string: absent,present\* | Deletes an IPv4 BGP network if set to absent | os10 |
| ``vrf.ipv6_network`` | list | Configures an IPv6 BGP network (see ``ipv6_network.*``) | os10 |
| ``ipv6_network.address`` | string (required)         | Configures the IPv6 address of the BGP network (2001:4898:5808:ffa2::1/126 format)  | os10 |
| ``ipv6_network.state`` | string: absent,present\* | Deletes an IPv6 BGP network if set to absent | os10 |
| ``vrf.neighbor`` | list | Configures IPv4 BGP neighbors in VRF (see ``neighbor.*``) | os10 |
| ``neighbor.ip`` | string (required)         | Configures the IPv4 address of the BGP neighbor (10.1.1.1)  | os10 |
| ``neighbor.interface`` | string      | Configures the BGP neighbor interface details | os10  |
| ``neighbor.name`` | string (required)         | Configures the BGP peer-group with this name; supported only when the neighbor is a peer group; mutually exclusive with *neighbor.ip* | os10 |
| ``neighbor.type`` | string (required): ipv4,ipv6,peergroup       | Specifies the BGP neighbor type   | os10 |
| ``neighbor.auto_peer`` |string:  unnumbered-auto | Enable auto-discovery of neighbors | os10 |
| ``neighbor.password`` | string      | Configures the BGP neighbor password  | os10  |
| ``neighbor.peergroup_type`` | string (ibgp, ebgp)   | Configures the BGP neighbor peer-group type| os10  |
| ``neighbor.ebgp_peergroup`` | string | Configures the peer-group to all auto-discovered external neighbors | os10 |
| ``neighbor.ebgp_peergroup_state`` | string: present,absent | Removes the peer-group from all auto-discovered external neighbors | os10 |
| ``neighbor.ibgp_peergroup`` | string | Configures the peer-group to all auto-discovered internal neighbors | os10 |
| ``neighbor.ibgp_peergroup_state`` | string: present,absent | Removes the peer-group from all auto-discovered internal neighbors | os10 |
| ``neighbor.route_reflector_client`` | boolean      | Configures router reflector client on the BGP neighbor | os10  |
| ``neighbor.local_as`` | integer     | Configures the local AS for the BGP peer | os10  |
| ``neighbor.weight`` | integer     | Configures the default weight for routes from the neighbor interface | os10  |
| ``neighbor.send_community`` | list | Configures the send community attribute to the BGP neighbor (see ``send_community.*``) | os10 |
| ``send_community.type`` | string (required)         | Configures the send community attribute to the BGP neighbor | os10 |
| ``send_community.state`` | string: absent,present\* | Deletes the send community attribute of the BGP neighbor if set to absent | os10 |
| ``neighbor.address_family`` | list | Configures address family commands on the BGP neighbor (see ``address_family.*``)| os10 |
| ``address_family.type`` | string (required): ipv4,ipv6,l2vpn         | Configures IPv4/IPv6 EVPN address family command mode on the BGP neighbor  | os10 |
| ``address_family.activate`` | boolean   | Configures activation or deactivation of IPv4/IPv6 address family command mode on the BGP neighbor  | os10 |
| ``address_family.sender_loop_detect`` | boolean   | Enables or disables the sender-side loop detection process for a BGP neighbor of IPv4/IPv6 l2vpn address family  | os10 |
| ``address_family.allow_as_in`` | integer  | Configures the local AS number in the as-path | os10 |
| ``address_family.next_hop_self`` | boolean   | Configures disabling the next-hop calculation for the neighbor | os10 |
| ``address_family.soft_reconf`` | boolean   | Configures per neighbor soft reconfiguration | os10 |
| ``address_family.add_path`` | string  | Configures send or receive multiple paths (value can be 'both <no of paths>', 'send <no of paths>', 'receive')| os10 |
| ``address_family.route_map`` | list   | Configures the route-map on the BGP neighbor (see ``route_map.*``) | os10 |
| ``route_map.name`` | string  | Configures the name of the route-map for the BGP neighbor   | os10 |
| ``route_map.filter`` | string  | Configures the filter for routing updates   | os10 |
| ``route_map.state`` | string, choices: absent,present* | Deletes the route-map of the BGP neighbor if set to absent | os10 |
| ``address_family.max_prefix`` | dictionary | Configures maximum-prefix parameters (see ``max_prefix.*``) | os10 |
| ``max_prefix.count`` | integer | Configures maximum number of prefix accepted from the peer | os10 |
| ``max_prefix.state`` | string: absent,present | Deletes maximum prefix configured for the peer | os10 |
| ``max_prefix.threshold`` | integer | Configures threshold percentage at which warning log is thrown | os10 |
| ``max_prefix.warning``| boolean | Configures a warning without dropping session when maximum limit exceeds if set to true | os10|
| ``address_family.default_originate`` | dictionary | Configures default-originate parameters (see ``default_originate.\*``) | os10 |
| ``default_originate.route_map`` | string  | Configures the name of the route-map to specify criteria to originate default   | os10 |
| ``default_originate.state`` | string, choices: absent,present\* | Deletes the default-originate if set to absent | os10 |
| ``address_family.distribute_list`` | list | Configures the distribute list to filter networks from routing updates (see ``distribute_list.*``) | os10 |
| ``distribute_list.in`` | string       | Configures the name of the prefix-list to filter incoming packets  | os10 |
| ``distribute_list.in_state`` | string: absent,present\* | Deletes the filter at incoming packets if set to absent           | os10 |
| ``distribute_list.out`` | string       | Configures the name of the prefix-list to filter outgoing packets   | os10 |
| ``distribute_list.out_state`` | string: absent,present\* | Deletes the filter at outgoing packets if set to absent          | os10 |
| ``address_family.state`` | string: absent,present\* | Deletes the address family command mode of the BGP neighbor if set to absent | os10 |
| ``neighbor.remote_asn`` | string (required)         | Configures the remote AS number of the BGP neighbor  | os10 |
| ``neighbor.remote_asn_state`` | string: absent,present\* | Deletes the remote AS number from the peer-group if set to absent; supported only when *neighbor.type* is "peergroup" | os10 |
| ``neighbor.timer`` | string          | Configures neighbor timers; 5 10, where 5 is the keepalive interval and 10 is the holdtime | os10 |
| ``neighbor.peergroup`` | string          | Configures neighbor to BGP peer-group (configured peer-group name) | os10 |
| ``neighbor.peergroup_state`` | string: absent,present\* | Deletes the IPv4 BGP neighbor from the peer-group if set to absent | os10 |
| ``neighbor.distribute_list`` | list | Configures the distribute list to filter networks from routing updates (see ``distribute_list.*``) | os10 |
| ``distribute_list.in`` | string       | Configures the name of the prefix-list to filter incoming packets  | os10 |
| ``distribute_list.in_state`` | string: absent,present\* | Deletes the filter at incoming packets if set to absent           | os10 |
| ``distribute_list.out`` | string       | Configures the name of the prefix-list to filter outgoing packets   | os10 |
| ``distribute_list.out_state`` | string: absent,present\* | Deletes the filter at outgoing packets if set to absent          | os10 |
| ``neighbor.admin`` | string: up,down       | Configures the administrative state of the neighbor  | os10 |
| ``neighbor.adv_interval`` | integer       | Configures the advertisement interval of the neighbor  | os10 |
| ``neighbor.adv_start`` | integer       | Set the advertisement start of the neighbor  | os10 |
| ``neighbor.adv_start_state`` | string: absent,present\* | Configures or unconfigures the advertisement start of the neighbor  | os10 |
| ``neighbor.conn_retry_timer`` | integer    | Configures the peer connection retry timer  |  os10 |
| ``neighbor.remove_pri_as`` | string: absent,present       | Removes private AS number from outbound updates  |  os10 |
| ``neighbor.fall_over`` | string: absent,present       | Configures the session fall on peer-route loss  |  os10 |
| ``neighbor.sender_loop_detect`` | boolean: true,false         | Enables or disables the sender-side loop detect for neighbors | os10 |
| ``neighbor.src_loopback`` | integer         | Configures the source loopback interface for routing packets | os10  |
| ``neighbor.ebgp_multihop`` | integer | Configures the maximum-hop count value allowed in eBGP neighbors that are not directly connected (default 255) | os10 |
| ``neighbor.listen`` | list | Configures listen commands on the BGP template (see ``listen.*``)| os10 |
| ``listen.subnet`` | string (required)         | Configures the passive BGP neighbor IPv4/IPv6 to this subnet | os10 |
| ``listen.subnet_state`` | string: absent,present\* | Deletes the subnet range set for dynamic IPv4/IPv6 BGP neighbor if set to absent            | os10 |
| ``listen.limit`` | integer    | Configures maximum dynamic peers count (key is required together with ``neighbor.subnet``) | os10 |
| ``neighbor.bfd`` | boolean | Enables BFD for neighbor | os10 |
| ``neighbor.description`` | string | Configures neighbor description | os10 |
| ``neighbor.state`` | string: absent,present\* | Deletes the IPv4 BGP neighbor if set to absent | os10 |
| ``vrf.redistribute`` | list | Configures the redistribute list to get information from other routing protocols in VRF (see ``redistribute.*``) | os10 |
| ``redistribute.route_type`` | string (required): static,connected,imported_bgp        | Configures the name of the routing protocol to redistribute | os10 |
| ``redistribute.route_map_name`` | string        | Configures the route-map to redistribute | os10 |
| ``redistribute.imported_bgp_vrf_name`` | string        | Configures the redistribute imported BGP VRF name | os10 |
| ``redistribute.ospf_id`` | string        | Configures the redistribute ospf | os10 |
| ``redistribute.address_type`` | string (required): ipv4,ipv6                  | Configures the address type of IPv4 or IPv6 routes | os10 |
| ``redistribute.state`` | string: absent,present\* | Deletes the redistribution information if set to absent | os10 |
| ``vrf.bfd_all_neighbors`` | dictionary | Enables BFD for all BGP neighbors in VRF ((see ``bfd_all_neighbors.*``))| os10 |
| ``bfd_all_neighbors.interval`` | integer: 100 to 1000 | Configures time interval for sending control packets to BFD peers in ms| os10 |
| ``bfd_all_neighbors.min_rx`` | integer: 100 to 1000 | Configures maximum waiting time for receiving control packets from BFD peers in ms| os10 |
| ``bfd_all_neighbors.multiplier`` | integer: 3 to 50 | Configures maximum number of consecutive packets that are not received from BFD peers before session state changes to Down| os10 |
| ``bfd_all_neighbors.role``| string: active, passive | Configures BFD role | os10 |
| ``bfd_all_neighbors.state`` |string: absent,present\*    | Deletes BFD for all neighbors if set to absent | os10 |
| ``vrf.state`` |  string: absent,present\*    | Deletes the VRF instance under router BGP if set to absent      | os10 |
| ``state`` |  string: absent,present\*    | Deletes the local router BGP instance if set to absent      | os10 |

> **NOTE**: Asterisk (\*) denotes the default value if none is specified.

Connection variables
--------------------

Ansible Dell EMC network roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories or inventory, or in the playbook itself.

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

This example uses the *os10_bgp* role to configure the BGP network and neighbors. It creates a *hosts* file with the switch details, a *host_vars* file with connection variables and the corresponding role variables. The hosts file should define the `ansible_network_os` variable with the corresponding Dell EMC OS10 name.

When `os10_cfg_generate` is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, the variable is set to false. This example writes a simple playbook that only references the *os10_bgp* role. 

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

    os10_bgp:
        asn: 12
        router_id: 90.1.1.4
        maxpath_ibgp: 2
        maxpath_ebgp: 2
        graceful_restart: true
        log_neighbor_changes: true
        fast_ext_fallover: false
        always_compare_med: true
        default_loc_pref: 1000
        as_notation: asdot
        enforce_first_as: false
        non_deterministic_med: true
        outbound_optimization: true
        confederation:
          identifier: 25
          peers: 23 24
          peers_state: present
        route_reflector:
          client_to_client: false
          cluster_id: 4294967295
        address_family_ipv4:
          aggregate_address:
             - ip_and_mask: 1.1.1.1/16
               state: present
               summary_only: true
          dampening:
            value: 15 750 2000 60
            route_map: qq
            state: present
          ibgp_redist_internal:
            state: present
          default_metric: 10
          distance_bgp:
            value: 3 4 6
            state: present
        address_family_ipv6:
          aggregate_address:
             - ip_and_mask: 2001:4898:5808:ffa0::/126
               state: present
               summary_only: true
          ibgp_redist_internal:
            state: present
        best_path:
           as_path: ignore
           as_path_state: present
           ignore_router_id: true
           med:
            - attribute: confed
              state: present
        ipv4_network:
           - address: 101.1.1.0/30
             state: present
        ipv6_network:
          - address: "2001:4898:5808:ffa0::/126"
            state: present
        neighbor:
          - name: ebgp_pg
            type: peergroup
            bfd: yes
            state: present
            address_family:
               - type: ipv4
                 activate: false
                 state: present
                 max_prefix:
                    count: 20
                    threshold: 90
                    warning: true
                    state: present
            listen:
               - subnet: 4.4.4.4/32
                 limit: 4
                 subnet_state: present
               - subnet: 20::/64
                 limit: 4
                 subnet_state: present
          - name: ibgp_pg
            type: peergroup
            weight: 10
            state: present
          - type: ipv4
            interface: vlan20
            send_community:
              - type: extended
                state: present
            address_family:
              - type: l2vpn
                activate: true
                state: present
            admin: up
            state: present
          - type: ipv4
            description: "U_site2-spine1"
            remote_asn: 11
            ip: 192.168.10.1
            peergroup: peer1
            peergroup_state: present
            peergroup_type: ibgp
            adv_interval: 40
            fall_over: present
            password: bgppassword
            route_reflector_client: true
            adv_start: 100
            adv_start_state: present
            conn_retry_timer: 20
            remove_pri_as: present
            src_loopback: 0
            address_family: 
              - type: ipv4
                activate: true
                state: present
                max_prefix:
                   count: 10
                   threshold: 40
                   warning: true
                   state: present
                default_originate:
                   route_map: aa
                   state: present
                distribute_list:
                   in: XX
                   in_state: present
                   out: YY 
                   out_state: present
            send_community:
              - type: standard
                state: present
            state: present
          - type: ipv4
            remote_asn: 13
            local_as: 10
            weight: 10
            ip: 192.168.12.3
            address_family:
              - type: ipv4
                activate: true
                allow_as_in: 5
                next_hop_self: true
                soft_reconf: true
                add_path: both 3
                route_map:
                  - name: qq
                    filter: in
                    state: present
                state: present
            state: present
          - type: ipv6
            remote_asn: 14
            ip: 2001:4898:5808:ffa2::1
            state: present
          - type: ipv6
            description: "U_site2-spine1-Auto Discovered peers"
            auto_peer: unnumbered-auto
            ebgp_peergroup: ebgp_pg
            ebgp_peergroup_state: absent
            ibgp_peergroup: ibgp_pg
            ibgp_peergroup_state: present
            sender_loop_detect: true
            password: bgppassword
            address_family:
              - type: ipv4
                activate: true
                sender_loop_detect: true
                state: present
                allow_as_in: 5
                next_hop_self: true
                soft_reconf: true
              - type: l2vpn
                activate: true
                sender_loop_detect: false
                state: present
            send_community:
              - type: standard
                state: present
            admin: up
            state: present
        redistribute:
          - route_type: static
            route_map_name: aa
            address_type: ipv4
            state: present
        bfd_all_neighbors:
          interval: 200
          min_rx: 200
          multiplier: 3
          role: active
          state: present
        vrfs:
          - name: "GREEN"
            router_id: 50.1.1.1
            maxpath_ibgp: 2
            maxpath_ebgp: 2
            graceful_restart: true
            log_neighbor_changes: false
            fast_ext_fallover: false
            always_compare_med: true
            default_loc_pref: 1000
            route_reflector:
              client_to_client: false
              cluster_id: 1 
            address_family_ipv4:
              aggregate_address:
                 - ip_and_mask: 1.1.1.1/16
                   state: present
              dampening:
                value: 15 750 2000 60
                route_map: qq
                state: present
              ibgp_redist_internal:
                state: present
            address_family_ipv6:
              aggregate_address:
                 - ip_and_mask: 2001:4898:5808:ffa0::/126
                   state: present
                   summary_only: true
              ibgp_redist_internal:
                state: present
            best_path:
               as_path: ignore
               as_path_state: present
               ignore_router_id: true
               med:
                - attribute: confed
                  state: present
                - attribute: missing-as-worst
                  state: present
            ipv4_network:
               - address: 101.1.1.0/30
                 state: present
            ipv6_network:
               - address: "2001:4898:5808:ffa0::/126"
                 state: present
            neighbor:
              - name: peer1
                type: peergroup
                bfd: yes
                state: present
              - name: ebgp_pg
                type: peergroup
                bfd: yes
                state: present
              - name: ibgp_pg
                type: peergroup
                weight: 10
                state: present
              - type: ipv4
                interface: vlan10
                description: U_site2 vlan
                send_community:
                  - type: extended
                    state: present
                admin: up
                state: present
              - type: ipv4
                description: "U_site2 spine1"
                remote_asn: 11
                ip: 192.168.20.1
                name: peer1
                peergroup: peer1
                peergroup_state: present
                peergroup_type: ibgp
                adv_interval: 40
                fall_over: present
                route_reflector_client: true
                src_loopback: 0
                address_family:
                  - type: ipv4
                    activate: false
                    state: present
                send_community:
                  - type: standard
                    state: present
                state: present
              - type: ipv4
                description: "U_site2 spine1"
                remote_asn: 13
                local_as: 10
                weight: 10
                ip: 192.168.15.3
                address_family:
                  - type: ipv4
                    activate: false
                    allow_as_in: 5
                    next_hop_self: true
                    soft_reconf: true
                    add_path: both 3
                    route_map:
                      - name: qq
                        filter: in
                        state: present
                    state: present
                state: present
              - type: ipv6
                remote_asn: 14
                ip: 2001:4898:5808:ffa2::1
                state: present
              - type: ipv6
                description: "U_site2-spine1-Auto Discovered peers"
                auto_peer: unnumbered-auto
                ebgp_peergroup: ebgp_pg
                ebgp_peergroup_state: present
                ibgp_peergroup: ibgp_pg
                ibgp_peergroup_state: present
                address_family:
                  - type: ipv4
                    activate: false
                    sender_loop_detect: false
                    state: present
                    allow_as_in: 5
                    next_hop_self: true
                    soft_reconf: true
                send_community:
                  - type: standard
                    state: present
                admin: up
                state: present
            redistribute:
              - route_type: static
                route_map_name: aa
                address_type: ipv4
                state: present
              - route_type: connected
                route_map_name: bb
                address_type: ipv4
                state: present
              - route_type: l2vpn
                route_map_name: cc
                address_type: ipv4
                state: present
              - route_type: imported_bgp
                imported_bgp_vrf_name: test6
                route_map_name: dd
                address_type: ipv4
                state: present
              - route_type: ospf
                ospf_id: 12
                address_type: ipv4
                state: present
            bfd_all_neighbors:
              interval: 200
              min_rx: 200
              multiplier: 3
              role: active
              state: present
            state: present
        state: present


**Simple playbook to configure BGP — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_bgp

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

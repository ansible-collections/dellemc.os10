Route-map role
==============

This role facilitates the configuration of route-map attributes. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10. 

The route-map role requires an SSH connection for connectivity to a Dell EMC OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable 
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os10_route_map keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``route_map`` | list | Configures the route-map (see ``route_map.*``) | os10 |
| ``route_map.name`` | string (required)        | Configures the route-map name  | os10 |
| ``route_map.permit`` | boolean | Configures permit/deny set operations | os10 |
| ``route_map.seq_num`` | integer         | Configures the sequence number | os10 |
| ``route_map.continue`` | integer         | Configures the next sequence number | os10 |
| ``route_map.set`` | dictionary | Configures route-map to set values in the destination routing protocol (see ``set.*``) | os10 |
| ``set.local_pref`` | integer   | Configures the BGP local preference path attribute     | os10 |
| ``set.metric`` | string | Configures a specific value to add or subtract from the existing metric value ("+ <value>", "- <value>", <value> format)   | os10 |
| ``set.metric_type`` | string: internal,type-1,type-2 | Configures the metric type for the destination routing protocol     | os10 |
| ``set.origin`` | string: igp,egp,incomplete   | Configures the BGP origin attribute     | os10 |
| ``set.weight`` | integer   | Configures the weight for the BGP route     | os10 |
| ``set.comm_list`` | dictionary   | Configures the BGP community list (see ``comm_list.*``)    | os10 |
| ``comm_list.add`` | string | Adds the community attribute of a BGP update | os10 |
| ``comm_list.delete`` | string | Deletes a community attribute of a BGP update | os10 |
| ``set.community`` | string   | Configures the community attribute for a BGP route update     | os10 |
| ``set.extcomm_list`` | dictionary   | Configures the BGP extcommunity list (see ``extcomm_list.*``)    | os10 |
| ``extcomm_list.add`` | string | Adds an extended community attribute of a BGP update | os10 |
| ``extcomm_list.delete`` | string | Deletes the extended community attribute of a BGP update | os10 |
| ``set.extcommunity`` | string   | Configures the extended community attribute for a BGP route update     | os10 |
| ``set.next_hop`` | list   | Configures the next-hop address (see ``next_hop.*``)  | os10 |
| ``next_hop.type`` | string: ip,ipv6 | Configures the type of the next-hop address | os10 |
| ``next_hop.address`` | string | Configures the next-hop address | os10 |
| ``next_hop.track_id`` | integer | Configures the object track ID | os10 |
| ``next_hop.state`` | string: present\*,absent   | Deletes the next-hop address if set to absent  | os10 |
| ``route_map.match`` | list | Configures the route-map to match values from the route table (see ``match.*``) | os10 |
| ``match.ip_type`` | string (required): ipv4,ipv6   | Configures the IPv4/IPv6 address to match    | os10 |
| ``match.access_group`` | string     | Configures the access-group or list to match                  | os10 |
| ``match.source_protocol_ebgp`` | string     | Configures the source protocol to eBGP to match       | os10 |
| ``match.source_protocol_ibgp`` | string     | Configures the source protocol to iBGP to match       | os10 |
| ``match.source_protocol_evpn`` | string     | Configures the source protocol to EVPN to match       | os10 |
| ``match.source_protocol_static`` | string     | Configures the source protocol to static to match       | os10 |
| ``match.source_protocol_connected`` | string     | Configures the source protocol to connected to match       | os10 |
| ``match.source_protocol_ospf`` | string     | Configures the source protocol to OSPF to match       | os10 |
| ``match.prefix_list`` | string     | Configures the IP prefix-list to match against                  | os10 |
| ``route_map.state`` | string, choices: present\*,absent   | Deletes the route-map if set to absent  | os10 |
| ``as_path`` | list | Configures the BGP AS path filter (see ``as_path.*``) | os10 |
| ``as_path.access_list`` | string (required)         | Configures the access-list name               | os10 |
| ``as_path.permit`` | boolean (required) | Configures an AS path to accept or reject   | os10  |
| ``as_path.regex``| string (required)         | Configures a regular expression              | os10 |
| ``as_path.state`` | string: absent,present\*     | deletes the BGP as path filter if set to absent         | os10 |
| ``community_list`` | list | Configures a community list entry (see ``community_list.*``) | os10 |
| ``community_list.type`` | string (required): standard,expanded        | Configures the type of community-list entry              | os10 |
| ``community_list.name`` | string (required)     | Configures the name of community-list entry             | os10 |
| ``community_list.permit`` | boolean(required) | Configures the community to accept or reject   | os10 |
| ``community_list.regex`` | string (required)         | Configures the regular expression for extended community list; mutually exclusive with *community_list.community*    | os10 |
| ``community_list.community`` | string (required)         | Configures a well-known community or community number for standard community list; mutually exclusive with *community_list.regex*            | os10 |
| ``community_list.state`` | string: absent,present\*     | Deletes the community list entry if set to absent  | os10 |
| ``extcommunity_list`` | list | Configures extcommunity-list entry (see ``extcommunity_list.*``)   | os10 |
| ``extcommunity_list.type`` | string (required): standard,expanded    | Configures the type of extcommunity-list entry              | os10 |
| ``extcommunity_list.name`` | string (required)     | Configures the name of extcommunity-list entry             | os10 |
| ``extcommunity_list.permit`` | boolean(required) | Configures the extcommunity to accept or reject   | os10  |
| ``extcommunity_list.regex`` | string (required)         | Configures the regular expression for the extended extcommunity list; mutually exclusive with *extcommunity_list.community*    | os10 |
| ``extcommunity_list.community`` | string (required)         | Configures the extended community for standard community-list; mutually exclusive with *extcommunity_list.regex*            | os10 |
| ``extcommunity_list.state`` | string: absent,present\*     | Deletes the extcommunity-list entry if set to absent   | os10 |

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

This example uses the *os10_route_map* role for the route-map, policy-map, and class-map. It creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the `ansible_network_os` variable with corresponding Dell EMC OS10 name. 

When `os10_cfg_generate` is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, the variable is set to false. It writes a simple playbook that only references the *os10_route_map* role. By including the role, you automatically get access to all of the tasks to configure route-map features. 

**Sample hosts file**
 
    leaf1 ansible_host= <ip_address> 

**Sample host_vars/leaf1**

    hostname: leaf1
    ansible_ssh_user: xxxxx
    ansible_ssh_pass: xxxxx
    ansible_network_os: dellemc.os10.os10
    build_dir: ../temp/os10
	  
    os10_route_map:
      as_path:
        - access_list: aa
          permit: true
          regex: www
          state: present
      community_list:
        - type: expanded
          name: qq
          permit: true
          regex: aaa
          state: present
        - type: standard
          name: qqq
          permit: false
          community: internet
          state: present
      extcommunity_list:
        - type: expanded
          name: qq
          permit: true
          regex: aaa
          state: present
        - type: standard
          name: qqq
          permit: false
          community: "rt 22:33"
          state: present
      route_map:
        - name:  test
          permit: true
          seq_num: 1
          continue: 20
          match:
           - ip_type: ipv4
             access_group: testaccess
             prefix_list: testprefix
             source_protocol_ebgp: present
             source_protocol_ibgp: present
             source_protocol_evpn: present
             source_protocol_static: present
             source_protocol_ospf: present
             source_protocol_connected: present
          set:
            local_pref: 1200
            metric_type: internal
            metric: + 30
            origin: igp
            weight: 50
            next_hop:
              - type: ip
                address: 10.1.1.1
                track_id: 3
                state: present
            community: internet
            comm_list:
              add: qq
              delete: qqq
            extcommunity: "22:33"
            extcomm_list:
              add: aa
              delete: aa
          state: present

**Simple playbook to setup QoS —leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_route_map

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

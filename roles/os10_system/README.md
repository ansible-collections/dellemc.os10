System role
===========

This role facilitates the configuration of global system attributes. It specifically enables configuration of hostname and hashing algorithm. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The System role requires an SSH connection for connectivity to a Dell EMC OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os10_system keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``hostname`` | string | Configures a hostname to the device (no negate command) | os10 |
| ``hardware_forwarding`` | string: scaled-l2,scaled-l3-routes,scaled-l3-hosts         | Configures hardware forwarding mode | os10 |
| ``hash_algo`` | dictionary | Configures hash algorithm commands (see ``hash_algo.*``) | os10 |
| ``hash_algo.algo`` | list         | Configures hashing algorithm (see ``algo.*``)   | os10 |
| ``algo.name`` | string (required)       | Configures the name of the hashing algorithm | os10 |
| ``algo.mode`` | string (required)       | Configures the hashing algorithm mode |  os10 |
| ``algo.state`` | string: absent,present\*     | Deletes the hashing algorithm if set to absent           | os10 |
| ``load_balance`` | dictionary | Configures the global traffic load balance (see ``load_balance.*``) | os10 |
| ``load_balance.ingress_port`` | boolean: true,false       | Specifies whether to use the source port ID for the hashing algorithm | os10 |
| ``load_balance.ip_selection`` | list    | Configures IPv4 key fields to use in hashing algorithm; | os10 |
| ``ip_selection.field`` | string | Configures IPv4 key fields to use in hashing algorithm | os10 |
| ``ip_selection.state`` | string: absent,present\* | Deletes the IPv4 key fields if set to absent | os10 |
| ``load_balance.ipv6_selection`` | list    | Configures IPv6 key fields to use in hashing algorithm | os10 |
| ``ipv6_selection.field`` | string | Configures IPv6 key fields to use in hashing algorithm | os10 |
| ``ipv6_selection.state`` | string: absent,present\* | Deletes the IPv6 key fields if set to absent | os10 |
| ``load_balance.mac_selection`` | list    | Configures MAC key fields to use in hashing algorithm (see ``mac_selection.*``) | os10 |
| ``mac_selection.field`` | string | Configures MAC key fields to use in hashing algorithm | os10 |
| ``mac_selection.state`` | string: absent,present\* | Deletes the MAC key fields if set to absent | os10 |
| ``load_balance.tcp_udp_selection`` | list    | Configures TCP UDP ports for load balancing configurations (see ``tcp_udp_selection.*``) | os10 |
| ``tcp_udp_selection.field`` | string | Configures TCP UDP port fields to use in hashing algorithm | os10 |
| ``tcp_udp_selection.state`` | string: absent,present\* | Deletes the TCP UDP ports if set to absent | os10 |
| ``min_ra`` | string | Configure global RA minimum interval value, applicable to all interfaces across VRFs | os10 |
| ``max_ra`` | string | Configure global RA maximum interval value, applicable to all interfaces across VRFs | os10 |

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

This example uses the *os10_system role* to completely set the NTP server, hostname, enable password, management route, hash alogrithm, clock, line terminal, banner and reload type. It creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the `ansible_network_os` variable with corresponding Dell EMC OS10 name. 

When `os10_cfg_generate` is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, the variable is set to false. The system role writes a simple playbook that only references the *os10_system* role. By including the role, you automatically get access to all of the tasks to configure system features. 

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
	  
    os10_system:
        hostname: os10
        hardware_forwarding: scaled-l3-hosts
        hash_algo:
          algo:
            - name: lag
              mode: crc
              state: present
            - name: ecmp
              mode: xor
              state: present
        load_balance:
            ingress_port: true
            ip_selection:
              - field: source-ip
                state: present
            ipv6_selection:
              - field: source-ip
                state: present
            mac_selection:
              - field: source-mac
                state: present
            tcp_udp_selection:
              - field: l4-source-port
                state: present
        max_ra: 15
        min_ra: 10

**Simple playbook to setup system — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_system

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

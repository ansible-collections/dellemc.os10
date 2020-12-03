VLT role
========

This role facilitates the configuration of the basics of virtual link trunking (VLT) to provide a loop-free topology. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The VLT role requires an SSH connection for connectivity to a Dell EMC SmartFabric OS10 device. You can use any of the built-in OS connection variables .

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable  that can take `dellemc.os10.os10` value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os10_vlt keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``domain``       | integer (required)        | Configures the VLT domain identification number (1 to 1000) | os10 |
| ``backup_destination`` | string    | Configures an IPv4 address for the VLT backup link (A.B.C.D format or X:X:X:X::X format) | os10 |
| ``destination_type``  | string    | Configures the backup destination based on this destination type (IPv4 or IPv6)| os10 |
| ``backup_destination_vrf``      | string         | Configures the virtual routing and forwarding (VRF) instance through which the backup destination IP is reachable (*vrfname* must be present)  | os10 |
| ``discovery_intf``    | string        | Configures the discovery interface for the VLT domain (range of interfaces)| os10 |
| ``discovery_intf_state``        | string: absent,present       | Deletes the discovery interfaces for the VLT domain if set to absent | os10 |
| ``peer_routing``     | boolean        | Configures VLT peer routing | os10 |
| ``priority``      | integer (default:32768)        | Configures VLT priority | os10 |
| ``vlt_mac``       | string        | Configures the VLT MAC address | os10 |
| ``vlt_peers``     | dictionary       | Contains objects to configure the VLT peer port-channel (see ``vlt_peers.*``)  | os10 |
| ``vlt_peers.<portchannelid>``    | dictionary       | Configures the VLT peer port-channel (`Po <portchannelid> value`) | os10 |
| ``vlt_peers.<portchannelid>.peer_lag``     | integer       | Configures the port-channel ID of the VLT peer lag  |  os10 |
| ``state``        | string: absent,present     | Deletes the VLT instance if set to absent | os10 |

> **NOTE**: Asterisk (\*) denotes the default value if none is specified.

Connection variables
--------------------

Ansible Dell EMC network OS roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories or inventory, or in the playbook itself.

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

Dependencies
------------

The *os10_vlt* role is built on modules included in the core Ansible code. These modules were added in ansible version 2.2.0.

Example playbook
----------------

This example uses the *os10_vlt* role to setup a VLT-domain. It creates a *hosts* file with the switch details and corresponding variables.The hosts file should define the `ansible_network_os` variable with corresponding Dell EMC OS10 name.

When `os10_cfg_generate` is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, the variable is set to false. It writes a simple playbook that only references the *os10_vlt* role.

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

    os10_vlt:
        domain: 1
        backup_destination: "192.168.211.175"
        destination_type: "ipv4"
        backup_destination_vrf:
        discovery_intf: 1/1/12
        discovery_intf_state: present
        peer_routing: True
        vlt_mac: aa:aa:aa:aa:aa:aa
        vlt_peers:
          Po 12:
           peer_lag: 13
        state: present

> **NOTE**: Discovery interface must not be in switchport mode and can be configured using the *os10_interface* role.

**Simple playbook to setup system — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_vlt

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

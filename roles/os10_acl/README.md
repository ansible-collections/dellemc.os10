ACL role
========

This role facilitates the configuration of an access-control list (ACL). It supports the configuration of different types of ACLs (standard and extended) for both IPv4 and IPv6, and assigns the access-class to the line terminals. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The ACL role requires an SSH connection for connectivity to a Dell EMC SmartFabric OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os10_acl keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``type`` | string (required): ipv4, ipv6, mac        | Configures the L3 (IPv4/IPv6) or L2 (MAC) access-control list | os10 |
| ``name`` | string (required)           | Configures the name of the access-control list | os10 |
| ``description`` | string           | Configures the description about the access-control list | os10 |
| ``remark`` | list           | Configures the ACL remark (see ``remark.*``)  | os10|
| ``remark.number`` | integer (required)        | Configures the remark sequence number | os10 |
| ``remark.description`` | string        | Configures the remark description | os10 |
| ``remark.state`` | string: absent,present\*   | Deletes the configured remark for an ACL entry if set to absent | os10 |
| ``entries`` | list | Configures ACL rules (see ``seqlist.*``) |  os10 |
| ``entries.number`` | integer (required)       | Specifies the sequence number of the ACL rule | os10 |
| ``entries.permit`` | boolean (required): true,false         | Specifies the rule to permit packets if set to true; specifies to reject packets if set to false | os10 |
| ``entries.protocol`` | string (required)       | Specifies the type of protocol or the protocol number to filter | os10 |
| ``entries.source`` | string (required)        | Specifies the source address to match in the packets | os10 |
| ``entries.src_condition`` | string         | Specifies the condition to filter packets from the source address; ignored if MAC | os10 |
| ``entries.destination`` | string (required)      | Specifies the destination address to match in the packets | os10 |
| ``entries.dest_condition`` | string         | Specifies the condition to filter packets to the destination address | os10 |
| ``entries.other_options`` | string         | Specifies the other options applied on packets (count, log, order, monitor, and so on) | os10 |
| ``entries.state`` | string: absent,present\*   | Deletes the rule from the ACL if set to absent | os10 |
| ``stage_ingress`` | list           | Configures ingress ACL to the interface (see ``stage_ingress.*``) | os10 |
| ``stage_ingress.name`` | string (required)        | Configures the ingress ACL filter to the interface with this interface name | os10 |
| ``stage_ingress.state`` | string: absent,present\*   | Deletes the configured ACL from the interface if set to absent | os10 |
| ``stage_egress`` | list           | Configures egress ACL to the interface (see ``stage_egress.*``) | os10 |
| ``stage_egress.name`` | string (required)        | Configures the egress ACL filter to the interface with this interface name | os10 |
| ``stage_egress.state`` | string: absent,present\*   | Deletes the configured egress ACL from the interface if set to absent | os10 |
| ``lineterminal`` | list | Configures the terminal to apply the ACL (see ``lineterminal.*``) | os10 |
| ``lineterminal.state`` | string: absent,present\*       | Deletes the access-class from line terminal if set to absent | os10 |
| ``state`` | string: absent,present\*       | Deletes the ACL if set to absent | os10 |

> **NOTE**: Asterisk (\*) denotes the default value if none is specified. 

Connection variables
--------------------

Ansible Dell EMC network roles require connection information to establish communication with the nodes in inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories or inventory, or in the playbook itself.

| Key         | Required | Choices    | Description                                           |
|-------------|----------|------------|-------------------------------------------------------|
| ``ansible_host`` | yes      |            | Specifies the hostname or address for connecting to the remote device over the specified transport |
| ``ansible_port`` | no       |            | Specifies the port used to build the connection to the remote device; if value is unspecified, the `ANSIBLE_REMOTE_PORT` option is used; it defaults to 22 |
| ``ansible_ssh_user`` | no       |            | Specifies the username that authenticates the CLI login for the connection to the remote device; if value is unspecified, the `ANSIBLE_REMOTE_USER` environment variable value is used  |
| ``ansible_ssh_pass`` | no       |            | Specifies the password that authenticates the connection to the remote device |
| ``ansible_become`` | no       | yes, no\*   | Instructs the module to enter privileged mode on the remote device before sending any commands; if value is unspecified, the `ANSIBLE_BECOM`E environment variable value is used, and the device attempts to execute all commands in non-privileged mode |
| ``ansible_become_method`` | no       | enable, sudo\*   | Instructs the module to allow the become method to be specified for handling privilege escalation; if value is unspecified, the `ANSIBLE_BECOME_METHOD` environment variable value is used |
| ``ansible_become_pass`` | no       |            | Specifies the password to use if required to enter privileged mode on the remote device; if ``ansible_become`` is set to no this key is not applicable |
| ``ansible_network_os`` | yes      | os10, null\*  | Loads the correct terminal and cliconf plugins to communicate with the remote device |

> **NOTE**: Asterisk (_*_) denotes the default value if none is specified.


Example playbook
----------------

This example uses the *os10_acl* role to configure different types of ACLs (standard and extended) for both IPv4 and IPv6 and assigns the access-class to the line terminals. The example creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the `ansible_network_os` variable with the corresponding Dell EMC OS10 name. 

When `os10_cfg_generate` is set to true, it generates the configuration commands as a .part file in the *build_dir* path. By default it is set to false. It writes a simple playbook that only references the *os10_acl* role. 

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
    os10_acl:
       - name: ssh
         type: ipv4
         description: acl
         remark:
           - description: 1
             number: 3
             state: absent
         entries:
           - number: 14
             permit: true
             protocol: tcp
             source: any
             src_condition: neq 6
             destination: any
             dest_condition: eq 4
             other_options: count
             state: present
         stage_ingress:
              - name: ethernet 1/1/1
                state: absent
              - name: ethernet 1/1/2
                state: absent
         stage_egress:
              - name: ethernet 1/1/3
                state: absent
         lineterminal:
              state: absent
         state: present
            
**Simple playbook to setup system — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_acl

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.
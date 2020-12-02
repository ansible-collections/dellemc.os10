VLAN role
=========

This role facilitates configuring virtual LAN (VLAN) attributes. It supports the creation and deletion of a VLAN and its member ports. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10. 

The VLAN role requires an SSH connection for connectivity to a Dell EMC SmartFabric OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- For variables with no state variable, setting an empty value for the variable negates the corresponding configuration
- `os10_vlan` (dictionary) holds the key with the VLAN ID key and default-vlan key.
- VLAN ID key should be in format "vlan ID" (1 to 4094)
- Variables and values are case-sensitive

**os10_vlan**

| Key        | Type                      | Notes                                                   | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``default_vlan_id`` | integer | Configures the vlan-id as the default VLAN for an existing VLAN | os10 |

**VLAN ID keys**

| Key        | Type                      | Notes                                                   | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``description``      | string          | Configures a single line description for the VLAN | os10 |
| ``tagged_members``   | list         | Specifies the list of port members to be tagged to the corresponding VLAN (see ``tagged_members.*``) | os10 |
| ``tagged_members.port`` | string | Specifies valid device interface names to be tagged for each VLAN | os10 |
| ``tagged_members.state`` | string: absent,present | Deletes the tagged association for the VLAN if set to absent | os10 |
| ``untagged_members`` | list         | Specifies the list of port members to be untagged to the corresponding VLAN (see ``untagged_members.*``) | os10 |
| ``untagged_members.port`` | string | Specifies valid device interface names to be untagged for each VLAN | os10 |
| ``untagged_members.state`` | string: absent,present | Deletes the untagged association for the VLAN if set to absent | os10 |
| ``state``           | string: absent,present\*          | Deletes the VLAN corresponding to the ID if set to absent | os10 |
| ``virtual_gateway_ip``     | string     | Configures an anycast gateway IPv4 address for VLAN interfaces| os10  |
| ``virtual_gateway_ipv6``     | string     | Configures an anycast gateway IPv6 address for VLAN interfaces| os10  |
| ``ip_and_mask`` | string | Configures the specified IP address to the interface | os10 |
                                                                                                      
> **NOTE**: Asterisk (\*) denotes the default value if none is specified.

Connection variables
--------------------

Ansible Dell EMC network roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars directories* or inventory, or in the playbook itself.

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


## Example playbook

This example uses the *os10_vlan* role to setup the VLAN ID and name, and it configures tagged and untagged port members for the VLAN. You can also delete the VLAN with the ID or delete the members associated to it. It creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the `ansible_network_os` variable with corresponding Dell EMC OS10 name. 

When `os10_cfg_generate` is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, the variable is set to false. It writes a simple playbook that only references the *os10_vlan* role.

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

    os10_vlan:
        default_vlan_id: 2
        vlan 100:
          description: "Blue"
          tagged_members:
              - port: ethernet 1/1/32
                state: present
              - port: ethernet 1/1/31
                state: present
          untagged_members:
              - port: ethernet 1/1/30
                state: present
              - port: ethernet 1/1/29
                state: present
          state: present
        vlan 888:
          description: "NSX_Cluster"
          untagged_members:
            - port: port-channel 1
              state: "present"
          state: "present"
        vlan 10:
          description: "vlan with anycast GW"
          ip_and_mask: "10.1.1.1/24"
          virtual_gateway_ip: "10.1.1.254"
          virtual_gateway_ipv6: "10:1:1::254"
          state: "present"

> **NOTE**: Interfaces should be created using the *os10_interface* role.

**Simple playbook to setup system — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_vlan
                
**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

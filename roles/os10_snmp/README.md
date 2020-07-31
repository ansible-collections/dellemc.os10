SNMP role
=========

This role facilitates the configuration of global SNMP attributes. It supports the configuration of SNMP server attributes including users, group, community, location, and traps. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The SNMP role requires an SSH connection for connectivity to a Dell EMC OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os10_snmp keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``snmp_contact`` | string | Configures SNMP contact information  | os10 |
| ``snmp_location`` | string | Configures SNMP location information | os10 |
| ``snmp_community`` | list | Configures SNMP community information (see ``snmp_community.*``) | os10 |
| ``snmp_community.name`` | string (required)         | Configures the SNMP community string | os10 |
| ``snmp_community.access_mode`` | string: ro,rw           | Configures access-mode for the community | os10 |
| ``snmp_community.state`` | string: absent,present\*   | Deletes the SNMP community information if set to absent | os10 |
| ``snmp_host`` | list | Configures SNMP hosts to receive SNMP traps (see ``snmp_host.*``) | os10 |
| ``snmp_host.ip`` | string | Configures the IP address of the SNMP trap host | os10  |
| ``snmp_host.communitystring`` | string | Configures the SNMP community string of the trap host | os10 |
| ``snmp_host.udpport`` | string | Configures the UDP number of the SNMP trap host (0 to 65535) | os10 |
| ``snmp_host.version`` | string (required) | Specifies the SNMP version of the host (1 or 2c in os10) | os10 |
| ``snmp_host.state`` | string: absent,present\* | Deletes the SNMP trap host if set to absent | os10 |
| ``snmp_traps`` | list | Configures SNMP traps (see ``snmp_traps.*``) | os10  |
| ``snmp_traps.name`` | string | Enables SNMP traps   | os10 |
| ``snmp_traps.state`` | string: absent,present\* | Deletes the SNMP trap if set to absent | os10 |
| ``snmp_view`` | list | Configures SNMPv3 view information (see ``snmp_view.*``) | os10 |
| ``snmp_view.name`` | string | Configures the SNMP view name (up to 20 characters) | os10 |
| ``snmp_view.oid_subtree`` | integer | Configures the SNMP view for the OID subtree | os10 |
| ``snmp_view.include`` | boolean: true,false | Specifies if the MIB family should be included or excluded from the view | os10 |
| ``snmp_view.state`` | string: absent,present\* | Deletes the SNMP view if set to absent | os10 |


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

This example uses the *os10_snmp* role to completely set up the SNMP server attributes. It creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the `ansible_network_os` variable with corresponding Dell EMC OS10 name. 

When `os10_cfg_generate` is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, the variable is set to false. It writes a simple playbook that only references the *os10_snmp* role. By including the role, you automatically get access to all of the tasks to configure SNMP features. 

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
	  
    os10_snmp:
        snmp_contact:  test
        snmp_location: Chennai
        snmp_community:
          - name: public
            access_mode: ro
            state: present
        snmp_traps: 
          - name: all
            state: present
        snmp_view:
          - name: view_1
            oid_subtree: 2
            include: true
            state: absent
        snmp_host:
          - ip: 1.1.1.1
            communitystring: c1
            version: "2c"
            udpport: 4
            state: present
          - ip: 2.2.2.2
            version: 1
            communitystring: c3
            state: present

**Simple playbook to setup SNMP — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_snmp

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

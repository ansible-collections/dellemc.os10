SNMP role
=========

This role facilitates the configuration of global SNMP attributes. It supports the configuration of SNMP server attributes including users, group, community, location, and traps. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The SNMP role requires an SSH connection for connectivity to a Dell EMC SmartFabric OS10 device. You can use any of the built-in OS connection variables.

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
| ``snmp_community.access_list`` | dictionary | Configures ACL for the community (see ``snmp_community.access_list.*``) | os10 |
| ``snmp_community.access_list.name`` | string | Specifies the name of the ACL for the community | os10 |
| ``snmp_community.access_list.state`` | string: absent,present\* | Deletes the ACL from the community if set to absent | os10 |
| ``snmp_community.state`` | string: absent,present\*   | Deletes the SNMP community information if set to absent | os10 |
| ``snmp_engine_id`` | string | Configures SNMP local EngineID | os10 |
| ``snmp_remote_engine_id`` | list | Configures SNMP remote engine information (see ``snmp_remote_engine_id.*``) | os10 |
| ``snmp_remote_engine_id.ip`` | string | Configures the IP address of the SNMP remote engine | os10 |
| ``snmp_remote_engine_id.engine_id`` | string | Configures the EngineID of the SNMP remote engine | os10 |
| ``snmp_remote_engine_id.udpport`` | string | Configures the UDP port of the SNMP remote engine | os10 |
| ``snmp_remote_engine_id.state`` | string: absent,present\* | Deletes the SNMP remote engine information if set to absent | os10 |
| ``snmp_group`` | list | Configures the SNMP group information (see ``snmp_group.*``) | os10 |
| ``snmp_group.name`` | string | Configures the name of the SNMP group | os10 |
| ``snmp_group.version`` | string: 1,2c,3 | Configures the version of the SNMP group | os10 |
| ``snmp_group.security_level`` | string: auth,noauth,priv | Configures the security level of SNMP group for version 3 | os10 |
| ``snmp_group.access_list`` | dictionary | Configures the access list of the SNMP group (see ``snmp_group.access_list.*``)| os10 |
| ``snmp_group.access_list.name`` | string | Specifies the name of the access list for the SNMP group wtih version 1 or 2c | os10 |
| ``snmp_group.access_list.state`` | string: absent,present\* | Deletes the access list from the SNMP group if set to absent | os10 |
| ``snmp_group.read_view`` | dictionary | Configures the read view of the SNMP group (see ``snmp_group.read_view.*``) | os10 |
| ``snmp_group.read_view.name`` | string | Specifies the name of the read view for the SNMP group | os10 |
| ``snmp_group.read_view.state`` | string: absent,present\* | Deletes the read view from the SNMP group if set to absent | os10 |
| ``snmp_group.write_view`` | dictionary | Configures the write view of the SNMP group (see ``snmp_group.write_view``) | os10 |
| ``snmp_group.write_view.name`` | string | Specifies the name of the write view for the SNMP group | os10 |
| ``snmp_group.write_view.state`` | string: absent,present\* | Deletes the write view from the SNMP group if set to absent | os10 |
| ``snmp_group.notify_view`` | dictionary | Configures the notify view of the SNMP group (see ``snmp_group.notify_view.*``) | os10 |
| ``snmp_group.notify_view.name`` | string | Specifies the name of the notify view for the SNMP group | os10 |
| ``snmp_group.notify_view.state`` | string: absent,present\* | Deletes the notify view from the SNMP group if set to absent | os10 |
| ``snmp_group.state`` | string: absent,present\* | Deletes the SNMP group if set to absent | os10 |
| ``snmp_host`` | list | Configures SNMP hosts to receive SNMP traps (see ``snmp_host.*``) | os10 |
| ``snmp_host.ip`` | string | Configures the IP address of the SNMP trap host | os10  |
| ``snmp_host.communitystring`` | string | Configures the SNMP community string of the trap host for version 1 or 2c | os10 |
| ``snmp_host.udpport`` | string | Configures the UDP number of the SNMP trap host (0 to 65535) | os10 |
| ``snmp_host.version`` | string: 1,2c,3 (required) | Specifies the SNMP version of the host (1 or 2c or 3 in os10) | os10 |
| ``snmp_host.security_level`` | string: auth,noauth,priv | Configures the security level of the SNMP host for version 3 | os10 |
| ``snmp_host.security_name`` | string | Configures the security name of the SNMP host for version 3 | os10 |
| ``snmp_host.notification_type`` | string: traps,informs | Configures the notification type of the SNMP host | os10 |
| ``snmp_host.trap_categories`` | dictionary | Enables or disables different trap categories for the SNMP host (see ``snmp_host.trap_categories.*``) | os10 |
| ``snmp_host.trap_categories.dom`` | boolean: true,false | Enables or disables dom category traps for the SNMP host | os10 |
| ``snmp_host.trap_categories.entity`` | boolean: true,false | Enables or disables entity category traps for the SNMP host | os10 |
| ``snmp_host.trap_categories.envmon`` | boolean: true,false | Enables or disables envmon category traps for the SNMP host | os10 |
| ``snmp_host.trap_categories.lldp`` | boolean: true,false | | Enables or disables lldp category traps for the SNMP host | os10 |
| ``snmp_host.trap_categories.snmp`` | boolean: true,false | | Enables or disables snmp category traps for the SNMP host | os10 |
| ``snmp_host.state`` | string: absent,present\* | Deletes the SNMP trap host if set to absent | os10 |
| ``snmp_source_interface`` | string | Configures the source interface for SNMP | os10 |
| ``snmp_traps`` | list | Configures SNMP traps (see ``snmp_traps.*``) | os10  |
| ``snmp_traps.name`` | string | Enables SNMP traps   | os10 |
| ``snmp_traps.state`` | string: absent,present\* | Deletes the SNMP trap if set to absent | os10 |
| ``snmp_user`` | list | Configures the SNMP user information (see ``snmp_user.*``) | os10 |
| ``snmp_user.name`` | string | Specifies the name of the SNMP user | os10 |
| ``snmp_user.group_name`` | string | Specifies the group of the SNMP user | os10 |
| ``snmp_user.version `` | string: 1,2c,3 | Configures the version for the SNMP user | os10 |
| ``snmp_user.access_list`` | string | Configures the access list for the SNMP user with version 1 or 2c | os10 |
| ``snmp_user.authentication`` | dictionary | Configures the authentication information for the SNMP user with version 3 (see ``snmp_user.authentication.*``) | os10 |
| ``snmp_user.authentication.localized`` | boolean: true,false | Configures the password to be in localized key format or not | os10 |
| ``snmp_user.authentication.algorithm`` | string: md5, sha | Configures the authentication algorithm for the SNMP user | os10 |
| ``snmp_user.authentication.password`` | string | Configures the authentication password for the SNMP user; if localized is true it should be a hexadecimal string prefixed with 0x and qouted | os10 |
| ``snmp_user.authentication.encryption`` | dictionary | Configures the encryption parameters for the SNMP user | os10 |
| ``snmp_user.authentication.encryption.algorithm`` | string: aes,des | Configures the encryption algorithm for the SNMP user | os10 |
| ``snmp_user.authentication.encryption.password`` | string | Configures encryption password for the SNMP user; if localized is true it should be a hexadecimal string prefixed with 0x and qouted | os10 |
| ``snmp_user.remote`` | dictionary | Configures the remote SNMP entity the user belongs to (see ``snmp_user.remote.*``) | os10 |
| ``snmp_user.remote.ip`` | string | Configures the IP address of the remote entity for the SNMP user | os10 |
| ``snmp_user.remote.udpport`` | string | Configures the UDP port of the remote entiry for the SNMP user | os10 |
| ``snmp_user.state`` | string: absent,present\* | Deletes the SNMP user if set to absent | os10 |
| ``snmp_view`` | list | Configures SNMPv3 view information (see ``snmp_view.*``) | os10 |
| ``snmp_view.name`` | string | Configures the SNMP view name (up to 20 characters) | os10 |
| ``snmp_view.oid_subtree`` | integer | Configures the SNMP view for the OID subtree | os10 |
| ``snmp_view.include`` | boolean: true,false | Specifies if the MIB family should be included or excluded from the view | os10 |
| ``snmp_view.state`` | string: absent,present\* | Deletes the SNMP view if set to absent | os10 |
| ``snmp_vrf`` | string | Configures the VRF for SNMP | os10 |


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
        snmp_source_interface: loopback 10
        snmp_vrf: test
        snmp_community:
          - name: public
            access_mode: ro
            access_list:
              name: test_acl
              state: present
            state: present
        snmp_engine_id: 123456789
        snmp_remote_engine_id:
          - host: 1.1.1.1
            engine_id: '0xab'
            udpport: 162
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
            trap_categories:
              dom: true
              lldp: true
            state: present
          - ip: 3.1.1.1
            version: 3
            security_level: priv
            security_name: test
            notification_type: informs
            udpport: 200
            trap_categories:
              dom: true
              entity: true
              envmon: true
              snmp: true
            state: present
        snmp_group:
          - name: group_1
            version: "2c"
            state: present
            access_list:
              name: test_acl
              state: present
            read_view:
              name: view_1
              state: present
            write_view:
              name: view_2
              state: present
            notify_view:
              name: view_3
              state: present
          - name: group_2
            version: 3
            security_level: priv
            state: present
            read_view:
              name: view_1
              state: absent
            notify_view:
              name: view_3
              state: present
        snmp_user:
          - name: user_1
            group_name: group_1
            version: 3
            authentication:
              localized: true
              algorithm: md5
              password: 9fc53d9d908118b2804fe80e3ba8763d
              encryption:
                algorithm: aes
                password: d0452401a8c3ce42804fe80e3ba8763d
            state: present
          - name: user_2
            group_name: group_1
            version: 3
            remote:
              ip: 1.1.1.1
              udpport: 200
            authentication:
              localized: true
              algorithm: md5
              password: '0x9fc53d9d908118b2804fe80e3ba8763d'
              encryption:
                algorithm: aes
                password: '0xd0452401a8c3ce42804fe80e3ba8763d'
            state: present
          - name: user_3
            group_name: group_1
            version: 2c
            state: present
          - name: user_4
            group_name: group_1
            version: 3
            state: present
          - name: user_5
            group_name: group_2
            version: 2c
            remote:
              ip: 1.1.1.1
              udpport: 200
            access_list: test_acl
            state: present

**Simple playbook to setup SNMP — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_snmp

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

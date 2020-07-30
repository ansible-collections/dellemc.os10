AAA role
========

This role facilitates the configuration of authentication, authorization, and acccounting (AAA). It supports the configuration of RADIUS server, TACACS server, and AAA. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10. 

The AAA role requires an SSH connection for connectivity to a Dell EMC OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os10_aaa keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``radius_server``            | dictionary        | Configures the RADIUS server (see ``radius_server.*``) | os10 |
| ``radius_server.retransmit`` | integer           | Configures the number of retransmissions | os10  |
| ``radius_server.timeout``    | integer           | Configures the timeout for retransmissions | os10  |
| ``radius_server.host``       | dictionary        | Configures the RADIUS server host (see ``host.*``) | os10  |
| ``host.ip``                  | string            | Configures the RADIUS server host address | os10  |
| ``host.key``                 | string (required); 0,7,LINE           | Configures the authentication key | os10  |
| ``host.auth_port``           | integer           | Configures the authentication port (0 to 65535)  | os10  |
| ``host.state``               | string: present,absent         | Removes the RADIUS server host if set to absent | os10  |
| ``auth.key``                 | string (required); 0,7,LINE           | Configures the authentication key | os10  |
| ``tacacs_server``            | dictionary        | Configures the TACACS server (see ``tacacs_server.*``) | os10 |
| ``tacacs_server.timeout``    | integer           | Configures the timeout for retransmissions | os10  |
| ``tacacs_server.host``       | dictionary        | Configures the TACACS server host (see ``host.*``) | os10  |
| ``host.ip``                  | string            | Configures the TACACS server host address | os10  |
| ``host.key``                 | string (required); 0,7,LINE           | Configures the authentication key | os10  |
| ``host.auth_port``           | integer           | Configures the authentication port (0 to 65535)  | os10  |
| ``host.state``               | string: present,absent         | Removes the TACACS server host if set to absent | os10  |
| ``auth.key``                 | string (required); 0,7,LINE           | Configures the authentication key | os10  |
| ``aaa_accounting``       | dictionary        | Configures accounting parameters (see ``aaa_accounting.*``) | os10  |
| ``aaa_accounting.accounting.accounting_type``       | dictionary        | Configures accounting type | os10  |
| ``aaa_accounting.accounting.connection_type``       | dictionary        | Configures accounting connection type | os10  |
| ``aaa_accounting.accounting.account_mode``       | dictionary        | Configures accounting mode | os10  |
| ``aaa_accounting.accounting.server_group``       | dictionary        | Configures accounting server group | os10  |
| ``aaa_accounting.accounting.state``       | string: present,absent        | Configures/unconfigures accounting parameters | os10  |
| ``aaa_authentication``       | dictionary        | Configures authentication parameters (see ``aaa_authentication.*``) | os10  |
| ``aaa_authentication.login`` | dictionary   | Configures authentication login (see ``aaa_authentication.login.*``)| os10 |
| ``aaa_authentication.login.console`` | dictionary   | Configures authentication method for console login | os10 |
| ``aaa_authentication.login.state`` | string: present,absent   | Unconfigures authentication login if set to absent | os10 |
| ``aaa_authentication.login.type`` | dictionary   | Configures authentication type | os10 |
| ``aaa_authentication.re_authenticate`` | boolean | Configures re-authenticate by enable if set to true | os10 |

> **NOTE**: Asterisk (*) denotes the default value if none is specified.

Connection variables
--------------------

Ansible Dell EMC network roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories or inventory, or in the playbook itself.

| Key         | Required | Choices    | Description                                         |
|-------------|----------|------------|-----------------------------------------------------|
| ``ansible_host`` | yes      |            | Specifies the hostname or address for connecting to the remote device over the specified transport |
| ``ansible_port`` | no       |            | Specifies the port used to build the connection to the remote device; if value is unspecified, the `ANSIBLE_REMOTE_PORT` option is used; it defaults to 22 |
| ``ansible_ssh_user`` | no       |            | Specifies the username that authenticates the CLI login for the connection to the remote device; if value is unspecified, the `ANSIBLE_REMOTE_USER` environment variable value is used  |
| ``ansible_ssh_pass`` | no       |            | Specifies the password that authenticates the connection to the remote device  |
| ``ansible_become`` | no       | yes, no\*   | Instructs the module to enter privileged mode on the remote device before sending any commands; if value is unspecified, the `ANSIBLE_BECOME` environment variable value is used, and the device attempts to execute all commands in non-privileged mode |
| ``ansible_become_method`` | no       | enable, sudo\*   | Instructs the module to allow the become method to be specified for handling privilege escalation; if value is unspecified, the `ANSIBLE_BECOME_METHOD` environment variable value is used |
| ``ansible_become_pass`` | no       |            | Specifies the password to use if required to enter privileged mode on the remote device; if ``ansible_become`` is set to no this key is not applicable |
| ``ansible_network_os`` | yes      | os10, null\*  | Loads the correct terminal and cliconf plugins to communicate with the remote device |

> **NOTE**: Asterisk (*) denotes the default value if none is specified.


Example playbook
----------------

This example uses the *os10_aaa* role to configure AAA for radius and TACACS servers. It creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the `ansible_network_os` variable with the corresponding Dell EMC OS10 name.

When `os10_cfg_generate` is set to true, the variable generates the configuration commands as a .part file in the *build_dir* path. By default, it is set to false and it writes a simple playbook that only references the *os10_aaa* role.

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

    os10_aaa:
      radius_server:
            retransmit: 5
            timeout: 10
            host:
              - ip: 2001:4898:f0:f09b::1001
                key: 0
                value: "abc"
                auth_port: 3
            state: present
      tacacs_server:
            host:
              - ip: 2001:4898:f0:f09b::1001
                key: 0
                value: "abc"
                auth_port: 3
            state: present
            timeout: 6
      aaa_authentication:
            login:
              - console: true
                type: group radius group tacacs+ local
                state: present
            re_authenticate: true
      aaa_accounting:
            accounting:
              - accounting_type: commands
                connection_type: console
                account_mode: start-stop
                server_group: group tacacs+
                state: present

**Simple playbook to setup system — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_aaa

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.
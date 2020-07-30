ACL flow-based monitor role
===========================

This role facilitates configuring ACL flow-based monitoring attributes. Flow-based mirroring is a mirroring session in which traffic matches specified policies that are mirrored to a destination port. Port-based mirroring maintains a database that contains all monitoring sessions (including port monitor sessions). This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The ACL flow-based role requires an SSH connection for connectivity to a Dell EMC OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take the `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable 
- Setting an empty value for any variable negates the corresponding configuration
- `os10_flow_monitor` (dictionary) with session ID key (in *session <ID>* format; 1 to 18)
- Variables and values are case-sensitive

**session ID keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``session_type``  | string: local_*_,rspan-source,erspan-source      | Configures the monitoring session type            | os10 |
| ``description`` | string | Configures the monitor session description | os10 |
| ``port_match`` | list | Displays a list of interfaces with location source and destination | os10 |
| ``port_match.interface_name``     | string | Configures the interface | os10 |
| ``port_match.location`` | string: source,destination | Configures the source/destination of an interface | os10 |
| ``port_match.state``  | string: absent,present\*           | Deletes the interface if set to absent | os10 |
| ``flow_based`` | boolean | Enables flow-based monitoring | os10 |
| ``shutdown`` | string: up,down\* | Enable/disables the monitoring session | os10 |
| ``state``  | string: absent,present\*           | Deletes the monitoring session corresponding to the session ID if set to absent | os10 |
                                                                                                      
> **NOTE**: Asterisk (\*) denotes the default value if none is specified.

Connection variables
--------------------

Ansible Dell EMC network roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories or inventory or in the playbook itself.

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

This example uses the *os10_flow_monitor* role to configure session monitor configuration. It creates a *hosts* file with the switch details and corresponding variables. The hosts file defines the `anisble_network_os` variable with corresponding Dell EMC OS10 name. 

When `os10_cfg_generate` is set to true, the variable generates the configuration commands as a .part file in the *build_dir* path. By default, the variable is set to false.
It writes a simple playbook that only references the *os10_flow_monitor* role.

**Sample hosts file**

    leaf1 ansible_host= <ip_address> 

**Sample host_vars/leaf1**

    hostname: leaf1
    ansible_ssh_user: xxxxx
    ansible_ssh_pass: xxxxx
    ansible_network_os: dellemc.os10.os10
    build_dir: ../temp/os10
    os10_flow_monitor:
      session 1:
        session_type: local
        description: "Discription goes here"
        port_match:
          - interface_name: ethernet 1/1/4
            location: source
            state: present
          - interface_name: ethernet 1/1/3
            location: destination
            state: present
        flow_based: true
        shutdown: up
        state: present
      session 2:
        session_type: local
        description: "Discription of session goes here"
        port_match:
          - interface_name: ethernet 1/1/6
            location: source
            state: present
          - interface_name: ethernet 1/1/7
            location: destination
            state: present
        flow_based: true
        shutdown: up
        state: present
      session 3:
        state: absent
    os10_acl:
	  - name: testflow
	    type: ipv4
            description: testflow description
	    extended: true
            entries:
                - number: 5
                    permit: true
                    protocol: icmp
                    source: any
                    destination: any
                    other_options: capture session 1 count
                    state: present
                - number: 10
                    permit: true
                    protocol: ip
                    source: 102.1.1.0/24
                    destination: any
                    other_option: capture session 1 count byte
                    state: present
                - number: 15
                    permit: false
                    protocol: udp
                    source: any
                    destination: any
                    other_options: capture session 2 count byte
                    state: present
                - number: 20
                    permit: false
                    protocol: tcp
                    source: any
                    destination: any
                    other_options: capture session 2 count byte
                    state: present
                stage_ingress:
                - name: ethernet 1/1/1
                    state: present

> **NOTE**: Destination port should not be an L2/L3 port which can be configured using the *os10_interface* role.

**Simple playbook to setup system — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_flow_monitor
         - dellemc.os10.os10_acl
                
**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.
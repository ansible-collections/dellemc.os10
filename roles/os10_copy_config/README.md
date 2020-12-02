Copy-config role
================

This role is used to push the backup running configuration into a Dell EMC PowerSwitch platform running Dell EMC SmartFabric OS10, and merges the configuration in the template file with the running configuration of the device.

The copy-config role requires an SSH connection for connectivity to a Dell EMC SmartFabric OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- No predefined variables are part of this role
- Use *host_vars* or *group_vars* as part of the template file
- Configuration file is host-specific
- Copy the host-specific configuration to the respective file under the template directory in *<host_name>.j2* format
- Variables and values are case-sensitive

Connection variables
--------------------

Ansible Dell EMC network roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories, or in the playbook itself.

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

> **NOTE**: Asterisk (\*) denotes the default value if none is specified.


Example playbook
----------------

This example uses the *os10_copy_config* role to push the configuration file into the device. It creates a *hosts* file with the switch details and corresponding variables. It writes a simple playbook that only references the *os10_copy_config* role. By including the role, you automatically get access to all of the tasks to push configuration file.

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

    # This variable shall be applied in the below jinja template for each host by defining here
    os10_bgp
       asn: 64801

**Sample roles/os10_copy_config/templates/leaf1.j2**

    ! Leaf1 BGP profile on Dell OS10 switch
    snmp-server community public ro
    hash-algorithm ecmp crc
    !
    interface ethernet1/1/1:1
     no switchport
     ip address 100.1.1.2/24
     ipv6 address 2001:100:1:1::2/64
     mtu 9216
     no shutdown
    !
    interface ethernet1/1/9:1
     no switchport
     ip address 100.2.1.2/24
     ipv6 address 2001:100:2:1::2/64
     mtu 9216
     no shutdown
    !
    router bgp {{ os10_bgp.asn }}
     bestpath as-path multipath-relax
     bestpath med missing-as-worst
     router-id 100.0.2.1
     !
     address-family ipv4 unicast
     !
     address-family ipv6 unicast
     !
     neighbor 100.1.1.1
      remote-as 64901
      no shutdown
     !
     neighbor 100.2.1.1
      remote-as 64901
      no shutdown
     !
     neighbor 2001:100:1:1::1
      remote-as 64901
      no shutdown
      !
      address-family ipv4 unicast
       no activate
       exit
      !
      address-family ipv6 unicast
       activate
       exit
     !
     neighbor 2001:100:2:1::1
      remote-as 64901
      no shutdown
      !
      address-family ipv4 unicast
       no activate
       exit
      !
      address-family ipv6 unicast
       activate
       exit
     !

**Simple playbook to setup to push configuration file into device — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_copy_config

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.
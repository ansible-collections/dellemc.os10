Image upgrade role
===================================

This role facilitates upgrades or installation of a software image. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The Image upgrade role requires an SSH connection for connectivity to a Dell EMC OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os10_image_upgrade keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``operation_type``   | string: cancel,install | Displays the type of image operation | os10 |
| ``software_image_url`` | string          | Configures the URL path to the image file | os10 |
| ``software_version`` | string         | Displays the software version of the image file | os10 |
| ``number_of_retries`` | int         | Configures the numbe of retries to check the status of image install process | os10 |

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

This example uses the *os10_image_upgrade* role to upgrade/install software image. It creates a *hosts* file with the switch details, corresponding *host_vars* file, and a simple playbook that references the *os10_image_upgrade* role.

**Sample hosts file**

    leaf1 ansible_host= <ip_address> 

**Sample host_vars/leaf1**

    hostname: leaf1
    ansible_ssh_user: xxxxx
    ansible_ssh_pass: xxxxx
    ansible_network_os: dellemc.os10.os10
    os10_image_upgrade:
      operation_type: install
      software_image_url: tftp://10.16.148.8/PKGS_OS10-Enterprise-10.2.9999E.5790-installer-x86_64.bin
      software_version: 10.2.9999E
      number_of_retries: 50

**Simple playbook to setup system — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_image_upgrade
                
**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

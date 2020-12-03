Template role
==============

This role provides access to structured data from show commands.  This role facilitates the TEXTFSM parsing engine. TextFSM is a template based state machine . It takes the raw string input from the CLI of network devices, run them through a TEXTFSM template and return structured text in the form of a Python dictionary. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The Template role is highly customizable, and it works with separate template definitions which contain variables and rules with regular expressions. This library is very helpful to parse any text-based CLI output from network devices. The Template role requires an SSH connection for connectivity to a Dell EMC SmartFabric OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- Variables and values are case-sensitive

Connection variables
--------------------

Ansible Dell EMC network roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories or inventory, or in the playbook  itself.

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

This example uses the *os10_template* role to parse any text-based CLI output. It creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the `ansible_network_os` variable with corresponding Dell EMC OS10 name. All the supported CLI commands are imported as tasks in tasks/main.yml.
 
For the *os10_template* role plugins to be used, you may need to specify the actual path of role in *ansible.cfg* file. 

**Sample ansible.cfg**

    action_plugins      = ../../plugins/modules/


**Sample hosts file**

    leaf1 ansible_host= <ip_address> ansible_network_os=dellemc.os10.os10 ansible_ssh_user=xxxxx ansible_ssh_pass=xxxxx


**Simple playbook to setup system — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_template

**Example playbook to run specific show command — leaf.yaml**


    ---
    - name: PARSE SHOW IP INTERFACE BRIEF
      hosts: leaf1
      collections:
        - dellemc.os10
      tasks:
        - import_role:
            name: os10_template
            tasks_from: show_ip_interface_brief.yaml
 


**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

LLDP role
=========

This role facilitates the configuration of link layer discovery protocol (LLDP) attributes at a global and interface level. It supports the configuration of hello, mode, multiplier, advertise TLVs, management interface, FCoE, and iSCSI at global and interface level. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The LLDP role requires an SSH connection for connectivity to a Dell EMC OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os10_lldp keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``enable``  | boolean         | Enables or disables LLDP at a global level | os10 |
| ``multiplier`` | integer | Configures the global LLDP multiplier (2 to 10) | os10 |
| ``reinit`` | integer | Configures the reinit value (1 to 10) | os10 |
| ``timer`` | integer | Configures the timer value (5 to 254) | os10 |
| ``advertise`` | dictionary     | Configures LLDP-MED and TLV advertisement at the global level (see ``advertise.*``) | os10 |
| ``advertise.med`` | dictionary     | Configures MED TLVs advertisement (see ``med_tlv.*``) | os10 |
| ``med.fast_start_repeat_count`` | integer | Configures med fast start repeat count value (1 to 10) | os10 |
| ``med.application`` | list     | Configures global MED TLVs advertisement for an application (see ``application.*``) | os10 |
| ``application.name`` | string     | Configures the application name for MED TLVs advertisement | os10 |
| ``application.vlan_id`` | integer     | Configures the VLAN ID for the application MED TLVs advertisement (1 to 4094) | os10 |
| ``application.l2_priority`` | integer     | Configures the L2 priority for the application MED TLVs advertisement (0 to 7) | os10 | 
| ``application.code_point_value`` | integer     | Configures differentiated services code point values for MED TLVs advertisement (0 to 63) | os10 |
| ``application.vlan_type`` | string: tag, untag | Configures the VLAN type for the application MED TLvs advertisement | os10 |
| ``application.network_policy_id`` | integer | Configures network policy ID for the application MED TLVs advertisement | os10 | 
| ``application.state`` | string: present\*,absent | Deletes the application if set to absent | os10 |
| ``local_interface`` | dictionary     | Configures LLDP at the interface level (see ``local_interface.*``) | os10 |
| ``local_interface.<interface name>`` | dictionary     | Configures LLDP at the interface level (see ``<interface name>.*``)     | os10 |
| ``<interface name>.mode``  | string: rx,tx   | Configures LLDP mode configuration at the interface level | os10 |
| ``<interface name>.mode_state`` | string: absent,present   | Configures transmit/receive at the interface level| os10 |
| ``<interface name>.advertise`` | dictionary     | Configures LLDP-MED TLV advertisement at the interface level (see ``advertise.*``)     | os10 |
| ``advertise.med`` | dictionary     | Configures MED TLVs advertisement at the interface level (see ``med_tlv.*``) | os10 |
| ``med.enable`` | boolean     | Enables interface level MED capabilities | os10 |
| ``med.tlv`` | string | Configures MED TLV advertisement at interface level | os10 |
| ``med.tlv_state`` | string: present\*,absent | Deletes the interface level MED configuration if set to absent | os10 |
| ``med.application`` | list     | Configures MED TLVs advertisement for the application at the interface level (see ``application.*``) | os10 |
| ``application.network_policy_id`` | integer    | Configures the *network_policy_id* for the application of MED | os10 |
| ``application.state`` | string: present\*,absent | Deletes the associated network policy ID for the application if set to absent.| os10 |
| ``advertise.tlv`` | list    | Configures TLVs advertisement at interface level (see `<interface_name>.tlv.*`) | os10 |
| ``tlv.name`` | string: basic-tlv,dcbxp,dcbxp-appln,dot1-tlv,dot3-tlv  | Configures corresponding to the TLV name specified at the interface | os10 |
| ``tlv.value`` | string     | Specifies corresponding TLV value according to the name as a string | os10 |
| ``tlv.state`` | string: present\*,absent   | Deletes the interface level TLVs advertisement if set to absent | os10 |


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

> **NOTE**: Asterisk (\*) denotes the default value if none is specified.


Example playbook
----------------

This example uses the *os10_lldp* role to configure protocol lldp. It creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the `ansible_network_os` variable with corresponding Dell EMC OS10 name. 

When `os10_cfg_generate` is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, the variable is set to false. It writes a simple playbook that only references the *os10_lldp* role.
 
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
    os10_lldp:
      enable: false
      multiplier: 3
      reinit: 2
      timer: 5
      advertise:
        med:
          fast_start_repeat_count: 4
          application:
            - name: guest-voice
              network_policy_id: 0
              vlan_id: 2
              vlan_type: tag
              l2_priority: 3
              code_point_value: 4
              state: present
            - name: voice
              network_policy_id: 1
              vlan_id: 3
              vlan_type: untag
              l2_priority: 3
              code_point_value: 4
              state: absent
      local_interface:
        ethernet 1/1/1:
          mode: rx
          mode_state: present
          advertise:
            med:
              enable: true
              tlv: inventory
              tlv_state: present
              application:
                - network_policy_id: 4
                  state: present
            tlv:
              - name: basic-tlv
                value: management-address port-description
                state: present
              - name: dcbxp-appln
                value: iscsi
                state: present
              - name: dcbxp
                state: present

**Simple playbook to setup system — leaf.yaml**

    - hosts: leaf1
      roles:
         - dellemc.os10.os10_lldp

**Run**

    ansible-playbook -i hosts leaf.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

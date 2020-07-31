# xSTP role

This role facilitates the configuration of xSTP attributes. It supports multiple version of spanning-tree protocol (STP), rapid spanning-tree (RSTP), rapid per-VLAN spanning-tree (Rapid PVST+), multiple spanning-tree (MST), and per-VLAN spanning-tree (PVST). It supports the configuration of bridge priority, enabling and disabling spanning-tree, creating and deleting instances, and mapping virtual LAN (VLAN) to instances. This role is abstracted for Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10.

The xSTP role requires an SSH connection for connectivity to a Dell EMC OS10 device. You can use any of the built-in OS connection variables.

Role variables
--------------

- Role is abstracted using the `ansible_network_os` variable that can take `dellemc.os10.os10` as the value
- If `os10_cfg_generate` is set to true, the variable generates the role configuration commands in a file
- `os10_xstp` (dictionary) contains the hostname (dictionary)
- Hostname is the value of the *hostname* variable that corresponds to the name of the device
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value to any variable negates the corresponding configuration
- Variables and values are case-sensitive

**hostname keys**

| Key        | Type                      | Description                                             | Support              |
|------------|---------------------------|---------------------------------------------------------|----------------------|
| ``type``       | string (required) | Configures the type of spanning-tree mode specified that can vary according to the device including RSTP, rapid-PVST, and MST | os10 |
| ``enable``  | boolean: true,false             | Enables/disables the spanning-tree protocol specified in the type variable | os10 |
| ``mac_flush_timer`` | integer | Configures the mac_flush_timer value (0 to 500) | os10 |
| ``rstp``  | dictionary             | Configures rapid spanning-tree (see ``rstp.*``)  | os10 |
| ``rstp.bridge_priority`` | integer | Configures bridge-priority for the spanning-tree (0 to 61440 in multiples of 4096) | os10 |
| ``rstp.max_age`` | integer  | Configures the max_age timer for RSTP (6 to 40) | os10 |
| ``rstp.hello_time`` | integer | Configures the hello-time for RSTP (1 to 10) | os10 |
| ``rstp.forward_time`` | integer | Configures the forward-time for RSTP (4 to 30) | os10 |
| ``rstp.force_version`` | string: stp | Configures the force version for the BPDUs transmitted by RSTP | os10 |
| ``rstp.mac_flush_threshold`` | integer | Configures the MAC flush threshold for RSTP (1 to 65535) | os10 |
| ``pvst``  | dictionary     | Configures per-VLAN spanning-tree protocol (see ``pvst.*``) | os10 |
| ``pvst.vlan`` | list | Configures the VLAN for PVST (see ``vlan.*``)  | os10 |
| ``vlan.range_or_id``  | string             | Configures a VLAN/range of VLANs for the per-VLAN spanning-tree protocol | os10 |
| ``vlan.max_age`` | integer  | Configures the max_age timer for a VLAN (6 to 40) | os10 |
| ``vlan.hello_time`` | integer | Configures the hello-time for a VLAN (1 to 10) | os10 |
| ``vlan.forward_time`` | integer | Configures the forward-time for a VLAN (4 to 30) | os10 |
| ``vlan.enable`` | boolean: true,false | Enables/disables spanning-tree for the associated VLAN range_or_id | os10 |
| ``vlan.mac_flush_threshold`` | integer | Configures the MAC flush threshold for a VLAN (1 to 65535) | os10 |
| ``vlan.root`` | string: primary,secondary | Designates the primary or secondary root for the associated VLAN range_or_id; mutually exclusive with *vlan.bridge_priority* | os10 |
| ``vlan.bridge_priority`` | integer | Configures bridge-priority for the per-VLAN spanning-tree (0 to 61440 in multiples of 4096); mutually exclusive with *vlan.root* | os10 |
| ``mstp``  | dictionary     | Configures multiple spanning-tree protocol (see ``mstp.*``)  | os10 |
| ``mstp.max_age`` | integer  | Configures the max_age timer for MSTP (6 to 40) | os10 |
| ``mstp.max_hops`` | integer | Configures the max-hops for MSTP (6 to 40) | os10 |
| ``mstp.hello_time`` | integer | Configures the hello-time for MSTP (1 to 10) | os10 |
| ``mstp.forward_time`` | integer | Configures the forward-time for MSTP (4 to 30) | os10 |
| ``mstp.force_version`` | string: stp,rstp | Configures the force-version for the BPDUs transmitted by MSTP | os10 |
| ``mstp.mstp_instances`` | list | Configures a MSTP instance (see ``mstp_instances.*``)  | os10 |
| ``mstp_instances.number_or_range``     | integer                   | Configures the multiple spanning-tree instance number| os10 |
| ``mstp_instances.bridge_priority`` | integer | Configures the bridge-priority for the spanning-tree (0 to 61440 in multiples of 4096); mutually exclusive with *mstp_instances.root* | os10 |
| ``mstp_instances.enable`` | boolean: true,false | Enables/disables spanning-tree for the associated MSTP instance | os10 |
| ``mstp_instances.mac_flush_threshold`` | integer | Configures the MAC flush-threshold for an MSTP instance (1 to 65535) | os10 |
| ``mstp_instances.root`` | string: primary,secondary | Designates the primary or secondary root for the associated MSTP instance; mutually exclusive with *mstp_instances.bridge_priority* | os10 |
| ``mstp.mst_config`` | dictionary | Configures multiple spanning-tree (see ``mstp.mst_config.*``); supported | os10 |
| ``mst_config.name`` | string | Configures the name which is specified for the MSTP | os10 |
| ``mst_config.revision`` | integer | Configures the revision number for MSTP | os10 |
| ``mst_config.cfg_list`` | list | Configures the multiple spanning-tree list (see ``mst_config.cfg_list.*``) | os10 |
| ``cfg_list.number`` | integer | Specifies the MSTP instance number | os10 |
| ``cfg_list.vlans``      | string     | Configures a VLAN/range of VLANs by mapping it to an instance number | os10 |
| ``cfg_list.vlans_state`` | string: absent,present\* | Deletes a set of VLANs mapped to the spanning-tree instance if set to absent | os10 |
| ``intf`` | list | Configures multiple spanning-tree in an interface (see ``intf.*``)  | os10 |
| ``intf <interface name>``| dictionary | Configures the interface name (see ``intf.<interface name>.*``) | os10 |
| ``intf.<interface name>.edge_port`` | boolean: true,false | Configures the EdgePort as dynamic if set to true | os10 |
| ``intf.<interface name>.bpdu_filter``| boolean: true,false | Enables/disables bpdufilter at the interface | os10 |
| ``intf.<interface name>.bpdu_guard``| boolean: true,false | Enables/disables bpduguard at the interface | os10 |
| ``intf.<interface name>.guard``| string: loop,root,none | Configures guard on the interface | os10 |
| ``intf.<interface name>.enable`` | boolean: true,false | Enables/disables spanning-tree at the interface level  | os10 |
| ``intf.<interface name>.link_type``| string: auto,point-to-point,shared | Configures the link type at the interface | os10 |
| ``intf.<interface name>.rstp`` | dictionary | Configures the RSTP interface name (see ``intf.<interface name>.rstp.*``) | os10 |
| ``rstp.priority``| integer | Configures the RSTP priority value at the interface | os10 |
| ``rstp.cost`` | integer | Configures the RSTP cost value at the interface | os10 |
| ``intf.<interface name>.msti`` | list | Configures the MSTi interface name (see ``intf.<interface name>.msti``) | os10 |
| ``msti.instance_number`` | integer or range | Specifies the MSTP instance number or range | os10 |
| ``msti.priority`` | integer | Specifies the priority value to be configured at the interface | os10 |
| ``msti.cost`` | integer | Specifies the cost value to be configured at the interface | os10 |
| ``intf.<interface name>.vlan`` | list | Configures the VLAN interface name (see ``intf.<interface name>.vlan``)  | os10 |
| ``vlan.range_or_id`` | integer or range | Specifies the VLAN ID or range | os10 |
| ``vlan.priority`` | integer | Specifies the priority value to be configured at the interface | os10 |
| ``vlan.cost`` | integer | Specifies the cost value to be configured at the interface | os10 |

> **NOTE**: Asterisk (_*_) denotes the default value if none is specified.

Connection variables
--------------------

Ansible Dell EMC network roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories or inventory or in the playbook itself.

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

> **NOTE**: Asterisk (\*) denotes the default value if none is specified.


Example playbook
----------------

This example uses the *os10_xstp* role to configure different variants of spanning-tree. Based on the type of STP and defined objects, VLANs are associated and bridge priorities are assigned. It creates a *hosts* file with the switch details, and a *host_vars* file with connection variables. The corresponding role variables are defined in the *vars/main.yml* file at the role path. 

It writes a simple playbook that only references the *os10_xstp* role. By including the role, you automatically get access to all of the tasks to configure xSTP. 

**Sample hosts file**

    spine1 ansible_host= <ip_address>

**Sample host_vars/spine1**
    
    hostname: spine1
    ansible_become: yes
    ansible_become_method: xxxxx
    ansible_become_pass: xxxxx
    ansible_ssh_user: xxxxx
    ansible_ssh_pass: xxxxx
    ansible_network_os: dellemc.os10.os10
    build_dir: ../temp/temp_os10

**Sample vars/main.yml**

     os10_xstp:
        type: rstp
        enable: true
        path_cost: true
        mac_flush_timer: 4
        rstp:
          max_age: 6
          hello_time: 7
          forward_time: 7
          force_version: stp
          bridge_priority: 4096
          mac_flush_threshold: 5
        pvst:
          vlan:
            - range_or_id: 10
              max_age: 6
              enable: true
              hello_time: 7
              forward_time: 7
              bridge_priority: 4096
              mac_flush_threshold: 9
        mstp:
          max_age: 6
          max_hops: 6
          hello_time: 7
          forward_time: 7
          force_version: stp
          mstp_instances:
            - number_or_range: 1
              enable: true
              mac_flush_threshold: 9
              bridge_priority: 4096
          mst_config:
             name: cfg1
             revision: 5
             cfg_list:
               - number: 1
                 vlans: 10,12
                 vlans_state: present
        intf:
          ethernet 1/1/8:
            edge_port: true
            bpdu_filter: true
            bpdu_guard: true
            guard: loop
            enable: true
            link_type: point-to-point
            msti:
              - instance_number: 1
                priority: 32
                cost: 1
            rstp:
                priority: 32
                cost: 7
            vlan:
                - range_or_id: 6
                priority: 16
                cost: 8


**Simple playbook to setup system — spine.yml**

    - hosts: spine
      roles:
         - dellemc.os10.os10_xstp
 
**Run**

    ansible-playbook -i hosts spine.yml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

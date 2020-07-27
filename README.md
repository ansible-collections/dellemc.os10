# Ansible Network Collection for Dell EMC SmartFabric OS10

This collection includes Ansible modules, plugins and roles required to work on Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10. Sample playbooks and documentation are also included to show how the collection can be used.

### Ansible modules

- **os10_command.py** — Run commands on devices running SmartFabric OS10

- **os10_config.py** — Manage configuration on devices running SmartFabric OS10
  
- **os10_facts.py** — Collect facts from devices running SmartFabric OS10

### Ansible roles
Roles facilitate provisioning of devices running SmartFabric OS10. These roles explain how to use SmartFabric OS10 and include *os10_acl*, *os10_bgp*, *os10_vxlan*, and so on. There are over 30 roles available. The documentation for each role is at [OS10 roles](https://github.com/ansible-collections/dellemc.os10/blob/master/docs/roles.rst).

### Playbooks

- [CLOS fabric](https://github.com/ansible-collections/dellemc.os10/blob/master/playbooks/clos_fabric_ebgp/README.md) — Example playbook to build CLOS fabric with SmartFabric OS10 switches

- [VXLAN EVPN](https://github.com/ansible-collections/dellemc.os10/blob/master/playbooks/vxlan_evpn/README.md) — Example playbook to build a Leaf-Spine topology with SmartFabric OS10 switches, using VxLAN Symmetric-IRB configuration model

## Installation
Use this command to install the latest version of the OS10 collection from Ansible Galaxy.

    ansible-galaxy collection install dellemc.os10

To install a specific version, a version range identifier must be specified. For example, to install the most recent version that is greater than or equal to 1.0.0 and less than 2.0.0.

    ansible-galaxy collection install 'dellemc.os10:>=1.0.0,<2.0.0'

## Version compatibility
Ansible version 2.10 or later.

> **NOTE**: For Ansible version lower than 2.10, use [dellos10 modules](https://ansible-dellos-docs.readthedocs.io/en/latest/modules.html#os10-modules) and [dellos roles](https://ansible-dellos-docs.readthedocs.io/en/latest/roles.html).

## Sample playbook

    - hosts: os10_sw1
      connection: network_cli
      collections:
        - dellemc.os10
      roles:
        - os10_vlan

**Sample host_vars/os10_sw1.yaml**

    hostname: os10_sw1
    # parameters for connection type network_cli
    ansible_ssh_user: xxxx
    ansible_ssh_pass: xxxx
    ansible_network_os: dellemc.os10.os10

    # Create vlan100 and delete vlan888
    os10_vlan:
        vlan 100:
          description: "Blue"
          state: present
        vlan 888:
          state: absent

**Sample inventory.yaml**

    [os10]
    os10_sw1 ansible_host=100.104.28.119


(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

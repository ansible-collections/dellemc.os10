# Ansible Network Collection for Dell EMC SmartFabric OS10

### Collection contents
This collection includes Ansible modules, plugins and roles needed to provision and manage Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10. Sample playbooks and documentation are also included to show how the collection can be used.

### Collection core modules

- **os10_command.py** — Run commands on devices running OS10

- **os10_config.py** — Manage configuration on devices running OS10
  
- **os10_facts.py** — Collect facts from devices running OS10

### Collection roles
These roles facilitate the provisioning and administration of devices running SmartFabric OS10. There are over 30 roles available that provide a comprehensive coverage of most OS10 resources, including *os10_interface*, *os10_acl*, *os10_bgp*, and *os10_vxlan*. The documentation for each role is at [OS10 roles](https://github.com/ansible-collections/dellemc.os10/blob/master/docs/roles.rst).

### Sample use case playbooks
This collection includes the following sample playbooks that illustrate end to end use cases:

- [CLOS fabric](https://github.com/ansible-collections/dellemc.os10/blob/master/playbooks/clos_fabric_ebgp/README.md) — Example playbook to build a Layer 3 Leaf-Spine fabric

- [VXLAN EVPN](https://github.com/ansible-collections/dellemc.os10/blob/master/playbooks/vxlan_evpn/README.md) — Example playbook to build a scale-out Leaf-Spine topology using VxLAN, BGP EVPN and Symmetric-IRB

## Installation
Use this command to install the latest version of the OS10 collection from Ansible Galaxy:

    ansible-galaxy collection install dellemc.os10

To install a specific version, a version range identifier must be specified. For example, to install the most recent version that is greater than or equal to 1.0.0 and less than 2.0.0.

    ansible-galaxy collection install 'dellemc.os10:>=1.0.0,<2.0.0'

## Version compatibility
* Ansible version 2.10 or later.
* Python 2.7 or higher and Python 3.5 or higher

> **NOTE**: For Ansible versions lower than 2.10, use the legacy [dellos10 modules](https://ansible-dellos-docs.readthedocs.io/en/latest/modules.html#os10-modules) and [dellos roles](https://ansible-dellos-docs.readthedocs.io/en/latest/roles.html).

## Sample playbook

**playbook.yaml**

    - hosts: os10_switches
      connection: network_cli
      collections:
        - dellemc.os10
      roles:
        - os10_vlan

**host_vars/os10_sw1.yaml**

    hostname: os10_sw1
    # Parameters for connection type network_cli
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

**inventory.yaml**

    [os10_sw1]
    os10_sw1 ansible_host=100.104.28.119

    [os10_sw2]
    os10_sw2 ansible_host=100.104.28.120

    [os10_switches:children]
    os10_sw1
    os10_sw2


(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

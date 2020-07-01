# Ansible Network Collection for Dell EMC SmartFabric OS10

## Collection contents
This collection includes Ansible modules, plugins and roles required to work on Dell EMC PowerSwitch platforms running SmartFabric OS10. Sample playbooks and documentation are also included to show how the collection can be used.

### Ansible modules

- **os10_command.py** — Run commands on devices running Dell EMC SmartFabric OS10

- **os10_config.py** — Manage configuration on devices running Dell EMC SmartFabric OS10
  
- **os10_facts.py** — Collect facts from devices running Dell EMC SmartFabric OS10

### Ansible roles
Roles facilitate provisioning of devices running Dell EMC SmartFabric OS10. These roles explain how to use SmartFabric OS10 and include os10_acl, os10_bgp, os10_vxlan, and so on. The documentation for each role is at [OS10 roles documentation](https://github.com/ansible-collections/dellemc.os10/blob/master/docs/roles.rst)

### Playbooks
Sample playbooks are included for provisioning devices running Dell EMC SmartFabric OS10.

## Installation
Use this command to install the latest version of OS10 collection from Ansible Galaxy:

    ansible-galaxy collection install dellemc.os10

To install a specific version, a version range identifier must be specified. For example, to install the most recent version that is greater than or equal to 1.0.0 and less than 2.0.0:

    ansible-galaxy collection install 'dellemc.os10:>=1.0.0,<2.0.0'

## Sample playbook

    - hosts: os10_sw1
      connection: network_cli
      collections:
        - dellemc.os10
      roles:
        - os10_vlan

> **NOTE**: When using Ansible 2.9, the ANSIBLE_NETWORK_GROUP_MODULES environment variable should be set to 'os10' to use the os10-collections in the playbook.

>           export ANSIBLE_NETWORK_GROUP_MODULES=os10

## Sample host_vars/os10_sw1.yaml

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

## Sample inventory.yaml

    [os10]
    os10_sw1 ansible_host=100.104.28.119


(c) 2020 Dell Inc. or its subsidiaries. All rights reserved.

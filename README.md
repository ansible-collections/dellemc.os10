# Ansible collection for Dell EMC SmartFabric OS10

## Collection contents
The Ansible network collection for Dell EMC SmartFabric OS10 includes Ansible modules, plugins and roles required to work on Dell EMC PowerSwitch platforms running SmartFabric OS10. It also includes sample playbooks and documentation that illustrate how the collection can be used.

### Ansible modules
The following modules are part of this collection:

- **os10_command.py** — Run commands on devices running Dell EMC SmartFabric OS10

- **os10_config.py** — Manage configuration on devices running Dell EMC SmartFabric OS10
  
- **os10_facts.py** — Collect facts from devices running Dell EMC SmartFabric OS10

### Ansible roles
Collection roles facilitate provisioning of devices running Dell EMC SmartFabric OS10. Roles included in the collection cover most of the functionality required to operate OS10, such as os10_acl, os10_bgp, os10_vxlan, and so on. The docs directory in the collection includes documentation for each role.

### Playbooks
The playbooks directory includes sample playbooks that show the usage of the OS10 collection for provisioning
device running Dell EMC SmartFabric OS10.

## Collection installation
Install the latest version of OS10 collection from Ansible Galaxy:

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

> **NOTE**: When using Ansible 2.9, the environment variable ANSIBLE_NETWORK_GROUP_MODULES should be set to 'os10' to use the os10-collections in the playbook.
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

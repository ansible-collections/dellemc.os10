# The Ansible collection for Dell EMC PowerSwitch platforms running SmartFabric OS10

## Collection contents
The OS10 Ansible collection includes the Ansible modules, plugins and roles required to work on a Dell EMC SmartFabric OS10 PowerSwitch. It also includes sample playbooks and documents that illustrate how the collection can be used.

### Ansible modules
The following Ansible modules are part of the OS10 collection:

- **os10_command.py** — Run commands on remote devices running Dell EMC SmartFabric OS10

- **os10_config.py** — Manage configuration sections on remote devices running Dell EMC SmartFabric OS10
  
- **os10_facts.py** — Collect facts from remote devices running Dell EMC SmartFabric OS10

### Ansible roles
The roles facilitate provisioning of device running Dell EMC SmartFabric OS10. Some of the roles included in the collection are os10_aaa , os10_bgp, os10_ecmp, and so on. The docs directory in the collection includes documentation for each of the roles part of the collection.

### Playbooks
The playbooks directory includes sample playbooks that illustrate the usage of OS10 collections for provisioning
device running Dell EMC SmartFabric OS10.

## Collection Installation
Install the latest version of OS10 collection from Ansible Galaxy:

    ansible-galaxy collection install dellemc_networking.os10

To install a specific version, a version range identifier must be specified. For example, to install the most recent version that is greater than or equal to 1.0.0 and less than 2.0.0:

    ansible-galaxy collection install 'dellemc_networking.os10:>=1.0.0,<2.0.0'

## Sample playbook

    - hosts: os10_sw1
      connection: network_cli
      collections:
        - dellemc_networking.os10
      roles:
        - os10_vlan

> **NOTE**: The environment variable ANSIBLE_NETWORK_GROUP_MODULES should be set to 'os10' for using os10-collections in the playbook.

## Sample host_vars/os10_sw1.yaml

    hostname: os10_sw1
    # parameters for connection type network_cli
    ansible_ssh_user: xxxx
    ansible_ssh_pass: xxxx
    ansible_network_os: dellemc_networking.os10.os10

## Sample inventory.yaml

    [os10]
    os10_sw1 ansible_host=100.104.28.119

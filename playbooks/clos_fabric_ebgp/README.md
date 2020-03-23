


# Provision CLOS fabric using the Ansible collection for Dell EMC SmartFabric OS10

This example describes how to use Ansible to build a CLOS fabric with Dell EMC SmartFabric OS10 switches. The sample topology is a two-tier CLOS fabric with two spines and four leaves connected as mesh. eBGP is running between the two tiers. All switches in spine have the same AS number, and each leaf switch has a unique AS number. All AS numbers used are private.

For application load-balancing purposes, the same prefix is advertised from multiple leaf switches and uses  _BGP multipath relax_  feature.

![CLOS FABRIC Topology](https://ansible-dellos-docs.readthedocs.io/en/latest/_images/topo.png)

## Create a simple Ansible playbook

**Step 1**
Create an inventory file called  `inventory.yaml`, then specify the device IP address.

**Step 2**
Create a group variable file called `group_vars/all`, then define credentials and SNMP variables.

**Step 3**
Create a group variable file called  `group_vars/spine.yaml`, then define credentials, hostname, and BGP neighbors of spine group.

**Step 4**
Create a host variable file called  `host_vars/spine1.yaml`, then define the host, credentials, and transport.
Create a host variable file called `host_vars/spine2.yaml`, then define the host, credentials, and transport.

Create a host variable file called `host_vars/leaf1.yaml`, then define the host, credentials, and transport.
Create a host variable file called `host_vars/leaf2.yaml`, then define the host, credentials, and transport.
Create a host variable file called `host_vars/leaf3.yaml`, then define the host, credentials, and transport.
Create a host variable file called `host_vars/leaf4.yaml`, then define the host, credentials, and transport.

**Step 5**
Create a playbook called  `datacenter.yaml`.

**Step 6**
Run the playbook.

`ansible-playbook  -i  inventory.yaml  datacenter.yaml`


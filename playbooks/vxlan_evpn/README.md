
#  VxLAN Symmetric-IRB configuration using BGP EVPN using the Ansible collection for Dell EMC SmartFabric OS10


This example describes how to use Ansible to build a LEAF - SPINE Topology with Dell EMC SmartFabric OS10 switches , using VxLAN Symmetric -IRB configuration Model.
VxLAN Symmetric-IRB is configured using BGP EVPN with Leaf and SPINE topology. BGP unnumbered is configured between Leaf and SPINE over VLANS for both underlay and overlay as well.
VLT is configured between the pair of LEAF nodes.

In all the LEAF nodes L3 VRF VNI "test" is configured to route between different VN's spanned across the topology and VTEP router mac is configured to identify the remote VTEP's.

VN 100 and VN 300 is configured in a pair of LEAF nodes and VN 200 and VN 300 configured in other pair of LEAF nodes.

## Create a simple Ansible playbook

**Step 1**
Create an inventory file called  `inventory.yaml`, then specify the device IP address.

**Step 2**
Create a host variable file called  `host_vars/spine1.yaml`, then define the host, credentials, and transport.
Create a host variable file called `host_vars/spine2.yaml`, then define the host, credentials, and transport.
Use Ansible roles os10_interface and os10_vlan  to configure required VLANs. Use Ansible role os10_bgp to configure BGP Unnumbered.

**Step 3**

***Configurations for VTEP-1***

Create a host variable file called `host_vars/prim-vtep1.yaml`
Create a host variable file called  `host_vars/sec-vtep1.yaml`

Define the host, credentials, and transport.

Use Ansible roles os10_interface and os10_vlan  to configure required VLANs. 
Use Ansible role os10_bgp to configure BGP Unnumbered . 
Use role os10_vxlan to configure VN networks, EVPN and Symmetric IRB functionality. 
Use role os10_vlt to configure VLT between leaves prim-vtep1 and sec-vtep1


**Step 4**

***Configurations for VTEP-2***

Create a host variable file called `host_vars/prim-vtep2.yaml`
Create a host variable file called  `host_vars/sec-vtep2.yaml`

Define the host, credentials, and transport.

Use Ansible roles os10_interface and os10_vlan  to configure required VLANs. 
Use Ansible role os10_bgp to configure BGP Unnumbered. 
Use role os10_vxlan to configure VN networks, EVPN and Symmetric IRB functionality. 
Use role os10_vlt to configure VLT between leaves prim-vtep2 and sec-vtep2

**Step 5**
Create a playbook called  `datacenter.yaml`.

**Step 6**
Run the playbook.

`ansible-playbook  -i  inventory.yaml  datacenter.yaml`

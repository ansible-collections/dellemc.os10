#  VxLAN Symmetric-IRB configuration using BGP EVPN using the Ansible collection for Dell EMC SmartFabric OS10


This example describes how to use Ansible to build a Leaf-Spine topology with Dell EMC PowerSwitch platforms running Dell EMC SmartFabric OS10, using a VxLAN Symmetric-IRB configuration model.

VxLAN Symmetric-IRB is configured using BGP EVPN with Leaf-Spine topology. BGP unnumbered is configured between the Leaf and Spine over VLANS for both underlay and overlay. VLT is configured between the pair of Leaf nodes.

In all Leaf nodes, the L3 VRF VNI "test" is configured to route between different VNs spanned across the topology, and the VTEP router MAC is configured to identify the remote VTEPs.
VN 100 and VN 300 is configured in a pair of Leaf nodes, and VN 200 and VN 300 configured in an other pair of Leaf nodes.

## Create simple Ansible playbook

**1**.  Create an inventory file called  `inventory.yaml`, then specify the device IP address.

**2**.  Create a host variable file called  `host_vars/spine1.yaml`, then define the host, credentials, and transport.

**3**.  Create a host variable file called `host_vars/spine2.yaml`, then define the host, credentials, and transport.

**4**.  Use the *os10_interface* and *os10_vlan* roles to configure the required VLANs.

**5**.  Use the *os10_bgp* role to configure BGP unnumbered.

**Configurations for VTEP-1**

**1**.  Create a host variable file called `host_vars/prim-vtep1.yaml`.

**2**.  Create a host variable file called  `host_vars/sec-vtep1.yaml`.

**3**.  Define the host, credentials, and transport.

**4**.  Use the *os10_interface* and *os10_vlan* roles to configure the required VLANs.

**5**.  Use the *os10_bgp* role to configure BGP unnumbered.

**6**.  Use the *os10_vxlan* role to configure VN networks, EVPN and Symmetric IRB functionality.

**7**.  Use *os10_vlt* role to configure VLT between leaves prim-vtep1 and sec-vtep1.

**Configurations for VTEP-2**

**1**.  Create a host variable file called `host_vars/prim-vtep2.yaml`.

**2**.  Create a host variable file called  `host_vars/sec-vtep2.yaml`.

**3**.  Define the host, credentials, and transport.

**4**.  Use *os10_interface* and *os10_vlan* roles to configure the required VLANs. 

**5**.  Use the *os10_bgp* role to configure BGP unnumbered. 

**6**.  Use *os10_vxlan* role to configure VN networks, EVPN and Symmetric IRB functionality. 

**7**.  Use the *os10_vlt* role to configure VLT between leaves prim-vtep2 and sec-vtep2.

**Create and run the playbook**

**1**.  Create a playbook called  `datacenter.yaml`.

**2**.  Run the playbook.

    ansible-playbook  -i  inventory.yaml  datacenter.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.

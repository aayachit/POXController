sudo ovs-ofctl add-flow s2 icmp,nw_dst=10.0.1.0/24,actions=output:2
sudo ovs-ofctl add-flow s2 icmp,nw_dst=10.0.0.0/24,actions=output:1
sudo ovs-ofctl add-flow s2 arp,arp_tpa=10.0.1.0/24,actions=output:2
sudo ovs-ofctl add-flow s2 arp,arp_tpa=10.0.0.0/24,actions=output:1
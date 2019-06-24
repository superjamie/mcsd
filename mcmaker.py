#!/usr/bin/python3

from scapy.all import *

packetcount = 99
packets = PacketList()

if __name__ == "__main__":

    # generate packets into a pcap file, sanitise source MAC/IP
    for i in range(1,packetcount+1):
        payload = f"{i:08d}".encode()
        packet = Ether(src="aa:aa:aa:bb:bb:bb")/IP(src="10.0.0.1",dst="239.0.0.1")/UDP(sport=65535,dport=9001)/Raw(load=payload)
        packets.append(packet)

    wrpcap("mcpackets.pcap", packets)


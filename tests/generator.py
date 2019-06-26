#!/usr/bin/python3

import argparse
from scapy.all import *

packets = PacketList()

if __name__ == "__main__":

    # generate packets into a pcap file, sanitise source MAC/IP
    for i in range(1,21):
        payload = f"{i:08d}".encode()
        if (i % 2 == 1):
            packet = Ether(src="aa:aa:aa:bb:bb:bb")/IP(src="10.0.0.1",dst="239.0.0.1")/UDP(sport=65535,dport=9001)/Raw(load=payload)
        else:
            packet = Ether(src="aa:aa:aa:bb:bb:bb")/IP(src="10.0.0.2",dst="239.0.0.2")/UDP(sport=1111,dport=9999)/Raw(load=payload)
        packets.append(packet)

    wrpcap("mcpackets.pcap", packets)


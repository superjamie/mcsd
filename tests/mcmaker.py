#!/usr/bin/python3

import argparse
from scapy.all import *

packets = PacketList()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help="number of packets to generate", type=int)
    args = parser.parse_args()

    if (args.number):
        packetcount = args.number
    else:
        packetcount = 9

    # generate packets into a pcap file, sanitise source MAC/IP
    for i in range(1,packetcount+1):
        payload = f"{i:08d}".encode()
        packet = Ether(src="aa:aa:aa:bb:bb:bb")/IP(src="10.0.0.1",dst="239.0.0.1")/UDP(sport=65535,dport=9001)/Raw(load=payload)
        packets.append(packet)

    wrpcap("mcpackets.pcap", packets)


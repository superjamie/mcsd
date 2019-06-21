#!/usr/bin/python3

from scapy.all import *
import ipaddress
import os
import sys

if __name__ == "__main__":

    try:
        filename = sys.argv[1]
    except IndexError:
        print("Usage:", os.path.basename(__file__), "[filename]")
        exit(1)

    try:
        pkts = rdpcap(filename)
    except FileNotFoundError:
        print("File not found:", filename)
        exit(1)

    # same to assume all packets are IP packets? probably not
    for pkt in pkts:
        if (IP in pkt) and (ipaddress.ip_address(pkt[IP].dst) in ipaddress.ip_network("224.0.0.0/4")):
                if (UDP in pkt) and (pkt[UDP].len > 0):
                    print(pkt[Raw].load[0:8].decode("utf-8"))

# vim: ft=python


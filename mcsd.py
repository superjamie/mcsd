#!/usr/bin/python3

from scapy.all import *
import argparse
import ipaddress
import os
import sys

pcap_packets = PacketList()  # list of raw packets from the pcap file
filt_packets = PacketList()  # list of packets after filtering

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="pcap filename to read")
    parser.add_argument("-s", "--source", help="filter on source IP address", action="store_true")
    parser.add_argument("-d", "--dest"  , help="filter on destination IP address", action="store_true")
    parser.add_argument("-S", "--sport" , help="filter on source port number", action="store_true")
    parser.add_argument("-D", "--dport" , help="filter on destination port number", action="store_true")
    parser.add_argument("-o", "--offset", help="offset into packet to start reading", action="store_true")
    parser.add_argument("-l", "--length", help="length of characters to read", action="store_true")
    parser.add_argument("-r", "--raw"   , help="raw mode. only print payload data")
    args = parser.parse_args()

    try:
        pcap_packets = rdpcap(args.filename)
    except FileNotFoundError:
        print("File not found:", filename)
        exit(1)

    # filter
    # TODO: filter on src/dst arguments
    for packet in pcap_packets:
        if (IP in packet) and (ipaddress.ip_address(packet[IP].dst) in ipaddress.ip_network("224.0.0.0/4")):
            if (UDP in packet) and (packet[UDP].len > 0):
                filt_packets.append(packet)

    # print header
    # TODO: not in raw mode
    if (len(filt_packets) > 0):
        print("{:10s} {:s}".format("frame no", "payload"))

    # process
    # TODO: read payload using offset and len arguments
    # TODO: don't print framenumber in raw mode
    for packet in filt_packets:
        framenumber = pcap_packets.index(packet)+1
        payload = packet[Raw].load[0:8].decode("utf-8")
        print("{:10d} {:s}".format(framenumber, payload))

# vim: ft=python


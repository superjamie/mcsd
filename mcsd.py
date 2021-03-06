#!/usr/bin/python3

from scapy.all import *
import argparse
import ipaddress

pcap_packets = PacketList()  # list of raw packets from the pcap file
filt_packets = PacketList()  # list of packets after filtering

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="pcap filename to read")
    parser.add_argument("-s", "--source", help="filter on source IP address")
    parser.add_argument("-d", "--dest"  , help="filter on destination IP address")
    parser.add_argument("-S", "--sport" , help="filter on source port number", type=int)
    parser.add_argument("-D", "--dport" , help="filter on destination port number", type=int)
    parser.add_argument("-o", "--offset", help="offset into packet to start reading", default=0, type=int)
    parser.add_argument("-l", "--length", help="length of characters to read", default=8, type=int)
    parser.add_argument("-r", "--raw"   , help="raw mode. only print payload data", action="store_true")
    args = parser.parse_args()

    # validate input
    try:
        pcap_packets = rdpcap(args.filename)
    except FileNotFoundError:
        print("ERROR - File not found:", args.filename)
        exit(1)
    except PermissionError:
        print("ERROR - Permission denied:", args.filename)
        exit(1)

    if (args.source is not None):
        try:
            ipaddress.ip_address(args.source)
        except ValueError:
            print("ERROR - Not a valid source IP address:", args.source)
            exit(1)

    if (args.dest is not None):
        try:
            ipaddress.ip_address(args.dest)
        except ValueError:
            print("ERROR - Not a valid destination IP address:", args.dest)
            exit(1)

    if (args.sport is not None):
        if (args.sport < 1) or (args.sport > 65535):
            print("ERROR - Not a valid source port number:", args.sport)
            exit(1)

    if (args.dport is not None):
        if (args.dport < 1) or (args.dport > 65535):
            print("ERROR - Not a valid destination port number:", args.dport)
            exit(1)

    # filter
    for packet in pcap_packets:
        # check if packet is IP multicast
        if (IP in packet) and (ipaddress.ip_address(packet[IP].dst) in ipaddress.ip_network("224.0.0.0/4") and (UDP in packet) and (packet[UDP].len > 0)):
            # apply any user filters
            if (args.source) and (ipaddress.ip_address(packet[IP].src) != ipaddress.ip_address(args.source)):
                continue
            if (args.dest) and (ipaddress.ip_address(packet[IP].dst) != ipaddress.ip_address(args.dest)):
                continue
            if (args.sport) and (packet[UDP].sport != args.sport):
                continue
            if (args.dport) and (packet[UDP].dport != args.dport):
                continue
            filt_packets.append(packet)

    # process
    if (args.offset is not None):
        offset = args.offset
    else:
        offset = 0

    if (args.length is not None):
        length = args.length
    else:
        length = 8

    if (len(filt_packets) > 0):
        for packet in filt_packets:
            payload = packet[Raw].load.decode("utf-8")[offset:offset+length]
            if (args.raw != True):
                framenumber = pcap_packets.index(packet)+1
                srcip = packet[IP].src
                dstip = packet[IP].dst
                sport = packet[UDP].sport
                dport = packet[UDP].dport
                print("{:>10d} {:>15s} → {:<15s} {:>5d} → {:<5d} {:s}".format(framenumber, srcip, dstip, sport, dport, payload))
            else:
                print(payload)

# vim: ft=python


#!/usr/bin/python3

import socket
import struct
import sys

maddr = ("239.0.0.1", 9001)
pkts = 9

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, struct.pack("b",1))
        for i in range(pkts):
            sock.sendto(f"{i:08d}".encode(), maddr)


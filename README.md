# Multicast Sequence Number Decoder

A scapy script for pulling the sequence number out of a UDP multicast
packet payload. Used for troubleshooting packet captures of
applications which claim to be losing traffic due to missing sequence.

## Usage

~~~
usage: mcsd.py [-h] [-s SOURCE] [-d DEST] [-S SPORT] [-D DPORT] [-o OFFSET]
               [-l LENGTH] [-r]
               filename

positional arguments:
  filename              pcap filename to read

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        filter on source IP address
  -d DEST, --dest DEST  filter on destination IP address
  -S SPORT, --sport SPORT
                        filter on source port number
  -D DPORT, --dport DPORT
                        filter on destination port number
  -o OFFSET, --offset OFFSET
                        offset into packet to start reading
  -l LENGTH, --length LENGTH
                        length of characters to read
  -r, --raw             raw mode. only print payload data
~~~

## Example

~~~
$ ./mcsd.py mcpackets.pcap 
frame no   payload
         1 00000001
         2 00000002
         3 00000003
         4 00000004
         5 00000005
         6 00000006
         7 00000007
         8 00000008
         9 00000009
        10 00000010
        11 00000011
        12 00000012
        13 00000013
        14 00000014
        15 00000015
        16 00000016
        17 00000017
        18 00000018
        19 00000019
        20 00000020
~~~

## Requirements

* Python 3 (tested on v3.6.8)
* scapy (tested on v2.4.2)

## Author

Jamie Bainbridge - jamie.bainbridge@gmail.com

## License

GPLv3 - https://www.gnu.org/licenses/gpl-3.0.en.html


# Multicast Sequence Decoder

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

## Examples

Fields displayed are:

~~~
     frame          src IP → dst IP          sport → dport payload
~~~

A capture file with multiple streams:

~~~
$ mcsd.py mcpackets.pcap 
         1        10.0.0.1 → 239.0.0.1       65535 → 9001  00000001
         2        10.0.0.2 → 239.0.0.2        1111 → 9999  00000002
         3        10.0.0.1 → 239.0.0.1       65535 → 9001  00000003
         4        10.0.0.2 → 239.0.0.2        1111 → 9999  00000004
         5        10.0.0.1 → 239.0.0.1       65535 → 9001  00000005
         6        10.0.0.2 → 239.0.0.2        1111 → 9999  00000006
         7        10.0.0.1 → 239.0.0.1       65535 → 9001  00000007
         8        10.0.0.2 → 239.0.0.2        1111 → 9999  00000008
         9        10.0.0.1 → 239.0.0.1       65535 → 9001  00000009
        10        10.0.0.2 → 239.0.0.2        1111 → 9999  00000010
        11        10.0.0.1 → 239.0.0.1       65535 → 9001  00000011
        12        10.0.0.2 → 239.0.0.2        1111 → 9999  00000012
        13        10.0.0.1 → 239.0.0.1       65535 → 9001  00000013
        14        10.0.0.2 → 239.0.0.2        1111 → 9999  00000014
        15        10.0.0.1 → 239.0.0.1       65535 → 9001  00000015
        16        10.0.0.2 → 239.0.0.2        1111 → 9999  00000016
        17        10.0.0.1 → 239.0.0.1       65535 → 9001  00000017
        18        10.0.0.2 → 239.0.0.2        1111 → 9999  00000018
        19        10.0.0.1 → 239.0.0.1       65535 → 9001  00000019
        20        10.0.0.2 → 239.0.0.2        1111 → 9999  00000020
~~~

Filtering on source IP:

~~~
$ mcsd.py -s 10.0.0.1 mcpackets.pcap 
         1        10.0.0.1 → 239.0.0.1       65535 → 9001  00000001
         3        10.0.0.1 → 239.0.0.1       65535 → 9001  00000003
         5        10.0.0.1 → 239.0.0.1       65535 → 9001  00000005
         7        10.0.0.1 → 239.0.0.1       65535 → 9001  00000007
         9        10.0.0.1 → 239.0.0.1       65535 → 9001  00000009
        11        10.0.0.1 → 239.0.0.1       65535 → 9001  00000011
        13        10.0.0.1 → 239.0.0.1       65535 → 9001  00000013
        15        10.0.0.1 → 239.0.0.1       65535 → 9001  00000015
        17        10.0.0.1 → 239.0.0.1       65535 → 9001  00000017
        19        10.0.0.1 → 239.0.0.1       65535 → 9001  00000019
~~~

Filtering on destination port:

~~~
$ mcsd.py -D 9999 mcpackets.pcap 
         2        10.0.0.2 → 239.0.0.2        1111 → 9999  00000002
         4        10.0.0.2 → 239.0.0.2        1111 → 9999  00000004
         6        10.0.0.2 → 239.0.0.2        1111 → 9999  00000006
         8        10.0.0.2 → 239.0.0.2        1111 → 9999  00000008
        10        10.0.0.2 → 239.0.0.2        1111 → 9999  00000010
        12        10.0.0.2 → 239.0.0.2        1111 → 9999  00000012
        14        10.0.0.2 → 239.0.0.2        1111 → 9999  00000014
        16        10.0.0.2 → 239.0.0.2        1111 → 9999  00000016
        18        10.0.0.2 → 239.0.0.2        1111 → 9999  00000018
        20        10.0.0.2 → 239.0.0.2        1111 → 9999  00000020
~~~

Raw mode, just displaying payload:

~~~
$ mcsd.py -D 9999 -r mcpackets.pcap 
00000002
00000004
00000006
00000008
00000010
00000012
00000014
00000016
00000018
00000020
~~~

Reading further ahead into the packet:

~~~
$ mcsd.py -D 9999 -r -o 4 -l 4 mcpackets.pcap 
0002
0004
0006
0008
0010
0012
0014
0016
0018
0020
~~~

## Analysis

Text processing tools can be used to iterate over printed sequence numbers and identify missing data.

The exact processing depends on the format of the packet data.

An example using `awk` to find missing sequence numbers which don't increase by 1, starting at 1, using the above sample data:

~~~
$ mcsd.py -D 9999 mcpackets.pcap | awk '$NF!=p+1{print p+1"-"$NF-1}{p=$NF}'
1-1
3-3
5-5
7-7
9-9
11-11
13-13
15-15
17-17
19-19
~~~

This output describes that we are missing sequence number 1, 3, 5, and so on.

## Requirements

* Python 3 (tested on v3.6.8)
* scapy (tested on v2.4.2)

## Installation

Put [mcsd.py](https://raw.githubusercontent.com/superjamie/mcsd/master/mcsd.py) somewhere in `$PATH`, eg:

~~~
mkdir -p ~/bin
wget -O ~/bin/mcsd.py https://raw.githubusercontent.com/superjamie/mcsd/master/mcsd.py
chmod +x ~/bin/mcsd.py
~~~

## Author

Jamie Bainbridge - jamie.bainbridge@gmail.com

## License

GPLv3 - https://www.gnu.org/licenses/gpl-3.0.en.html

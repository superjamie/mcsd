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

## Requirements

* Python 3 (tested on v3.6.8)
* scapy (tested on v2.4.2)

## Features

* Takes pcap filename as argument
* Checks if packet is multicast
* Checks if UDP payload exists
* Prints packet number and a fixed substring of UDP payload as text
* "Raw mode" which just prints the packet payload substring

## Todo

* Filter on source/dest addr/port arguments
* Take traffic offset and lenth arguments

## Not Todo

* Any processing of payload data. This tool is used to extract the payload
  sequence number as text only. Process the payload with text manipulation
  tools. This fits with Unix Philosophy of "do one thing and do it well".

## Author

Jamie Bainbridge - jamie.bainbridge@gmail.com

## License

GPLv3 - https://www.gnu.org/licenses/gpl-3.0.en.html

## Testing

* In `tests` directory


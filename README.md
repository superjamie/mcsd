# Multicast Sequence Number Decoder

A scapy script for pulling the sequence number out of a UDP multicast
packet payload. Used for troubleshooting packet captures of
applications which claim to be losing traffic due to missing sequence.

## Usage

    mcsd.py [fiename]

## Requirements

* Python 3 (tested on v3.6.8)
* scapy (tested on v2.4.2)

## Features

* Takes pcap filename as argument
* Checks if packet is multicast
* Checks if UDP payload exists
* Prints a fixed substring of UDP payload as text

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

* Use `mcmaker.py` to generate multicast packets with an 8-digit payload to
  address 239.0.0.1 port 9001
* Capture those packets, like the example `mcpackets.pcap` file
* Read the payload back from the pcap file with the script


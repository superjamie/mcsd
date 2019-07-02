#!/bin/bash

tests=(*.test)
num_tests=${#tests[@]}

#echo "tests = ${tests[@]}."
#echo "num_tests = $num_tests"

./generator.py
if [[ $(tshark -nr mcpackets.pcap -T fields -e frame.number -e ip.src -e ip.dst -e ip.proto -e udp.srcport -e udp.dstport -e udp.length | diff - mcpackets.txt) ]]; then
    echo "ERROR - packet generator not ok"
    exit 1
fi

echo "1..$num_tests"
test_num=0
for test_prog in ${tests[@]}; do
	let test_num++
	if bash $test_prog "$@"; then
		echo "$test_num ok $test_prog $@"
	else
		echo "$test_num not ok $test_prog $@"
	fi
done

if [[ -f mcpackets.pcap ]]; then
    rm -f mcpackets.pcap
fi


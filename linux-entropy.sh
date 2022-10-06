#!/bin/sh
ESTIMATE=/proc/sys/kernel/random/entropy_avail
timeout 3s dd if=/dev/random bs=4k count=1 2> /dev/null | base64
entropy=`cat $ESTIMATE`
while [ $entropy -lt 128 ]
do
	sleep 3
	entropy=`cat $ESTIMATE`
	echo $entropy
done
dd if=/dev/random bs=8 count=1 2> /dev/null | base64
cat $ESTIMATE

#!/usr/bin/bash
server_ip=$1
ping $server_ip -c 2
if [ $? -eq 0 ];
then
	echo "Server is up"
else
	echo "Server is down"
fi

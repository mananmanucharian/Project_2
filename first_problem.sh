#!/bin/bash

 IP=$1
 MAX_TRIES=3

if [ -z "$IP" ]; then
    exit 1
fi

FAILED=$(grep "Failed password" /var/log/auth.log | grep "$IP" | awk '{print $11}' | sort >

if [ "$FAILED" -ge "$MAX_TRIES" ]; then
    iptables -A INPUT -p tcp --dport 22 -s "$IP" -j DROP

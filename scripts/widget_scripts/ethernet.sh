#!/bin/bash

ethernet_status=$(nmcli | grep -i 'enp1s0' | head -n 1 | awk '{ print $2 }')
echo $ethernet_status





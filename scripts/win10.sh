#!/bin/bash

sudo virsh list --all > /dev/null 2>&1
sudo virsh start win10 > /dev/null 2>&1
echo $?
sleep 2
echo "started the vm"
sudo virt-viewer --attach win10


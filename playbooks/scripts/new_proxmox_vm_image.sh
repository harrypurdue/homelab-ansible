#!/bin/bash
## for proxmox server
## https://pve.proxmox.com/wiki/Cloud-Init_Support
## set up the image
## requires configuring cloud-init in the proxmox web gui

if [ -z "$1" -o -z "$2" -o -z "$3"]; then
    echo Invalid arguments
    echo ./new_proxmox_vm_image.sh /path/to/image VMID NAME
    exit 1
fi
set -ex
IMAGE=$1
VMID=$2
NAME=$3

# create a new VM with VirtIO SCSI controller
qm create $VMID --memory 2048 --net0 virtio,bridge=vmbr0 --scsihw virtio-scsi-pci

# import the downloaded disk to the local-lvm storage, attaching it as a SCSI drive
qm set $VMID --scsi0 local-lvm:0,import-from=$1

# increase storage size
qm resize $VMID scsi0 +10G

# name the template
qm set $VMID --name $NAME

qm set $VMID --ide2 local-lvm:cloudinit

qm set $VMID --boot order=scsi0

qm set $VMID --serial0 socket --vga serial0

qm set $VMID --ciuser ansible

qm template $VMID

#!/bin/sh
# passed devices:
#   Laptop touchpad
#   Laptop keyboard
#   USB mouse
#   Laptop touchscreen
# ip address is a virtual bridge device to a guest VM
./main.py --client --ip-address 192.168.122.186 --device --path platform-AMDI0010:00-event-mouse --type pointer --device --path platform-i8042-serio-0-event-kbd --type keyboard --device --path platform-AMDI0010:00-event --type pointer --device --path pci-0000:05:00.4-usb-0:1.2.1:1.0-event-mouse --type pointer

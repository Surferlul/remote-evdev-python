#!/bin/sh
# Windowing System:
#    Xorg is super laggy
#    Wayland is smooth, feels like native
# Custom VM settings:
#    Spice server side mouse:
#      <graphics type='spice'>
#        <listen type='none'/>
#        <mouse mode='server'/>
#        <gl enable='yes' rendernode='/dev/dri/by-path/pci-0000:05:00.0-render'/>
#      </graphics>
# Special Gnome (and gdm) settings:
#    Zoom toggle on:
#      Magnification: 1.0
#      -> continuously refreshes screen (i think?) to remove mouse stutter
# Guest OS firewall might need to be tinkered with
./main.py --guest --server --ip-address 0.0.0.0

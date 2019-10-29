#!/bin/sh
# launcher.sh
# Run the pixel pet robot (ideally on startup)
cd /home/pi/code/pixel-pet/code/ 
su pi -c '/usr/bin/python gamepad.py'
cd /
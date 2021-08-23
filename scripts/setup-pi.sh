#!/bin/sh

# Install everything that is needed
sudo apt -y update
sudo apt install python3-pip libsdl2-ttf-2.0-0 libsdl2-image-2.0-0

# Disable autostart up of emulationstation And enable my pycade
sudo echo "sudo python3 /home/pi/dev/pycade/main.py" > /opt/retropie/configs/all/autostart.sh

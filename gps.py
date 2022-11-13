'''
###write in /boot/config.txt  sudo nano /boot/config.txt
dtparam=spi=on
dtoverlay=pi3-disable-bt
core_freq=250
enable_uart=1
force_turbo=1
### exit and reboot
vcc-2
gnd-6
txd-8
rxd-10
#######execute in terminal
sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service
sudo systemctl enable serial-getty@ttyAMA0.service

sudo apt-get install minicom
sudo pip install pynmea2
###run the code##########
'''

import time
import serial
import pynmea2
import string
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
port = "/dev/ttyAMA0"

ser = serial.Serial(port, baudrate=9600, timeout=0.5)
while 1:
    try:
        data = ser.readline()
        print(data)

    except:
        print("loading")

    if data[0:6] == '$GPRMC':
        msg = pynmea2.parse(data)
        print(msg)
        time.sleep(2)

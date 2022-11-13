'''
connection
vcc pin 2
gnd pin 6
txd pin 8
rxd pin 10

sudo raspi-config -->Interfacing Options --> enable I2C or do by preference enable i2c

sudo apt-get update
sudo apt-get install libusb-dev libpcsclite-dev i2c-tools
wget http://dl.bintray.com/nfc-tools/sources/libnfc-1.7.1.tar.bz2

or download by browser
https://src.fedoraproject.org/lookaside/extras/libnfc/libnfc-1.7.1.tar.bz2/a3bea901778ac324e802b8ffb86820ff/


#to expand tar file
tar -xf libnfc-1.7.1.tar.bz2 

cd libnfc-1.7.1
./configure --prefix=/usr --sysconfdir=/etc
make
sudo make install

cd /etc
sudo mkdir nfc
sudo nano /etc/nfc/libnfc.conf

 i2cdetect –yes 1
 nfc list
    nfc-poll

'''
import subprocess
import time


def nfc_raw():
    lines = subprocess.check_output("/usr/bin/nfc-poll",
                                    stderr=open('/dev/null', 'w'))
    return lines


def read_nfc():

    lines = nfc_raw()
    return lines


try:
    while True:
        myLines = read_nfc()
        buffer = []
        for line in myLines.splitlines():
            line_content = line.split()
            if(not line_content[0] == 'UID'):
                pass
            else:
                buffer.append(line_content)
        str = buffer[0]
        id_str = str[2]+str[3]+str[4]+str[5]
        print(id_str)
except KeyboardInterrupt:
    pass

'''
connection 
VDD--pin 17
GND--pin 9
SCL--pin 5
SDA--pin 3

sudo apt-get update
sudo apt-get upgrade
sudo raspi-config --> interfacing options --> enable I2C
sudo apt-get install build-essential python-dev python-smbus git
git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
ls cd Adafruit_Python_ADS1x15 --> sudo python setup.py install
ls cd examples --> sudo python simpletest.py
cd 
sudo apt-get install python-matplotlib
sudo apt-get install python-pip12
sudo pip install drawnow
sudo nano scope.py
save ctrl o and run scope.py
'''
import time
import matplotlib.pyplot as plt
#import numpy
from drawnow import *
# Import the ADS1x15 module.
import Adafruit_ADS1x15
# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1
val = [ ]
cnt = 0
plt.ion()
# Start continuous ADC conversions on channel 0 using the previous gain value.
adc.start_adc(0, gain=GAIN)
print('Reading ADS1x15 channel 0')
#create the figure function
def makeFig():
    plt.ylim(-5000,5000)
    plt.title('Osciloscope')
    plt.grid(True)
    plt.ylabel('ADC outputs')
    plt.plot(val, 'ro-', label='Channel 0')
    plt.legend(loc='lower right')
while (True):
    # Read the last ADC conversion value and print it out.
    value = adc.get_last_result()
    print('Channel 0: {0}'.format(value))
    # Sleep for half a second.
    time.sleep(0.5)
    val.append(int(value))
    drawnow(makeFig)
    plt.pause(.000001)
    cnt = cnt+1
    if(cnt>50):
        val.pop(0)


#2 way
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
val = []
adc.start_adc(0, gain=GAIN)
print('Reading ADS1x15 channel 0')
fig, ax = plt.subplots()
ax.set_ylim(-5000, 5000)
ax.set_title('Oscilloscope')
ax.grid(True)
ax.set_ylabel('ADC outputs')
line, = ax.plot([], 'ro-', label='Channel 0')
ax.legend(loc='lower right')


def update(cnt):
    value = adc.get_last_result()
    print('Channel 0: {0}'.format(value))
    line.set_data(list(range(len(val))), val)
    ax.relim()
    ax.autoscale_view()
    val.append(int(value))
    if(cnt > 50):
        val.pop(0)


ani = FuncAnimation(fig, update, interval=500)
plt.show()

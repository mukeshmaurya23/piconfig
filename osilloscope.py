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
'''
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

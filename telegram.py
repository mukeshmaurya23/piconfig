import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)


def on(pin):
    GPIO.output(pin, GPIO.HIGH)
    return


def off(pin):
    GPIO.output(pin, GPIO.LOW)
    return


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Got command: %s' % command)
    if command == 'on':
        bot.sendMessage(chat_id, on(11))
    elif command == 'off':
        bot.sendMessage(chat_id, off(11))


bot = telepot.Bot('Bot Token')
bot.message_loop(handle)
print('I am listening...')
while 1:
    time.sleep(10)


'''
check version python -v
sudo apt-get install python3-pip
sudo pip install telepot
'''

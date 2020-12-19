import RPi.GPIO as GPIO
import time

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("Movement Detected!")
    else:
        print("Movement Detected!")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=100)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(1)
    
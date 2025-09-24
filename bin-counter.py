import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds=[16,12,25,17,27,23,22,24]
pl=9
mn=10
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds,0)
GPIO.setup(pl, GPIO.IN)
GPIO.setup(mn, GPIO.IN)
time_sleep=0.2
num=0
def totwo(x):
    return [int(element) for element in bin(x)[2:].zfill(8)]
while True:
    if GPIO.input(pl):
        num+=1
        num%=255
    if GPIO.input(mn):
        if num:
            num-=1
    time.sleep(time_sleep)
    for i in range(8):
        GPIO.output(leds[i],totwo(num)[i])
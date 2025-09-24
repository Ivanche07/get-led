import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds=[24,22,23,27,17,25,12,16]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds,0)
time_light=0.3
while True:
    for num in leds:
        GPIO.output(num,1)
        time.sleep(time_light)
        GPIO.output(num,0)
    for num in reversed(leds):
        GPIO.output(num,1)
        time.sleep(time_light)
        GPIO.output(num,0)
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led=26
datchik=31
GPIO.setup(datchik, GPIO.IN)#как цифровой выход
GPIO.setup(led, GPIO.OUT)
while True:
    light=GPIO.input(datchik)
    if light:
        GPIO.output(led,1)
    time.sleep(0.2)
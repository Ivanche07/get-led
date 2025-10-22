import RPi.GPIO as GPIO
bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
GPIO.setmode(GPIO.BCM)
GPIO.setup(bits_gpio, GPIO.OUT, initial = 0)
GPIO.output(bits_gpio,[1,1,1,1,1,1,1,1])
while True:
    if input()=="0":
        GPIO.setup(bits_gpio, GPIO.OUT, initial = 0)
    break
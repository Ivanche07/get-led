import RPi.GPIO as GPIO
import time
def dec2bin(value):
    return ([int(element) for element in bin(value)[2:].zfill(8)])
class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
        print("GPIO have been cleaned")
    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio,dec2bin(number))
        #print(dec2bin(number))
        #time.sleep(self.compare_time)
    def sequential_counting_adc(self):
        for value in range(256):
            self.number_to_dac(value)
            time.sleep(self.compare_time)
            compValue = GPIO.input(self.comp_gpio)
            if(compValue==1):
                print(value)
                return value
        return self.dynamic_range
    
if __name__ == "__main__":
    try:
        dac = R2R_ADC(3.14,0.01,True)
        while True:
            try:
                voltage=dac.sequential_counting_adc()
                print(voltage)
            except ValueError:
                print("Как ты сюда попал?\n")

    finally:
        dac.deinit()
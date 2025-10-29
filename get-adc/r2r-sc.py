import matplotlib.pyplot as plt
import time
import adc_plot
#import RPi.GPIO as GPIO
import r2r_adc
'''
class R2R_ADC:
    def __init__(self, voltage, time, verbose=False):
        self.voltage=voltage
        self.time=time
        self.comp_gpio=21
        self.bits_gpio=[26, 20, 19, 16, 13, 12, 25, 11]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
        print("GPIO have been cleaned")
    def to_massive(self):
        if(duration>=time.time()-t0):
            self.time.append(time.time()-t0)
            self.voltage.append(GPIO.input(self.comp_gpio))
'''
if __name__ == "__main__":
    try:
        voltage_value=[]
        time_values=[]
        max_voltage=3.278
        dac = r2r_adc.R2R_ADC(3.278, 0.01, True)
        duration=3.0
        t0=time.time()
        while (duration>=time.time()-t0):
            try:
                while (duration>=time.time()-t0):
                    time_values.append(time.time()-t0)
                    voltage_value.append(dac.good_algoritm()/255*max_voltage)
                #print(time_values)
                adc_plot.plot_voltage_vs_time(time_values, voltage_value, max_voltage)  
                #for i in range(len(voltage_value)):
                #    if voltage_value[i]!=0:
                #        print(voltage_value[i]) 
            except ValueError:
                print("Как ты сюда попал?\n")
    finally:
        dac.deinit()
import RPi.GPIO as GPIO
leds=[16,20,21,25,26,17,27,22]
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(leds, GPIO.OUT)
#GPIO.output(leds,0)
dynamic_range1=3.14
class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self,number):
        some=[int(element) for element in bin(number)[2:].zfill(8)]
        for i in range(len(self.gpio_bits)):#почему self  много
            GPIO.output(self.gpio_bits[i],some[i])

    def set_voltage(self,voltage):
            if not (0.0 <= voltage <= self.dynamic_range):
                print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
                return 
            self.set_number(int(voltage / self.dynamic_range * 255))

if __name__ == "__main__":
    try:
        dac = R2R_DAC(leds, dynamic_range1, True)#Видимо, эта штука записывает все значения на вход в init
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led=12
GPIO.setup(led, GPIO.OUT)
pwm=GPIO.PWM(led,1000)
dynamic_range_max=3.14
duty=0.0
pwm.start(duty)
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        pwm_frequency=pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self,voltage):
            if not (0.0 <= voltage <= self.dynamic_range):
                print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            else:    
                duty=100*voltage/dynamic_range_max
                pwm.ChangeDutyCycle(duty)
                print(f"Коэффициент заполнения:{voltage/dynamic_range_max}")

if __name__ == "__main__":
    try:
        dac = PWM_DAC(led,duty, dynamic_range_max, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()

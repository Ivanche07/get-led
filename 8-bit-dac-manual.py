import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#leds=[16,12,25,17,27,23,22,24]
leds=[16,20,21,25,26,17,27,22]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds,0)
dynamic_range=3.3

def number_to_dac(x):
    return [int(element) for element in bin(x)[2:].zfill(8)]

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В почему")
        return 0
    #print(f"Число на вход ЦАП: {number}, биты: [0, 0, 0, 0, 0, 0, 0, 0]")
    return int(voltage / dynamic_range * 255)
try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
            print(f"Число на вход ЦАП: {number}, биты: {[int(element) for element in bin(number)[2:].zfill(8)]}")
            for i in range(8):
                GPIO.output(leds[i],number_to_dac(number)[i])
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")
finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()

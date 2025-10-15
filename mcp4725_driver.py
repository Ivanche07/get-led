import smbus
dynamic_range_max=5.11
number_max=4095
class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)
        
        self.address = address
        self.wm = 0x00
        self.pds = 0x00
        
        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_voltage(self,voltage):
            if not (0.0 <= voltage <= self.dynamic_range):
                print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            else:    
                self.set_number(int(number_max*voltage/self.dynamic_range))  #очень важно устанавливать номер

    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")

        if not (0 <= number <= number_max):
            print("Число выходит за разраядность MCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")
 

if __name__ == "__main__":
    try:
        dac = MCP4725(dynamic_range_max)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
'''Не забыть про команды:
raspi-gpio set 2 a0
raspi-gpio set 2 a0
raspi-gpio get'''
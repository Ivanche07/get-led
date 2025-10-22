import matplotlib.pyplot as plt
def plot_voltage_vs_time(time,voltage,max_voltage):
    plt.figures(figsize=(10,6))
    plt.plot(time,voltage)
    plt.show
class R2R_ADC:
    def __init__(self):
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
        print("GPIO have been cleaned")

if __name__ == "__main__":
    try:
        dac = R2R_ADC()
        voltage_values=[]
        time_values=[]
        duration=3.0
        while True:
            try:
                voltage=(dac.sequential_counting_adc()/256)*dac.dynamic_range
                print(voltage)
            except ValueError:
                print("Как ты сюда попал?\n")

    finally:
        dac.deinit()
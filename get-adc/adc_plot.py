#from scipy.optimize import curve_fit
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.ylabel("Напряжение, U (В)")
    plt.xlabel("Время, T (с)")
    plt.title("График напрядений на входе АЦП ПС")
    plt.xlim(0,4)
    plt.ylim(0,3.5)
    plt.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    plt.plot(time,voltage)
    plt.show()
    plt.savefig('for_adc_plot.png', dpi=300)
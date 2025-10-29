'''
import adc_plot
from matplotlib import pyplot as plt
x=[]
y=[]
for i in range(1,1000):
    x.append(1/i)
for j in range(1,1000):
    y.append(j/1000)
adc_plot.plot_voltage_vs_time(x,y,3)
'''
x=113
v=0
for i in range(1,9):
    if(v+2**(8-i)<=x):
        v=v+2**(8-i)
print(v)
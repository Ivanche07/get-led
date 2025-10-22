import time
import math
def get_triangle_amplitude(freq, time):
    n=math.floor(time*freq)
    delta=(time-n/freq)*2*freq
    if delta>=0 and delta<=1:
        return delta
    else:
        return delta-1
def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)
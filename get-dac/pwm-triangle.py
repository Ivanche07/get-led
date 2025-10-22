import pwm_dac as pwm
import triangle as tg
import time as tm
amplitude = 3.1
signal_frequency = 10
sampling_frequency = 1000
led=12
if __name__ == "__main__":
    try:
        pwm = pwm.PWM_DAC(led, 500, 3.14, True)#Видимо, эта штука записывает все значения на вход в init
        paraputairaputiraputai=tm.asctime(tm.gmtime(0))
        while True:
            try:
                voltage=0.5*amplitude*tg.get_triangle_amplitude(signal_frequency, tm.time())
                pwm.set_voltage(voltage)
                tg.wait_for_sampling_period(sampling_frequency)
            except ValueError:
                print("Mission failed\n")

    finally:
        pwm.deinit()
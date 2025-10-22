import mcp4725_driver
import triangle as tg
import time as tm
amplitude = 3.1
signal_frequency = 10
sampling_frequency = 1000
if __name__ == "__main__":
    try:
        mcp4725_driver = mcp4725_driver.MCP4725(5.11)#Видимо, эта штука записывает все значения на вход в init
        paraputairaputiraputai=tm.asctime(tm.gmtime(0))
        while True:
            try:
                voltage=0.5*amplitude*tg.get_triangle_amplitude(signal_frequency, tm.time())
                mcp4725_driver.set_voltage(voltage)
                tg.wait_for_sampling_period(sampling_frequency)
            except ValueError:
                print("Mission failed\n")
    finally:
        mcp4725_driver.deinit()
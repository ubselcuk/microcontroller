import machine
import time


while True:
    print("Nem:", machine.ADC(28).read_u16())
    time.sleep(1)
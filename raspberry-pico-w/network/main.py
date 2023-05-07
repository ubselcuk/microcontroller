import network
from time import sleep
import machine
from machine import Pin

led=Pin("LED", Pin.OUT)
ssid = ''
password = ''

def connected(a):
    for x in range(0,a):
        led.value(1)
        sleep(0.1)
        led.value(0)
        sleep(0.1)

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    connected(3)
    return ip


try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()
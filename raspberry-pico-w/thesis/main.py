import micropg
import network
import socket
from time import sleep
import machine
from machine import Pin

led=Pin("LED", Pin.OUT)
def flash():
    led.value(1)
    sleep(1)
    led.value(0)
    print('QUERY SENDED')

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('SUPERONLINE_WiFi_9488', 'k2SPT36SxuYf')
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def get_serial_number():
    cpuid = machine.unique_id()
    serial_number = ""
    for i in range(len(cpuid)):
        serial_number += "{:02x}".format(cpuid[i])
    return serial_number

try:
    ip = connect()
    serial = get_serial_number()
    conn = micropg.connect(host='185.136.206.253',
                    port=5432,
                    user='postgres',
                    password='password',
                    database='flora')
    cur = conn.cursor()

    while True:
        cur.execute("UPDATE plants SET humid=%s WHERE pico=%s",[int(100 - ((machine.ADC(28).read_u16() / 65535) * 100)),serial])
        conn.commit()
        flash()
        sleep(10)

except KeyboardInterrupt:
    machine.reset()

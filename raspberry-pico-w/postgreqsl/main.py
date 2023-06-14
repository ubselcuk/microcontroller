import micropg
import network
import socket
from time import sleep
import machine
from machine import Pin
led=Pin("LED", Pin.OUT)
BRate=0.25


def flash():
    led.value(1)
    sleep(4*BRate)
    led.value(0)
    sleep(BRate)

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
    cur.execute("INSERT INTO plants(humid, pico) values (25,%s)",[serial])
    conn.commit()
    print('QUERY SENDED')
    flash()
    
except KeyboardInterrupt:
    machine.reset()

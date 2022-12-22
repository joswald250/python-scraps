#!/usr/bin/python3

import signal, gpiozero
from time import sleep

sensor = gpiozero.DistanceSensor(echo=24, trigger=23)

def safe_exit(signum, frame):
    exit(1)
    
signal.signal(signal.SIGTERM, safe_exit)
signal.signal(signal.SIGHUP, safe_exit)

try:
    while True:
        print('Distance: ', sensor.distance * 100)
        sleep(1)
        
except KeyboardInterrupt:
    pass

finally:
    sensor.close()
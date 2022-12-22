#!/usr/bin/python3
import signal, rpi_lcd
from gpiozero import MotionSensor, DistanceSensor
from time import sleep

lcd = rpi_lcd.LCD()
sensor = DistanceSensor(echo=24, trigger=23)

def safe_exit(signum, frame):
    exit(1)
    
signal.signal(signal.SIGTERM, safe_exit)
signal.signal(signal.SIGHUP, safe_exit)

try:
    while True:
        
        lcd.text("Your Distance:", 1)
        lcd.text(str(round(sensor.distance * 100, 1)) + "cm", 2)
        sleep(0.5)
        lcd.clear()
    

except KeyboardInterrupt:
    pass

finally:
    lcd.clear()
    sensor.close()


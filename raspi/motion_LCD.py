#!/usr/bin/python3
import signal, rpi_lcd
from gpiozero import MotionSensor, DistanceSensor
from time import sleep

pir = MotionSensor(21)
lcd = rpi_lcd.LCD()
sensor = DistanceSensor(echo=24, trigger=23)

def safe_exit(signum, frame):
    exit(1)
    
signal.signal(signal.SIGTERM, safe_exit)
signal.signal(signal.SIGHUP, safe_exit)

try:
    while True:
        pir.wait_for_motion()
        lcd.text("You Moved!", 1)
        lcd.text("Distance: " + str(round(sensor.distance * 100, 1)) + "cm", 2)
        pir.wait_for_no_motion()
        lcd.clear()
    

except KeyboardInterrupt:
    pass

finally:
    lcd.clear()
    sensor.close()


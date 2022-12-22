#!/usr/bin/python3
import signal, rpi_lcd

lcd = rpi_lcd.LCD()

def safe_exit(signum, frame):
    exit(1)
    
signal.signal(signal.SIGTERM, safe_exit)
signal.signal(signal.SIGHUP, safe_exit)

try:
    lcd.text("Hello,", 1)
    lcd.text("Raspberry Pi!", 2)
    
    signal.pause()

except KeyboardInterrupt:
    pass

finally:
    lcd.clear()

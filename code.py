"""
Cretaed by: Osamah
Created on: FEB 2025
Created for: TEJ3M-Unite 2-01 led loop
"""
import board 
import digitalio 
import time

blink_time = 1

led = digitalio.DigitalInOut(board.LED)

led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(blink_time)

    led.value = False
    time.sleep(blink_time)
    
    blink_time = blink_time + 1

import machine
import time

leds = [machine.Pin(2, machine.Pin.OUT), machine.Pin(16, machine.Pin.OUT)]

for i in range(100):
    leds[0].on()
    leds[1].off()
    time.sleep(.5)
    leds[0].off()
    leds[1].on()
    time.sleep(.5)

import board
import digitalio
import time
import usb_hid
import storage
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    # Turn on LED
    led.value = True

    # Move Mouse 1 pixel right and left
    mouse.move(x=1)
    mouse.move(x=-1)

    # Sleep, a little bit
    time.sleep(0.5)

    # Turn off LED
    led.value = False

    # Sleep
    time.sleep(30)
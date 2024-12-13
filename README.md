# pico2hid
Use a Raspberry Pico 2 W as a USB mouse-device (aka "Jiggler")

## HowTo install
### 1. Connect fresh Pico 2 via USB
Your Pico 2 will show up as "RP2350" device with 2 read-only files
- INDEX.HTM
- INFO_UF2.TXT
### 2. Install CircuitPython
Drop the UF2-CircuitPython [Firmware](firmwares/adafruit-circuitpython-raspberry_pi_pico2_w-de_DE-9.2.1.uf2), 
or [download](https://circuitpython.org/board/raspberry_pi_pico2_w/) a newer one, 
on to your Pico 2 "RP2350"-Device. It will automatically install the CircuitPython firmware and reboot.
You now have a "CIRCUITPYTHON" USB-device.

### 3. Install libraries and code
Drop the files and contents from
- [lib](lib) (from [CircuitPython Libraries Bundle](https://circuitpython.org/libraries))
- [code.py](code.py)
  
on to your device.
The LED should start blinking every 30 second, indicating your device is running (and doing mouse-moves 😁).
### 4. (Optional) Disable Pico from showing up as a mass-storage-device
⚠️ THIS WILL MAKE YOUR PICO READ-ONLY!  

Drop the file
- [boot.py](boot.py)

on to your device. You will need to unplug and reinsert the device.  
Your Pico 2 is now acting like a mouse device (Jiggler).

As the device is no mass-storage-device any longer, for making any further change to it, you will need to reset the firmware and start from beginning:

### 5. Reset firmware
In order to make any further change, we will need to wipe the contents from device, and make it writable, again. 
- Unplug Device
- Press AND HOLD the "Bootsel"-Button on the device and reinsert it. (Then release, of course).
- Your Pico will start up as "RP2350" with the 2 files (like at the start), again.
- Drop the [nuke](firmwares/universal_flash_nuke.uf2) firmware on it
- Unplug Device
- Start from [beginning...](#connect-fresh-pico-2-via-usb)

## Improvements
How about making use of the bluetooth stack, included in Pico 2 W, for acting like a bluetooth-device?

## References
- [CircuitPython](https://circuitpython.org)
- [CircuitPython Pico 2 firmware](https://circuitpython.org/board/raspberry_pi_pico2_w/)
- [CircuitPython Libraries Bundle](https://circuitpython.org/libraries)
- [CircuitPython keyboard and mouse](https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse)
- [Disabling as storage-device](https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial#circuitpy-mass-storage-device-3096583)
- GitHub [Gadgetoid/pico-universal-flash-nuke](https://github.com/Gadgetoid/pico-universal-flash-nuke?tab=readme-ov-file)
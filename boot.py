import storage
import usb_hid

# THIS WILL MAKE YOUR PICO UNREADABLE (as a mass storage device)!
storage.disable_usb_drive()
usb_hid.enable((usb_hid.MOUSE))
import storage
import usb_hid

# THIS WILL MAKE YOUR PICO UNREADABLE (as a mass storage device)!
storage.disable_usb_drive()
usb_hid.enable((Device.MOUSE,), boot_device=2)
usb_hid.set_interface_name("Insomnia Jiggler")
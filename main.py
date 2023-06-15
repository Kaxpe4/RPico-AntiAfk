import usb_hid
from adafruit_hid.mouse import Mouse
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid. devices)

while True:
    mouse.move(x=200)
    time.sleep(1)
    mouse.move(x=-200)
    time.sleep(1)
    kbd.press(Keycode.W)
    time.sleep(5)
    kbd.press(Keycode.A)
    time.sleep(15)
    

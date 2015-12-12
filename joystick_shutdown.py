# Shutdown Pi by pressing the Sense HAT joystick centre button for 5 seconds
# Place joystick_shutdown script in crontab to run at startup
# Change path to joystick_shutdown.py in .sh file as required

import sys
import os, time
import subprocess
from sense_hat import SenseHat
from evdev import InputDevice, list_devices, ecodes

sense = SenseHat()
sense.clear()

# Check if Sense HAT is available, else abort
found = False;
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
    if dev.name == 'Raspberry Pi Sense HAT Joystick':
        found = True;
        break

if not(found):
    print('Raspberry Pi Sense HAT  not found. Aborting ...')
    sys.exit()

i = 0
try:
  for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
       if event.code == 28: #28 is event code for KEY_ENTER
          i = i+1
          time.sleep(1)
       if i == 5:  
          subprocess.call(["sudo", "shutdown", "-h", "now"])
except KeyboardInterrupt:
  sys.exit()

#!/usr/bin/python

from evdev import InputDevice, categorize, ecodes
import time
gamepad = InputDevice('/dev/input/event2')
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        print(categorize(event))
    elif event.type == ecodes.EV_ABS:
        print(categorize(event))
	absevent = categorize(event)
	print(absevent.event.value)
	print(ecodes.bytype[absevent.event.type][absevent.event.code])

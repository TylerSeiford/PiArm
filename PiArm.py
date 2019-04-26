#!/usr/bin/python

from evdev import InputDevice, categorize, ecodes, KeyEvent
import os
import time

pos1 = 150
os.system("sudo echo 0=150 > /dev/servoblaster")
pos2 = 150
os.system("sudo echo 1=150 > /dev/servoblaster")
pos3 = 150
os.system("sudo echo 2=150 > /dev/servoblaster")
pos4 = 150
os.system("sudo echo 3=150 > /dev/servoblaster")
pos5 = 150
os.system("sudo echo 4=150 > /dev/servoblaster")
pos6 = 150
os.system("sudo echo 5=150 > /dev/servoblaster")
gamepad = InputDevice('/dev/input/event2')
last = 0

for event in gamepad.read_loop():
	if event.type == ecodes.EV_KEY:
		keyevent = categorize(event)
		if keyevent.keystate == KeyEvent.key_down:
			if keyevent.keycode == 'BTN_Y':
				if pos1 <= 240:
					os.system("sudo echo 0=+10 > /dev/servoblaster")
					print "1 +10"
					pos1 += 10
					print pos1
			elif keyevent.keycode[0] == 'BTN_A':
				if pos1 >= 60:
					os.system("sudo echo 0=-10 > /dev/servoblaster")
					print "1 -10"
					pos1 -= 10
					print pos1
			elif keyevent.keycode == 'BTN_B':
				if pos2 <= 240:
					os.system("sudo echo 1=+10 > /dev/servoblaster")
					print "2 +10"
					pos2 += 10
					print pos2
			elif keyevent.keycode == 'BTN_X':
				if pos2 >= 60:
					os.system("sudo echo 1=-10 > /dev/servoblaster")
					print "2 -10"
					pos2 -= 10
					print pos2
			elif keyevent.keycode == 'BTN_TR':
				if pos3 <= 240:
					os.system("sudo echo 2=+10 > /dev/servoblaster")
					print "3  +10"
					pos3 += 10
					print pos3
			elif keyevent.keycode == 'BTN_TL':
				if pos3  >= 60:
					os.system("sudo echo 2=-10 > /dev/servoblaster")
					print "3 -10"
					pos3 -= 10
					print pos3
			elif keyevent.keycode == 'BTN_START':
				os.system("sudo echo 0=150 > /dev/servoblaster")
				os.system("sudo echo 1=150 > /dev/servoblaster")
				os.system("sudo echo 2=150 > /dev/servoblaster")
				os.system("sudo echo 3=150 > /dev/servoblaster")
				os.system("sudo echo 4=150 > /dev/servoblaster")
				os.system("sudo echo 5=150 > /dev/servoblaster")
				print "Centered!"
				pos1 = 150
				pos2 = 150
				pos3 = 150
				pos4 = 150
				pos5 = 150
				pos6 = 150
	elif event.type == ecodes.EV_ABS:
		absevent = categorize(event)
		code = ecodes.bytype[absevent.event.type][absevent.event.code]
		if code == 'ABS_HAT0X':
			if absevent.event.value > 0.5:
				if pos4 <= 240:
					os.system("sudo echo 3=+10 > /dev/servoblaster")
					print "4 +10"
					pos4 += 10
					print pos4
			elif absevent.event.value < -0.5:
				if pos4 >= 60:
					os.system("sudo echo 3=-10 > /dev/servoblaster")
					print "4 -10"
					pos4 -= 10
					print pos4
		elif code == 'ABS_HAT0Y':
			if absevent.event.value > 0.5:
				if pos5 <= 240:
					os.system("sudo echo 4=+10 > /dev/servoblaster")
					print "5 +10"
					pos5 += 10
					print pos5
			elif absevent.event.value < -0.5:
				if pos5 >= 60:
					os.system("sudo echo 4=-10 > /dev/servoblaster")
					print "5 -10"
					pos5 -= 10
					print pos5
		elif code == 'ABS_Z':
			if absevent.event.value > 128:
				if last == 0:
					if pos6 <= 240:
						os.system("sudo echo 5=+10 > /dev/servoblaster")
						print "6  +10"
						pos6 += 10
						print pos6
						last = 1
			else:
				last = 0
		elif code == 'ABS_RZ':
			if absevent.event.value > 128:
				if last == 0:
					if pos6  >= 60:
						os.system("sudo echo 5=-10 > /dev/servoblaster")
						print "6 -10"
						pos6 -= 10
						print pos6
						last = 1
			else:
				last = 0

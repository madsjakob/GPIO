import sys

sys.path.append("./MJS")

import GPIO as gp 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ir = [5, 6, 13, 19]

for sensor in ir:
	GPIO.setup(sensor, GPIO.IN)

while 1:
 	for sensor in ir:
		if GPIO.input(sensor):
			print str(sensor) + " is high"
		else:
			print str(sensor) + " is low"
	time.sleep(1)


GPIO.cleanup()

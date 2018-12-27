#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

print("Grove Sensor")

GPIO.setmode(GPIO.BCM)
print("RPi.GPIO setup OK")

trig = 4 #gpio 04
echo = 17 #gpio 17

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)


try:
	while True:
		GPIO.output(trig, False)
		time.sleep(0.5)
		
		GPIO.output(trig, True)
		time.sleep(0.0001)
		GPIO.output(trig, False)
		
		while GPIO.input(echo) == 0:
			startTime = time.time()
		while GPIO.input(echo) == 1:
			endTime = time.time()
		
		# 시간의 차이에 따라 거리 계산
		durationTime = endTime - startTime
		distance = durationTime * 17000
		distance = round(distance, 2)
		print("Distance:",distance,"cm")
		

except KeyboardInterrupt:
	print("GPIO.cleanup()")
	GPIO.cleanup()

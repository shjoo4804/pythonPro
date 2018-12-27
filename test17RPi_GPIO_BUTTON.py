#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

print("RPi_GPIO_BUTTON")

GPIO.setmode(GPIO.BCM)
print("RPi.GPIO setup OK")

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #BUTTON : IN


try:
	while True:
		inputValue = GPIO.input(17) #눌렸는지 떼졌는지 체크  
		print(inputValue)
		if(inputValue == False):
			print("button")
			time.sleep(0.3)
except KeyboardInterrupt:   #terminal : ctrl + C 
	GPIO.cleanup()
	print("cleanup") 

	
print("end...")

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

print("RPi_GPIO_BUTTON")

GPIO.setmode(GPIO.BCM)
print("RPi.GPIO setup OK")

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #BUTTON : IN
GPIO.setup(17, GPIO.OUT)  #LED : OUTPUT
GPIO.output(17, False) 
GPIO.setup(4, GPIO.OUT) 
GPIO.output(4, False) 


try:
	while True:
		inputValue = GPIO.input(22) #눌렸는지 떼졌는지 체크  
		print(inputValue)
		if(inputValue == False):
			print("button")
			print("ON")
			GPIO.output(17, True)
			GPIO.output(4, True) 
			time.sleep(0.3)
		else:
			print("OFF")
			GPIO.output(17, False) 
			GPIO.output(4, False) 
except KeyboardInterrupt:   #terminal : ctrl + C 
	GPIO.cleanup()
	print("cleanup") 

	
print("end...")

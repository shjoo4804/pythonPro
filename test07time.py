#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys #lib
import time
import datetime

print('python::: time')

time.sleep(3) # 3초 후에 아래 실행 
print("end sleep")
print(datetime.datetime.now()) # 연 월 일 시 분 초

for i in range(10):
	print(i)
	time.sleep(1)
	

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys #lib

print('python::: sys and if else')

#터미널에서 실행 : python test03sys_if.py 11  
print("msg[0]:", sys.argv[0])  # shell - $0
print("msg[1]:", sys.argv[1])  # shell - $1

#raw_input() >> python2.x
#input() >> python3.x
print("input your name:")
name = raw_input()   # br.readline() 혹은 scanf()과 같이 입력받는 것


hi = "hello"
print(name)
print(hi)
print(raw_input("input your name:;")  #format 쓸때는 .(온점) 사용


if True:
	print("{} {}".format(name, hi))  # depth 주의(들여쓰기해야 if문 안에서 돌아감)
	
if 5>=5:
	print("{} {}".format(name, hi)) 


a = 3.14
print(type(a))
print(float(a))
print(type(a))
print(type(float(a)))

if float(a) == 3.14:
	print("lee")
elif a==3:
	print("sam")
elif a==5:
	print("five")
else:
	print("other")
	
	


#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys #lib

print('python::: def')
#def : java(method), c(function)

def sum(a,b):
	print("sum(a,b)...a:{},b:{}".format(a,b))

sum(10,20.22) # type상관없이 넣을 수 있음
sum(10,20)


##############

def sum():
	print("sum()...")

sum()

##############
# 함수의 반환값 출력하기
def sum(x,y):
	return x+y

sumXY = sum(100,200)
print("sumXY", sumXY)

###############

def test(a,b,c,d,e):
	print("test()...")
	lst=[a,b,c,d,e,"kim"]
	for item in lst:
		print(item),

test(1,2,3,4,5)

###############

def test2(*args): # *:모든 매개변수들
	for item in args:
		print(item)

test2(11,22,33,44,55,66,77,"yangssem:")

################

def getName():
	name = raw_input("input your name:")
	return  name
print(getName())


def printList(lst):
	for item in lst:
		print(item)
		
printList([11,22,33,99])

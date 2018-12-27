#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys #lib

print('python::: for')

for i in range(10):
	print(i) #print(i) : 엔터쳐서 한줄씩(세로)
	
print

for i in range(10):
	print(i),  #print(i), : 한줄에 출력(가로)


#python2.x >>> ,(comma) 사용 시 가로출력가능


#10~19까지 출력
for i in range(10,20): 
	print(i),
	
   #python3.xxx >> i, end= ' ' 사용 시 가로출력
#for i in range(10,20):  
#	 print(i, end=",")
#	print(i, end=" ") #구분자 지정가능

print

for i in range(10,20): 
	print("{} * {} = {}".format(i, 10, i*10)),


print
print


# 구구단
for x in range(1,10):
	for i in range(1,10):
		print("{}*{}={}".format(x, i, x*i)),
	print

print

#list >> java, c, js : array
lst = [11,22,33,44,55]
print("lst", type(lst))
print("len(lst)", len(lst))

for i in range(len(lst)):
	print(lst[i])

print("======")

sum=0
for item in lst:
	print(item)
	sum+=item
	
print("sum:",sum)



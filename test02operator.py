#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python test01hello.py
#python3 test01hello.py

print('python Operator')

su = 100
result = su + 1
print('result', result)

re01 = 'result:'
re02 = '101'
re03 = re01 + re02 # 문자열 더하기..
print(re03)


# +,-,*,/,%
print('10+10',10+10)
print('10-10',10-10)
print('10*10',10*10)
print('10/10',10/10)
print('10/3',10/3)
print('10%10',10%10)
print("'a'*10",'a'*10)


# +=, -=, *=, /=, %, &=, |=, ^=
x=10
x+=10
print('x+=10', x)


# &, |, ^(exclusive or) >> bit연산
print(10&2) 


# ==, !=, >, <, >=, <=
print(10==10)


# 3항연산
result = True and "KIM" or "LEE" # True면 KIM
print(result)
result = False and "KIM" or "LEE" # False면 LEE
print(result)

result = "yangssem" if True else "Han"
print(result)
result = "yangssem" if False else "Han"
print(result)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys #lib

print('python ::: dict(dictionary)')

dic = {'name':'yangssem', 'tel':'010'}
print(type(dic))
print(dic)


print(dic['name'])
print(dic['tel'])
print(dic.get('name'))
print(dic.get('tel'))


print('name' in dic) #dic안에 있으면 True, 없으면 False


dic = {}
print(dic)


dic = {1:'aaa',2:'bbb'}
dic[3] = 'yangssem'
dic['addr'] = 'seoul'
dic['lst'] = [1,2,3]
dic['tp'] = (4,5,6)
dic['dt'] = {'email':'aaa@ccc.com'}
print(dic)
print(dic['lst'][0])
print(dic['tp'][0])
print(dic['dt']['email'])

print

print(dic.keys())
print(type(dic.keys()))
print

print(dic.values())
print(type(dic.values()))
print

print(dic.items())
print(type(dic.items()))
print

for key in dic:
	print(key,dic[key])
print

print(dic.get('100')) #None

dic.clear()
print(dic)

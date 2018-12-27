#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys #lib

print('python ::: tuple')

#list >>> read, insert, update(append), delete
#tuple >>> read only (수정불가능)


tp = ()
tp = (0,0,0,0)
print(type(tp))
print(tp)

tp = (1,2,3,4)
print(tp)

tp = (1,2,3,(11,22))
print(tp)

tp = (1,2,3,(11,22),[99,88])
print(tp)

#del tp[0] # error # read Only
#tp[0] = 100 # error
#tp[1:3] = (77,88) #error
#tp.append(99) # error

tp = tp + (77,88) # 병합은 가능함 (재할당)
print(tp)

tp = tp * 2
print(tp)


tp = (1,2,3,('aaa','bbb'))
tp = tp[3:] # index 3부터 새로운 tp에 재할당
print(tp)

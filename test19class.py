#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("class")

#MemberVO
class MemberVO:
	userName = "yangssem"
	def __init__(self):  # constructor
		print("__init__")

m = MemberVO()
print("m.userName", m.userName)
print

##########

#ScoreVO
class ScoreVO:
	def __init__(self, name, kor, eng, math): #매개변수가 있는 생성자 
		print("__init__")
		self.name = name
		self.kor = kor
		self.eng = eng
		self.math = math
	def getName(self):
		return self.name
	def setName(self, name):
		self.name = name

s = ScoreVO("kim", 99, 88, 77)
print("s.name", s.name)
print("s.kor", s.kor)
print("s.eng", s.eng)
print("s.math", s.math)
print(vars(s))  #함수 call #dict 타입으로 나옴
print(type(vars(s)))
s.setName("yangssem")
print(s.getName())

##########

#BoardVO
class BoardVO:
	def __init__(self, title="bbb"):
		print("__init__")
		self.title = title

b = BoardVO()
print(b.title)
b = BoardVO("title")
print(b.title)


##########

class Student:
	def __init__(self, num=0, name="hong"):
		print("__init__")
		self.__num = num #__ : private >> getter, setter필요
		self.__name = name
	def getNum(self):
		return self.num
	def setNum(self,  num):
		self.num = num
	def getName(self):
		return self.name
	def setName(self,  name):
		self.name = name

st = Student()
#print(st.num) # error
#print(st.name)
st.setNum(13)
print(st.getNum()) 
st.setName("shin")
print(st.getName()) 



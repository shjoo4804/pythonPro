#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("inner def")


#절댓값 abs
print(abs(-11))
print(abs(11))
print


#all
print(all([])) #리스트 형식인가
print(all([1,2,3])) #리스트 형식인가
print(all([1,2,3,0])) #0이 있으면 거짓 
print(all(['aaa','bbb','ccc']))
print(all(['aaa','bbb','ccc',''])) #빈문자가 있으면 거짓
print(all(['aaa','bbb','ccc',""])) #빈문자가 있으면 거짓
print

#any : 하나라도 정상적인 데이터가 들어있으면 True 
print(any([1,2,3,0])) 
print(any(['aaa','bbb','ccc',""])) 
print


#dir
print(dir([])) 
print

print(dir(())) 
print

print(dir(("kim"))) 
print


#chr : 정수를 캐릭터로 변환 
print(chr(97), chr(98), chr(66)) 
print


#divmod : 몫, 나머지 구해줌
print(divmod(7,3))
print(type(divmod(7,3)))

print(divmod(22.3, 12.5))
print(type(divmod(22.3, 12.5)))
print


#eval : 연산해줌
print(eval("'kim'+'lee'"))
print(eval("22+33"))
print


#hex : 10진수를 16진수로 변환
print(hex(10))
print(hex(255))
print(hex(0))
print


#id : 값이 내부적으로 갖는 id
print(id("yangssem"))
print(id("a"))
print


# isinstance
class Person:
	pname = "yangssem"

p = Person()
print(p.pname)
print(isinstance(p, Person)) #p가 Person의 객체인가


# filter
def fn(item):
	return item >= 0

print(list(filter(fn, [0,1,-1,2,-2])))   
#list(filter) : filter를 거쳐서 True로 나온 애들만 list로 만듦

print(list(filter(lambda item:item<0, [0,1,-1,2,-2])))   # lambda 표현식 
print


#
def fn2(item):
	return item**2
print(list(map(fn2,[1,2,3,4,-5])))

print(list(map(lambda item:item**2, [1,2,3,4,-5])))
print


#zip : 첫번째끼리, 두번재끼리...묶어주기
print(list(zip([1,2,3], [4,5,6])))  
print(list(zip([1,2,3], [4,5,6], [100,200,300])))  
print(list(zip("abc", "123")))

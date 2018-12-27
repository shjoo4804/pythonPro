#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("os path exists")

os.system("pwd")
os.system("ls -l")

result = os.path.exists("/home/pi/pythonPro")
print("os.path.exists", result)  #경로가 있으면 True

result = os.path.exists("/home/pi/pythonPro/test01hello.py")
print("os.path.exists", result)


#os.path.dirname : 해당 폴더/파일이 들어있는 dir의 이름을 알려달라
result = os.path.dirname("/home/pi/pythonPro")
print("os.path.dirname", result)

result = os.path.dirname("/home/pi/pythonPro/test01hello.py")
print("os.path.dirname", result)


#isfile :file인가
result = os.path.isfile("/home/pi/pythonPro")
print("os.path.isfile", result)

result = os.path.isfile("/home/pi/pythonPro/test01hello.py")
print("os.path.isfile", result)


#getsize : 용량
result = os.path.getsize("/home/pi/pythonPro")
print("os.path.getsize", result)

result = os.path.getsize("/home/pi/pythonPro/test01hello.py")
print("os.path.getsize", result)



### 참고 documents
# https://docs.python.org/3/library/os.path.html

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
print("os open")
"""
---os.open option---
os.O_RDWR >> read write
os.O_RDONLY >> readonly
os.O_WOONLY >> writeonly
os.O_CREAT >> file create if not exist
os.O_APPEND >> append
"""

fd = os.open("test29.txt", os.O_RDWR | os.O_APPEND | os.O_CREAT)

print(fd)
print(type(fd))
print


txt = "My name is Shin"
txt_length = os.write(fd, txt.encode()) # txt를 인코딩하고 fd에 write하겠다 
print(txt_length)
print(type(txt_length))
 
 
os.close(fd)

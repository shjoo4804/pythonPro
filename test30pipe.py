#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
print("os pipe")

fd_receive, fd_transmit = os.pipe() #pipe로 두 개가 연결되어 있어서 

print("fd_receive",fd_receive)
print("fd_transmit",fd_transmit)

data = "shin123456"
data_length = os.write(fd_transmit, data.encode()) # fd_transmit에 write하고
print("data_length",data_length)

print(os.read(fd_receive, 1024)) #fd_receive에서 read가 가능함 



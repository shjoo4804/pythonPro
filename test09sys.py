#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys #lib

print('python ::: sys')

# terminal :  python test09sys.py 11 22 33 ...
print("sys.argv:", sys.argv)
print("len(sys.argv):", len(sys.argv))


if len (sys.argv)>3:
	for i in range(len(sys.argv)):
		print(sys.argv[i])


print("input name:")
name = sys.stdin.readline()
print("name:", name)

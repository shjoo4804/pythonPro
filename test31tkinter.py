#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import tkinter #python3.x
#import Tkinter #python 2.x

from tkinter import *  # tkinter.~~ 로 쓰지 않아도 되게됨

print("python GUI tkinter")

top = Tk()  #container
lst = ['java', 'python', 'android', 'linux']

lstBox = Listbox(top)
def onselected(event):
	print("onselected", event.widget.curselection()[0]) 
	#목록하나를 누르면 인덱스를 찍음.. #getIndex를 넣어서 목록의 글자를 뽑을수도 있음

lstBox.bind("<<ListboxSelect>>", onselected)

for item in lst:
	lstBox.insert(0,item)
lstBox.pack()

top.mainloop()

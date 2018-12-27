#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import tkinter #python3.x
#import Tkinter #python 2.x

from tkinter import *  # tkinter.~~ 로 쓰지 않아도 되게됨

print("python GUI tkinter")

class ListPage:
	def __init__(self) :
		top = Tk()  #container
		top.title("list")
		top.geometry("150x100+550+100")
		top.resizable(False, False)
		
		lst = ['java', 'python', 'android', 'linux']

		lstBox = Listbox(top, selectbackground="orange")
		for item in lst:
			lstBox.insert(0,item)
			
		def onselected(event):
			w = event.widget
			index = int(w.curselection()[0])
			print("onselected", index)  #인덱스
			print("onselected", w.get(index))  #값
		lstBox.bind("<<ListboxSelect>>", onselected)
		lstBox.pack()
		mainloop()


class InsertPage:
	def __init__(self):
		top = Tk()  #container
		top.title("insert")
		top.geometry("250x100+300+100") #가로크기x세로크기 + 가로위치+세로위치
		top.resizable(False, False)  # 사이즈 고정

		fnameLabel = Label(top, text="fname:")
		lnameLabel = Label(top, text="lname:")
		fnameLabel.grid(row=0) # grid layout
		lnameLabel.grid(row=1)
		
		# nameLabel.pack(side=LEFT) #하나만 쓸때

		fnameEntry = Entry(top) # Entry는 text속성이 없음
		lnameEntry = Entry(top) 
		fnameEntry.grid(row=0, column=1)
		lnameEntry.grid(row=1, column=1)
		
		#nameEntry.pack(side=RIGHT)

		def onclick():
			print("onclick", fnameEntry.get(), lnameEntry.get())
			ListPage()

		okButton = Button(top, text="ok", command=onclick)
		okButton.grid(row=2,column=1)
		#okButton.pack(side=BOTTOM)


		mainloop()


#test
#ListPage()
InsertPage()

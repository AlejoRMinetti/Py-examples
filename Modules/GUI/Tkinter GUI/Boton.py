#!/usr/bin/python
import tkinter

top = tkinter.Tk()

def helloCallBack():
	B.flash()

B = tkinter.Button(top, text ="Hello", command = helloCallBack)
B.pack()
top.mainloop()
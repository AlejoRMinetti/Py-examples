#!/usr/bin/env python
import tkinter as tk
import pyautogui

def MouseCuadricular():
	for i in range(2):
		pyautogui.moveRel(100, 0, duration=0.25)
		pyautogui.moveRel(0, 100, duration=0.25)
		pyautogui.moveRel(-100, 0, duration=0.25)
		pyautogui.moveRel(0, -100, duration=0.25)

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.RatonButton = tk.Button(self, text='Mover Raton',command = MouseCuadricular)
		self.RatonButton.grid()

app = Application()
app.master.title('Mover Mouse application')
app.mainloop()
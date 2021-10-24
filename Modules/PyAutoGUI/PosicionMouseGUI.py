# Muestra posicion del mouse
#import tkinter as tk
import pyautogui
import time
'''
class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.PosicionRaton = tk.Label(self, text='Mover Raton')


app = Application()
app.master.title('Mover Mouse application')
app.mainloop()
'''
while True:
    print(pyautogui.position())
    time.sleep(1) # espera en segundos
	#app.PosicionRaton.Label.Label(self, text= pyautogui.position())


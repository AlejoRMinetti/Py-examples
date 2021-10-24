#example mover mouse
import pyautogui

for i in range(2):
    pyautogui.moveTo(10, 10, duration=0.25)
    pyautogui.moveTo(10, 1000, duration=0.25)
    pyautogui.moveTo(1000, 10, duration=0.25)
    pyautogui.moveTo(10, 1000, duration=0.25)


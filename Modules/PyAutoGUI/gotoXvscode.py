#ejemplo captura pantalla con vscode abierto y mueve cursor a la X
import pyautogui

print("Guardando captura de pantalla en PruebaPantalla.png")
#pantalla con el vscode abierto
pantalla = pyautogui.screenshot("PruebaPantalla.png") # pantalla a variable y se guarda en archivo
print("localizando X de vscode...")
# localizamos la X del vscode y movemos el cursor ahi
botonX = pyautogui.locateOnScreen('XvscodeASUS.png')
print(botonX) # devuelve None si no lo encuentra
print("posicion para el mouse:")
puntoCursor = pyautogui.center(botonX)
print(puntoCursor)
pyautogui.moveTo(puntoCursor, duration=0.5)

# version resumida:
#pyautogui.moveTo('Xvscode.png', duration=0.5)
# PyQt5 Python app with Qt-Designer

Probado usando python 3.9 en windows.
Si tenes una version superior usar: 
```
py -3.9 main.py
```

Intalar dependencias:
```
py -3.9 -m pip install PyQt5
py -3.9 -m pip install Pyside2
```
Este ultimo instala el Qt Designer para diseñar la app en forma grafica

## Usar Qt Designer
El ejecutable se encuentra en:

#### usando Pyside2:
```
C:\Users\alejo\AppData\Local\Programs\Python\Python39\Lib\site-packages\PySide2\designer.exe
```

## Convertion from .ui to .py
```
"C:\Python37\Scripts\pyside2-uic.exe" mainwindow.ui > ui_mainwindow.py
```
# PyQt5 Python app with Qt-Designer

Probado corriendo python 3.9 en windows.
### Si tenes una version superior usar:
`py -3.9 app.py` 

Intalar dependencias:
```
py -3.9 -m pip install PyQt5
py -3.9 -m pip install PyQt5-tools
```
Este ultimo instala el Qt Designer para diseñar la app en forma grafica
## Usar Qt Designer
El ejecutable se encuentra en:
```
C:\Users\tu-user\AppData\Local\Programs\Python\Python39\Lib\site-packages\qt5_applications\Qt\bin\designer.exe
```
Crear la ui usando Main Windows

## Instalar app para tenerla como un ejecutable
```
py -3.9 -m pip install pyinstaller
pyinstaller --clean --onefile --windowed app.py
```
El ejecutable debe estar en el mismo directorio con el .ui
## Convertion from .ui to .py
"C:\Python37\Scripts\???.exe" mainwindow.ui > ui_mainwindow.py

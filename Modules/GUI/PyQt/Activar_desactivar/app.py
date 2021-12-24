import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('activar-desactivar.ui', self)
        self.btn_activar.clicked.connect(self.activar)
        self.btn_desactivar.clicked.connect(self.desactivar)

    def activar(self):
        self.btn_desactivar.setEnabled(True)
        self.btn_activar.setEnabled(False)
        self.label.setText('Activado!')

    def desactivar(self):
        self.btn_desactivar.setEnabled(False)
        self.btn_activar.setEnabled(True)
        self.label.setText('Desactivado!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
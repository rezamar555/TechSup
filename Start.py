import sys

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QPen, QBrush, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QMainWindow

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "TechSup"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.showMaximized()
        self.show()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black))
        painter.drawRect(20,20,900,500)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())

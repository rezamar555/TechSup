import sys
#Project name and libraries
from PyQt5 import uic, QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QPen, QBrush, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QMainWindow

#class Window(QMainWindow):
class Canvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()

        #pixmap = QtGui.QPixmap(600,300)
        #self.setPixmap(pixmap)

    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return # Ignore the first time.

            #def paintEvent(self, e):
            #    painter = QPainter(self)
            painter = QtGui.QPainter(self.pixmap())
            p = painter.pen()
            p.setColor(self.pen_color)
            painter.setPen(p)
            #painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
            painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
            painter.setBrush(QBrush(Qt.black, Qt.Dense1Pattern))
            painter.drawRect(20,20,900,500)
            painter.end()
            self.update()

            self.last_x = e.x()
            self.last_y = e.y()

            def mouseReleaseEvent(self, e):
                self.last_x = None
                self.last_y = None

COLORS = [
# 17 undertones https://lospec.com/palette-list/17undertones
'#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
'#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
'#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]

class QPaletteButton(QtWidgets.QPushButton):

    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24,24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = "TechSup"
        self.canvas = Canvas()
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.showMaximized()

        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)
        l.addLayout(palette)

        self.setCentralWidget(w)

    def paintEvent(self, e):
        '''painter = QPainter(self)
        painter = setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black, Qt.Dense1Pattern))
        painter.drawRect(20,20,900,500)'''
        painter = QPainter(self) ##temp
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black, Qt.Dense1Pattern))
        painter.drawRect(20,20,900,500) ##temp


    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

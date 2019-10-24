import sys
#Project name and libraries
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QPen, QBrush, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QMainWindow

class Window(QMainWindow):
#class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "TechSup"
        self.InitWindow()

        '''def InitWindow(self):            ###Draw insert of lines
            self.setWindowTitle(self.title)
            self.setGeometry(300, 300, 280, 270)
            self.show()'''

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.showMaximized()
        self.show()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        #self.drawLines(painter) ##black board
        painter.setBrush(QBrush(Qt.black))
        painter.drawRect(20,20,900,500)
        '''qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()'''

    '''def drawLines(self, qp):                 ###Draw Functions in QWidget
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)'''


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())

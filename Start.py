import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('Inicial')

    btn = QPushButton('Este es un Button', w)
#    btn.setToolTip('This is a <b>QPushButton</b> widget') # As Reference
    btn.move(150, 50)

    btn.clicked.connect(QCoreApplication.instance().quit)

    w.resize(500, 500)
    w.show()

    sys.exit(app.exec_())


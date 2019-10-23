import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('Inicial')
    w.move(QDesktopWidget().availableGeometry().center() - w.frameGeometry().center())
    w.resize(500, 500)
    w.show()

    sys.exit(app.exec_())

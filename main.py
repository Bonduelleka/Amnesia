import sys
import random

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, qp):
        qp = QPainter()
        qp.begin(self)
        size = random.choice(range(5, 150))
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(randint(6, 700) - size // 2, randint(6, 900) - size // 2, size, size)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
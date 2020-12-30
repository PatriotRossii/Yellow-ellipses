import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.timer = QTimer()
        self.ellipses = []

        self.init_signals()

    def init_signals(self):
        self.timer.timeout.connect(self.add_ellipse)
        self.pushButton.clicked.connect(self.start_timer)

    def start_timer(self):
        self.timer.start(500)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        for ellipse in self.ellipses:
            self.draw_ellipse(qp, ellipse)

        qp.end()

    def add_ellipse(self):
        self.ellipses.append(
            (
                random.randint(0, self.width()),
                random.randint(0, self.height()),
                random.randint(0, 250),
                random.randint(0, 250),
            )
        )
        self.repaint()

    def draw_ellipse(self, qp, ellipse):
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(*ellipse)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

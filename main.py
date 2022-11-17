from random import randint
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI import Ui_Form


class RandomCircles(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.to_repaint = False

        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_click)
        self.setFixedSize(600, 600)

    def btn_click(self):
        self.to_repaint = True
        self.update()

    def paintEvent(self, event):
        if self.to_repaint:
            self.draw_circle(QPainter(self))

    @staticmethod
    def draw_circle(qp):
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        qp.setBrush(QColor(r, g, b))

        s = randint(10, 100)
        x, y = randint(0, 600 - s), randint(10, 600 - s)
        qp.drawEllipse(x, y, s, s)


def except_hook(c, e, t):
    sys.__excepthook__(c, e, t)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomCircles()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

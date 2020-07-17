import sys
from PyQt5.Qt import *


class App(QApplication):
    def notify(self, a0: QtCore.QObject, a1: QtCore.QEvent) -> bool:


app = App(sys.argv)

window = QWidget()

btn = QPushButton(window)
btn.setText("按钮1")
btn.move(100, 200)


def cao():
    print("按钮被点击了")


btn.pressed.connect(cao)

window.show()

sys.exit(app.exec_())


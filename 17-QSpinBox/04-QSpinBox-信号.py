import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox-信号")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        sb = QSpinBox(self)
        sb.resize(100, 25)
        sb.move(100, 100)

        sb.valueChanged[int].connect(lambda val: print("数值发生了改变", val))
        sb.valueChanged[str].connect(lambda val: print("数值发生了改变", val))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

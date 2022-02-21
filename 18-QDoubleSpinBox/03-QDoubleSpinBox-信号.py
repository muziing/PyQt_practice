import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDoubleSpinBox-信号")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        dsb = QDoubleSpinBox(self)
        dsb.move(100, 100)
        dsb.resize(150, 30)

        dsb.valueChanged.connect(lambda val: print(val, type(val)))
        dsb.valueChanged[str].connect(lambda val: print(val, type(val)))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

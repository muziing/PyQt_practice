import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        sb = QSpinBox(self)
        sb.resize(100, 25)
        sb.move(100, 100)

        # -----设置最大值最小值-------
        # sb.setMaximum(180)
        # sb.setMinimum(18)
        sb.setRange(18, 180)
        print(sb.maximum())
        print(sb.minimum())

        # -------数值循环---------
        print("wrapping默认值为", sb.wrapping())  # 默认为 False
        sb.setWrapping(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

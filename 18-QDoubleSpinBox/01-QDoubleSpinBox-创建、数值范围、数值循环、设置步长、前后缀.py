import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDoubleSpinBox")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        dsb = QDoubleSpinBox(self)
        dsb.move(100, 100)
        dsb.resize(200, 30)

        # ----------数值范围------------
        # dsb.setMaximum(200.0)
        # dsb.setMinimum(50.0)
        dsb.setRange(50.0, 200.0)  # 默认范围0.00-99.99

        # ----------数值循环----------
        dsb.setWrapping(True)  # 打开循环

        # ----------步长-----------
        dsb.setSingleStep(0.02)  # 默认值为1

        # ---------前后缀---------
        dsb.setPrefix("前缀")
        dsb.setSuffix("后缀")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

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

        # -------步长设置------------
        sb.setSingleStep(3)  # 设置单步步长
        # print(sb.singleStep())

        # -------前缀和后缀-------
        # sb.setPrefix("周")  # 设置前缀作为展示
        # print(sb.prefix())
        sb.setRange(1, 12)
        sb.setSuffix("月")  # 设置后缀
        print(sb.suffix())

        # ------进制设置--------
        sb.setDisplayIntegerBase(10)  # 设置基数（进制）
        # print(sb.displayIntegerBase())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

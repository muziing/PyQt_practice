from PyQt5.Qt import *
import sys

"""
编辑日期和时间的单行文本框
既可以用剪头调节，也可以用键盘编辑输入
可以单独调节某个部分
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDateTimeEdit")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        dte = QDateTimeEdit(self)
        dte.move(100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

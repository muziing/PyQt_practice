import sys

from PyQt5.Qt import *


# ------自定义展示格式--------
class MySpinBox(QSpinBox):
    def textFromValue(self, v: int) -> str:
        # 修改的只是展示效果，真实数值没有变
        print(v)
        return str(v) + "*" + str(v)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        sb = MySpinBox(self)
        sb.resize(100, 25)
        sb.move(100, 100)

        # ------值的设置与获取-------
        sb.setValue(20)  # 如果设置的数值超过范围，则自动取范围边界值
        sb.value()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

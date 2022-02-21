import sys

from PyQt5.Qt import *


# -------自定义展示格式---------
class MyDoubleSpinBox(QDoubleSpinBox):
    def textFromValue(self, v: float) -> str:
        # 修改的只是展示效果，真实数值没有变
        print("v", v)
        return str(v) + "**"


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDoubleSpinBox")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        dsb = MyDoubleSpinBox(self)
        dsb.move(100, 100)
        dsb.resize(200, 30)

        # -------最小值特殊文本------
        dsb.setSpecialValueText("达到最小值啦！")

        # ------设置小数位数-------
        dsb.setDecimals(3)  # 默认两位小数

        # ------设置数值----------
        dsb.setValue(66.666)  # 如果设置的小数位数过多，会按照真实的位数四舍五入

        # -----获取数值--------
        print(dsb.value())  # 获取数值
        print("cleanText", dsb.cleanText())  # 不包含任何前后缀、前导尾随空格
        print(dsb.lineEdit().text())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

import sys

from PyQt5.Qt import *


class MyASB(QAbstractSpinBox):
    """自定义的子类，实现限制数值范围在0~9的功能"""

    def __init__(self, parent, num: int = 0):
        super().__init__(parent)
        self.current_num = 0
        self.lineEdit().setText(f"{num}")

    def stepEnabled(self) -> "QAbstractSpinBox.StepEnabled":
        # 目标：限制用户通过箭头输入数值在0-9范围内
        try:
            self.current_num = int(self.text())
        except ValueError:
            self.current_num = 0
        if self.current_num == 0:
            return QAbstractSpinBox.StepUpEnabled
        elif self.current_num == 9:
            return QAbstractSpinBox.StepDownEnabled
        elif self.current_num < 0 or self.current_num > 9:
            return QAbstractSpinBox.StepNone
        else:
            return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, steps: int) -> None:
        self.current_num = self.current_num + steps
        self.lineEdit().setText(str(self.current_num))
        # 仅限于用户通过键盘方向键或者鼠标点击上下箭头改变数值
        # 此时用户还可以通过键盘数字键输入0~9之外的数值


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSpinBox")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        asb = MyASB(self)
        self.asb = asb
        asb.resize(120, 30)
        asb.move(150, 100)

        test_btn = QPushButton("测试按钮", self)
        test_btn.move(300, 100)
        test_btn.clicked.connect(self.btn_test)

    def btn_test(self):
        print(self.asb.text())  # 获取文本
        self.asb.lineEdit().setText("888")  # 设置文本
        # 不受MyASB的0~9限制，仍可设置为888


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

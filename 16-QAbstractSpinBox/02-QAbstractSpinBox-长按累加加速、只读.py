import sys

from PyQt5.Qt import *


class MyASB(QAbstractSpinBox):
    def __init__(self, parent, num: int = 0):
        super().__init__(parent)
        self.current_num = 0
        self.lineEdit().setText(f"{num}")

    def stepEnabled(self) -> "QAbstractSpinBox.StepEnabled":
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, steps: int) -> None:
        self.current_num = self.current_num + steps
        self.lineEdit().setText(str(self.current_num))


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSpinBox-长按累加加速")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        asb = MyASB(self)
        asb.resize(120, 30)
        asb.move(150, 100)

        # -------累加加速--------
        asb.setAccelerated(True)  # 加速
        print(asb.isAccelerated())

        # ------只读---------
        asb.setReadOnly(True)  # 不能通过键盘直接修改数字，但可以通过小箭头控制数字增减
        print(asb.isReadOnly())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

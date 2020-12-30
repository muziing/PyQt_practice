from PyQt5.Qt import *
import sys


class MyASB(QAbstractSpinBox):
    def __init__(self, parent, num: int = 0):
        super().__init__(parent)
        self.current_num = 0
        self.lineEdit().setText(f'{num}')

    def stepEnabled(self) -> 'QAbstractSpinBox.StepEnabled':
        # 目标：限制在0-9范围内
        try:
            self.current_num = int(self.text())
        except TypeError:
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


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSpinBox")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        asb = MyASB(self)
        asb.resize(120, 30)
        asb.move(150, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

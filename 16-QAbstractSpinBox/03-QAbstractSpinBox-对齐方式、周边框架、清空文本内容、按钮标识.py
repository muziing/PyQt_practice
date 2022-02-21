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
        self.setWindowTitle("QAbstractSpinBox")
        self.resize(500, 500)
        self.move(450, 250)
        self.setup_ui()

    def setup_ui(self):
        asb = MyASB(self)
        asb.resize(120, 30)
        asb.move(150, 100)

        # -------对齐方式--------
        asb.setAlignment(Qt.AlignHCenter)  # 水平居中

        # ------周边框架-------
        print(asb.hasFrame())  # 默认有边框
        asb.setFrame(False)  # 手动删除边框

        # -----清空内容------
        asb.clear()

        # -----按钮标识-----
        asb.setButtonSymbols(QAbstractSpinBox.UpDownArrows)  # 上下箭头（默认值）
        # asb.setButtonSymbols(QAbstractSpinBox.PlusMinus)  # 加号减号
        # asb.setButtonSymbols(QAbstractSpinBox.NoButtons)  # 无按钮


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

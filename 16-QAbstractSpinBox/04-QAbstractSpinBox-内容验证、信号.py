import sys

from PyQt5.Qt import *


class MyASB(QAbstractSpinBox):
    def __init__(self, parent, num: int = 20):
        super().__init__(parent)
        self.current_num = 20
        self.lineEdit().setText(f"{num}")

    def stepEnabled(self) -> "QAbstractSpinBox.StepEnabled":
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, steps: int) -> None:
        self.current_num = self.current_num + steps
        self.lineEdit().setText(str(self.current_num))

    def validate(self, input: str, pos: int):
        # 18 - 180
        try:
            num = int(input)
            if num < 18:
                return QValidator.Intermediate, input, pos
            elif num <= 180:
                return QValidator.Acceptable, input, pos
            else:
                return QValidator.Invalid, input, pos
        except Exception:
            return QValidator.Invalid, input, pos

    def fixup(self, input: str) -> str:
        self.current_num = 18
        return "18"


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSpinBox-内容验证")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        asb = MyASB(self)
        asb.resize(120, 30)
        asb.move(150, 100)
        te = QTextEdit(self)
        te.resize(200, 80)
        te.move(150, 200)
        te.setPlaceholderText("将焦点移到这里以实现结束SpinBox的编辑，调用fixup方法")

        def te_cao():
            te.setText("SpinBox已经结束编辑！")

        asb.editingFinished.connect(te_cao)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

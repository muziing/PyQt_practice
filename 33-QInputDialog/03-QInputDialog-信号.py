import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog-信号")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        input_d = QInputDialog(self)

        """
        intValueChanged(int value)
        intValueSelected(int value)
        doubleValueChanged(double value)
        doubleValueSelected(double value)
        textValueChanged(text_str)
        textValueSelected(text_str)
        """
        input_d.setInputMode(QInputDialog.IntInput)
        input_d.intValueChanged.connect(lambda val: print("数值发生了改变", val))
        input_d.intValueSelected.connect(lambda val: print("最终选择了", val))

        input_d.open()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

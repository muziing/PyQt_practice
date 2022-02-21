import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSlider")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # print(QAbstractSlider.__subclasses__())
        label = QLabel(self)
        label.setText("0")
        label.move(300, 100)
        label.resize(100, 30)
        sd = QSlider(self)
        sd.move(100, 100)
        sd.valueChanged.connect(lambda val: label.setText(str(val)))

        # ----------数值范围----------
        sd.setMaximum(100)
        sd.setMinimum(50)
        # print(sd.maximum())
        # print(sd.minimum())

        # ---------当前数值-----------
        sd.setValue(88)
        # print(sd.value())

        # ----------步长------------
        sd.setSingleStep(5)  # 键盘方向键步长，默认为1
        sd.setPageStep(20)  # 键盘 PgUP PgDn步长，默认为10


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

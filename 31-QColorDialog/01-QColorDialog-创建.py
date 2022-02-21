import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QColorDialog")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        cd = QColorDialog(QColor(20, 154, 151), self)  # 可以传入创建时的默认颜色
        cd.setWindowTitle("选择颜色")
        cd.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

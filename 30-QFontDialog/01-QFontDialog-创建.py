import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton("测试按钮", self)
        btn.move(100, 100)
        btn.clicked.connect(lambda: fd.open())

        font = QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        fd = QFontDialog(font, self)  # 可以在创建时传入一个QFont对象作为默认字体


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

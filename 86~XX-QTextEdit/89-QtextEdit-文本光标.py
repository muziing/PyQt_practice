from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit-文本光标")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        te = QTextEdit(self)
        self.te = te

        test_btn = QPushButton("测试按钮", self)
        test_btn.move(350, 140)
        test_btn.clicked.connect(self.test_btn_cao)

    def test_btn_cao(self):
        # print(self.te.document())
        print(self.te.textCursor())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

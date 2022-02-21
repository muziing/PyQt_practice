import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit-占位文本")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        self.te = QTextEdit(self)
        self.te.resize(200, 200)
        self.占位文本的提示()

    def 占位文本的提示(self):
        self.te.setPlaceholderText("请输入信息")  # 只有在QTextEdit框为空时才显示
        print(self.te.placeholderText())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

from PyQt5.Qt import *
import sys

"""
setBlockCharFormat(QTextCharFormat)  设置要格式化的当前块（或选择中包含的所有块）的块char格式
setBlockFormat(QTextBlockFormat)  设置当前块的块格式（或选中包含的所有块）以进行格式化
setCharFormat(QTextCharFormat)  将光标的当前字符格式设置为给定格式。如光标有选择，则给定格式应用于当前选择
mergeBlockCharFormat(QTextCharFormat)  合并当前块的char格式
mergeBlockFormat(QTextBlockFormat)  合并当前块的格式
mergeCharFormat(QTextCharFormat)  合并当前字符格式
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit-文本光标-格式操作")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

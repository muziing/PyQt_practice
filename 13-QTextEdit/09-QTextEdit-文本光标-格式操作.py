import sys

from PyQt5.Qt import *

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
        te = QTextEdit(self)
        self.te = te
        te.resize(400, 400)
        test_btn = QPushButton("测试按钮", self)
        test_btn.move(410, 140)
        test_btn.clicked.connect(self.test_btn_slot)

    def test_btn_slot(self):
        tc = self.te.textCursor()  # 创建文本光标

        tcf = QTextCharFormat()
        tcf.setFontFamily("Microsoft YaHei")
        tcf.setFontPointSize(30)  # 设置字体大小
        tcf.setFontOverline(True)  # 设置上划线
        tcf.setFontUnderline(True)  # 设置下划线

        # tc.setBlockCharFormat(tcf)  # 把当前块的格式设置成tcf的样式

        tbf = QTextBlockFormat()
        tbf.setAlignment(Qt.AlignCenter)  # 中心对齐
        # tbf.setIndent(2)  # 缩进

        tc.setBlockFormat(tbf)  # 设置当前块格式


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

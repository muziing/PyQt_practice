import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit-插入文本块")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        te = QTextEdit(self)
        self.te = te
        te.setText("abc")
        te.resize(400, 400)
        test_btn = QPushButton("测试按钮", self)
        test_btn.move(410, 140)
        test_btn.clicked.connect(self.test_btn_cao)

    def test_btn_cao(self):
        self.cursor_insert_block()

    def cursor_insert_block(self):
        tc = self.te.textCursor()  # 创建光标对象

        tbf = QTextBlockFormat()  # QTextBlockFormat对象里面可以设置各种文本段落格式
        tbf.setAlignment(Qt.AlignRight)  # 右对齐
        tbf.setRightMargin(100)  # 设置右对齐
        # tbf.setIndent(1)  # 缩进1个Tab

        tcf = QTextCharFormat()  # QTextCharFormat里面可以设置字体等格式
        tcf.setFontFamily("Microsoft YaHei")
        tcf.setFontItalic(True)  # 设置为斜体
        tcf.setFontPointSize(60)

        tc.insertBlock(tbf, tcf)  # 插入文本块
        self.te.setFocus()  # 使文本输入框重新获得焦点，方便观察光标位置的变化


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

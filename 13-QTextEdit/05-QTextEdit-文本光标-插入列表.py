import sys

from PyQt5.Qt import *


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
        te.setText("abc")
        test_btn = QPushButton("测试按钮", self)
        test_btn.move(350, 140)
        test_btn.clicked.connect(self.test_btn_cao)

    def test_btn_cao(self):
        # self.cursor_insert1()  # 插入方法
        self.cursor_insert2()  # 创建方法

    def cursor_insert1(self):
        tc = self.te.textCursor()  # 创建一个光标对象

        # ---------插入--------

        # tc.insertList(QTextListFormat) -> QTextList
        # 在当前位置插入一个新块，并使其成为具有给定格式的新创建列表的第一个列表项。返回创建的列表

        # tc.insertList(QTextListFormat.Style) -> QTextList
        # 在当前位置插入一个新块，并使其成为具有给定格式的新创建列表的第一个列表项。返回创建的列表

        """
        QTextListFormat.ListDisc  # 样式为圆圈
        QTextListFormat.ListCircle  # 样式为空心圆圈
        QTextListFormat.ListSquare  # 样式为方块
        QTextListFormat.ListDecimal  # 小写阿拉伯数字，最大4999
        QTextListFormat.ListLowerAlpha  # 小写拉丁字符，按字母顺序
        QTextListFormat.ListUpperAlpha  # 大写拉丁字符，按字母顺序
        QTextListFormat.ListLowerRoman  # 小写罗马数字，最大4999
        QTextListFormat.ListUpperRoman  # 大写罗马数字，最大4999
        """
        tc.insertList(QTextListFormat.ListSquare)  # 样式为方块

    def cursor_insert2(self):
        tc = self.te.textCursor()  # 创建一个光标对象

        # ---------创建--------

        # tc.createList(QTextListFormat) -> QTextList
        # 创建并返回具有给定格式的新列表，并使当前段落的光标位于第一个列表项之中

        # tc.createList(QTextListFormat.style) -> QTextList
        # 创建并返回具有给定格式的新列表，并使当前段落的光标位于第一个列表项之中

        tc.createList(QTextListFormat.ListCircle)

        tlf = QTextListFormat()
        tlf.setIndent(3)  # 设置列表的缩进
        tlf.setNumberPrefix("<<")  # 设置前缀（只有在列表前有数字时才生效）
        tlf.setNumberSuffix(">>")  # 设置后缀（只有在列表前有数字时才生效）
        tlf.setStyle(QTextListFormat.ListDecimal)  # 样式为阿拉伯数字
        tc.createList(tlf)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

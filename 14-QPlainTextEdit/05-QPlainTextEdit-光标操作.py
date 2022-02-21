import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPLainTextEdit-光标操作")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        pte = QPlainTextEdit(self)
        pte.move(50, 50)
        pte.resize(400, 400)

        with open(
            "./01-QPlainTextEdit-创建、占位提示文本、只读、字符格式.py", "r", encoding="UTF8"
        ) as f:
            pte.appendPlainText(f.read())

        # tc = pte.textCursor()  # 获取光标对象
        # tc.insertImage("../Icons/html_96px.ico")  # 虽然有对应的方法，但是PlainTextEdit并不支持
        pte.setCursorWidth(15)  # 设置光标宽度

        tc = pte.cursorForPosition(QPoint(100, 60))  # 获取指定位置的光标对象，这个光标与真实存在的光标不同
        tc.insertText("https://muzing.top")  # 在(100, 60)的位置已经插入；Text，但真实的光标仍在结尾位置

        pte.cursorRect()  # 获取文本光标矩形，返回一个QRect，也可以传入一个（通过cursorForPosition）指定的光标
        pte.moveCursor(QTextCursor.Up, QTextCursor.KeepAnchor)  # 光标向上移动一行，并选中


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

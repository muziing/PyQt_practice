import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainTextEdit")
        self.resize(600, 600)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        pte = QPlainTextEdit(self)
        pte.resize(500, 500)
        pte.move(50, 20)

        btn1 = QPushButton("放大", self)
        btn2 = QPushButton("测试按钮2", self)
        btn1.move(320, 540)
        btn2.move(420, 540)

        with open(
            "./01-QPlainTextEdit-创建、占位提示文本、只读、字符格式.py", "r", encoding="UTF8"
        ) as f:
            pte.appendPlainText(f.read())

        # ---------放大缩小---------
        btn1.clicked.connect(
            lambda: pte.zoomIn(1)
        )  # zoomIn()中的int值为正则放大，为负则缩小，绝对值越大变化越快

        # --------滚动保证光标可见-----
        """比如正在编辑一个长文本的中间段落，光标位置不变，去临时阅读一下文首的内容后，期望直接返回光标所在位置继续编辑"""
        pte.setCenterOnScroll(True)  # 可以滚动到中间位置，会在末尾增加一些空白来使得最后一行文本也能处于Edit的中间

        def test_slot():
            # pte.centerCursor()  # 尽可能使当前光标所在行滚动到整个Edit框中间
            pte.ensureCursorVisible()  # 确保Edit中显示光标，如果光标已经在显示范围内则不滚动，否则进行centerCursor()的滚动
            pte.setFocus()  # 重新获得焦点以显示光标

        btn2.clicked.connect(test_slot)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

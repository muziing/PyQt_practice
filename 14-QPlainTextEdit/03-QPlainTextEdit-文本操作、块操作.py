import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainTextEdit-文本操作")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        pte = QPlainTextEdit(self)
        pte.move(100, 100)
        pte.resize(300, 300)
        test_btn = QPushButton("测试按钮", self)
        test_btn.move(20, 20)

        # ------文本操作-------
        pte.setPlainText("这是一行PlainText")
        # pte.insertPlainText("插入的PlainText")  # 在光标位置插入
        # pte.appendPlainText("<a href='https://muzing.top'muzing的博客</a>")
        # pte.appendHtml("<a href='https://muzing.top'muzing的博客</a>")  # 貌似这个方法已经弃用
        print(pte.toPlainText())

        # ------块操作---------
        def btn_test():
            print(pte.blockCount())
            pte.setMaximumBlockCount(5)  # 限制最大块数量，输入新的块会顶掉最上面的块

        test_btn.clicked.connect(btn_test)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

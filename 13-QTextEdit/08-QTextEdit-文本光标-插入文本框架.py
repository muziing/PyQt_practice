import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit-插入文本框架")
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
        self.cursor_insert_frame()

    def cursor_insert_frame(self):
        tc = self.te.textCursor()  # 创建光标对象

        tff = QTextFrameFormat()  # 设置框架格式
        tff.setBorder(10)  # 边框10像素宽度
        tff.setBorderBrush(QColor(100, 50, 50))
        tff.setRightMargin(30)  # 右侧间距

        # tc.insertFrame(tff)

        # 根框架
        doc = self.te.document()
        root_frame = doc.rootFrame()
        root_frame.setFrameFormat(tff)  # 设置根框架的样式


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

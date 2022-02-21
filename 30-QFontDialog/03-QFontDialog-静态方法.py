import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog-静态方法")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton("测试按钮", self)
        btn.move(100, 100)
        label = QLabel(self)
        label.move(100, 200)
        label.setText("muzing")

        def font_sel_1():
            result = QFontDialog.getFont(self)  # 返回一个元组，(QFont, bool) 用户点击确定键则为True
            if result[1]:
                label.setFont(result[0])
                label.adjustSize()

        def font_sel_2():
            font = QFont()
            font.setFamily("宋体")
            font.setPointSize(22)
            result = QFontDialog.getFont(
                font, self, "选择一个字体", QFontDialog.ScalableFonts
            )
            if result[1]:
                label.setFont(result[0])
                label.adjustSize()

        # btn.clicked.connect(font_sel_1)
        btn.clicked.connect(font_sel_2)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

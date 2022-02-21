import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel("muzing", self)
        label.move(100, 100)
        label.setStyleSheet("background-color: cyan;")
        label.resize(200, 200)  # 手动设置大小
        # label.adjustSize()  # 根据内容自适应大小

        # ---------对齐----------
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # 手动设置靠右居中对齐
        # ---------缩进----------
        label.setIndent(20)  # 文本缩进，仅左右
        # ---------间距----------
        label.setMargin(20)  # 设置内容范围的边框与控件边框的间距，上下左右


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

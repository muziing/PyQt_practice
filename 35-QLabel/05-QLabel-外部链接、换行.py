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
        label = QLabel(self)
        label.move(100, 100)
        label.resize(200, 200)
        label.setText("muzing的个人博客\n链接为 <a href='https://muzing.top'>https://muzing.top</a>")
        label.setTextFormat(Qt.RichText)
        label.setStyleSheet("background-color: cyan;")

        # ---------链接------------
        label.setOpenExternalLinks(True)
        print(label.openExternalLinks())

        # ---------换行------------
        label.setWordWrap(True)  # 如果内容超出控件宽度，则以单词为分割，进行换行
        print(label.wordWrap())

        # ---------文本竖排的小技巧-----------
        # label.setText("\n".join("123456789"))  # 貌似已经失效


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

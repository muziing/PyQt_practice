import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel-信号")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.move(100, 100)
        label.setText(
            "muzing的个人博客链接为 <a href=https://muzing.top>https://muzing.top</a>"
        )
        label.setTextFormat(Qt.RichText)
        # label.setOpenExternalLinks(True)
        label.setOpenExternalLinks(False)

        # label.linkHovered.connect(lambda val: print("鼠标指向了链接", val))
        label.linkActivated.connect(
            lambda val: print("鼠标点击了链接", val)
        )  # 仅在 OpenExternalLinks(False)时有效


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel-内容缩放")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.move(100, 100)
        label.resize(80, 80)
        label.setPixmap(QPixmap("../Icons/OS_Ubuntu_128px.ico"))
        label.setScaledContents(True)  # 设置内容缩放


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

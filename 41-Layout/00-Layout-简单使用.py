import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理器")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        lb1 = QLabel()
        lb1.setStyleSheet("background-color: cyan;")
        lb2 = QLabel()
        lb2.setStyleSheet("background-color: yellow;")
        lb3 = QLabel()
        lb3.setStyleSheet("background-color: red;")

        v_layout = QVBoxLayout()
        v_layout.addWidget(lb1)
        v_layout.addWidget(lb2)
        v_layout.addWidget(lb3)
        v_layout.setContentsMargins(15, 15, 15, 15)  # 设置外边距，左上右下
        v_layout.setSpacing(30)  # 设置内边距

        self.setLayout(v_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

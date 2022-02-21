import sys

from PyQt5.Qt import *

"""
QSS Qt Style Sheet Qt样式表
可以类比CSS，但没有CSS强大：选择器少、属性少、有些属性仅适用部分控件
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS初体验")
        self.resize(600, 600)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        box_1 = QWidget(self)
        box_2 = QWidget(self)
        # box_1.setStyleSheet("QPushButton {background-color: orange;}")
        # box_2.setStyleSheet("background-color: cyan;")

        label_1 = QLabel("标签1", box_1)
        label_1.move(50, 50)
        btn_1 = QPushButton("按钮1", box_1)
        btn_1.move(150, 50)

        label_2 = QLabel("标签2", box_2)
        label_2.move(50, 50)
        btn_2 = QPushButton("按钮2", box_2)
        btn_2.move(150, 50)

        v_layout = QVBoxLayout()
        self.setLayout(v_layout)

        v_layout.addWidget(box_1)
        v_layout.addWidget(box_2)

        self.other_btn = QPushButton("按钮3")
        self.other_btn.show()

        self.setStyleSheet("QPushButton {background-color: orange;}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

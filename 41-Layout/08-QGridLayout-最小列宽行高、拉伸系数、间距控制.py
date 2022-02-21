import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        gl = QGridLayout()
        self.setLayout(gl)

        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color: red;")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color: yellow;")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color: cyan;")

        gl.addWidget(label1, 0, 0)
        gl.addWidget(label2, 0, 1)
        gl.addWidget(label3, 1, 0, 1, 2)

        gl.setColumnMinimumWidth(0, 100)  # 设置最小列宽
        gl.setRowMinimumHeight(0, 100)  # 设置第1行的最小行高

        gl.setColumnStretch(0, 2)  # 设置列拉伸系数
        gl.setColumnStretch(1, 1)
        gl.setRowStretch(0, 1)  # 设置行拉伸系数
        gl.setRowStretch(1, 2)

        print(gl.spacing())  # 默认水平垂直间距相等且为7
        gl.setVerticalSpacing(18)  # 设置垂直间距，默认值为7
        print(gl.verticalSpacing())  # 获取垂直间距，此时已经为18
        # gl.setSpacing(30)  # 同时设置水平垂直间距


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

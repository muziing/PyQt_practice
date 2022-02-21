import sys

from PyQt5.Qt import *

# 当缩小到一定程度后，空白伸缩因子会不遵守伸缩比例而一直缩小到最小宽度为止，和控件不同
# 若一组控件中，某些控件伸缩因子为0（默认值），而其他非零，则这些控件将始终以最小显示


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QBoxLayout")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        lb1 = QLabel("标签1")
        lb1.setStyleSheet("background-color: cyan;")
        lb2 = QLabel("标签2")
        lb2.setStyleSheet("background-color: yellow;")
        lb3 = QLabel("标签3")
        lb3.setStyleSheet("background-color: red;")
        lb4 = QLabel("标签4")
        lb4.setStyleSheet("background-color: orange;")

        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)

        layout.addWidget(lb1, 2)
        # layout.addSpacing(50)  # 因为控件本身有空白边框，实际间距大于50，此宽度为固定值
        layout.addWidget(lb2, 2)
        layout.addStretch(1)  # 添加空白的伸缩因子
        layout.addWidget(lb3, 2)
        layout.addWidget(lb4)  # 默认伸缩因子为 0

        # layout.insertSpacing(3, 50)  # 插入空白

        layout.setStretchFactor(lb1, 1)  # 给lb1设置伸缩因子为 1


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

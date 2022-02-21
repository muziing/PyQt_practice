import sys

from PyQt5.Qt import *

# 除名称、方向外，和父类QBoxLayout完全一致
# 甚至可以通过 setDirection() 方法把水平布局和垂直布局互换


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):

        v_layout = QVBoxLayout()
        self.setLayout(v_layout)
        v_layout.setDirection(QBoxLayout.BottomToTop)
        # v_layout.setDirection(QBoxLayout.RightToLeft)  # 甚至可以改变为水平布局

        lb1 = QLabel("lb1")
        lb1.setStyleSheet("background-color: cyan;")
        lb2 = QLabel("lb2")
        lb2.setStyleSheet("background-color: orange;")

        v_layout.addWidget(lb1)
        v_layout.addWidget(lb2)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

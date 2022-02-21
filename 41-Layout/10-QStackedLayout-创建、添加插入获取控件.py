import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # 1. 创建一个布局管理器对象
        sl = QStackedLayout()
        # 2. 把布局对象设置给需要布局的父控件 父布局
        self.setLayout(sl)
        # 3. 通过布局管理器对象，管理布局一些子控件
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color: red;")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color: yellow;")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color: cyan;")

        label4 = QLabel("标签4")
        label4.setStyleSheet("background-color: pink;")
        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color: blue;")
        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color: cyan;")

        v_layout = QVBoxLayout()
        v_layout.addWidget(label4)
        v_layout.addWidget(label5)
        v_layout.addWidget(label6)

        print("标签1的当前索引值", sl.addWidget(label1))
        print("标签2的当前索引值", sl.addWidget(label2))
        print(f"正在显示{sl.currentIndex()}")  # 当前显示的内容的索引
        print(
            "标签3的当前索引值", sl.insertWidget(0, label3)
        )  # 在1的位置插入标签3，但此时仍然显示标签1（标签1的索引已经变成1）
        print(f"正在显示{sl.currentIndex()}")  # 当前显示的内容的索引
        print(f"此时{sl.widget(2).text()}的索引值为2")
        # sl.addChildLayout(v_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

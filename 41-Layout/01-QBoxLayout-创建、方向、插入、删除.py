import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BoxLayout")
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

        # 1.创建布局管理器对象
        layout = QBoxLayout(QBoxLayout.LeftToRight)

        # 2.把布局管理器对象设置给需要布局的父控件
        self.setLayout(layout)

        # 3.添加需要布局的子控件到布局管理器中
        layout.addWidget(lb1)
        layout.addWidget(lb2)
        layout.addWidget(lb3)
        # layout.addWidget(lb4)

        # layout.insertWidget(1, lb4)  # 插入 Widget

        v_layout = QBoxLayout(QBoxLayout.TopToBottom)
        lb5 = QLabel("标签5")
        lb5.setStyleSheet("background-color: pink;")
        lb6 = QLabel("标签6")
        lb6.setStyleSheet("background-color: blue;")
        lb7 = QLabel("标签7")
        lb7.setStyleSheet("background-color: orange;")
        v_layout.addWidget(lb5)
        v_layout.addWidget(lb6)
        v_layout.addWidget(lb7)

        layout.insertLayout(1, v_layout)  # 插入另一个 Layout

        # timer = QTimer(self)
        #
        # def test():
        #     layout.setDirection((layout.direction() + 1) % 4)  # 修改方向
        #
        # timer.timeout.connect(test)
        # timer.start(1000)

        # layout.removeWidget(lb1)  # 只是将其从布局管理器中移除，不改变其和其他控件的父子关系（包含通过布局管理器间接建立的）
        lb1.hide()  # 继承自 QWidget 的方法，隐藏，再调用show()方法时会再次显示
        lb1.show()
        lb1.setParent(None)  # 彻底删除释放对象


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

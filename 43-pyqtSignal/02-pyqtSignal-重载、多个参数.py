import sys

from PyQt5.Qt import *


class Btn(QPushButton):
    """自定义按钮类，重写事件以实现自定义信号"""

    # 自定义信号
    rightClicked = pyqtSignal([str], [int])  # 每次只发送一个str或int类型的数据，应用于重载等情况
    leftClicked = pyqtSignal([str], [int, str])  # 可以传出多个参数

    def mousePressEvent(self, e) -> None:
        super().mousePressEvent(e)
        if e.button() == Qt.RightButton:  # 当按下的键是鼠标右键时
            # self.rightClicked.emit(self.text())  # 发送信号，传递参数
            self.rightClicked[str].emit(self.text())  # 发送信号，指明了传递的参数为str类型
            self.rightClicked[int].emit(888)  # 发送信号，指明了传递的参数为int类型

        if e.button() == Qt.LeftButton:
            self.leftClicked[int, str].emit(888, "muzing")  # 指明传递参数的数量和对应类型


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = Btn("测试按钮", self)
        btn.move(100, 100)

        # 没有指明需要的参数类型，默认取第一种
        btn.rightClicked.connect(lambda content: print("按钮被鼠标右键点击击了", content))

        # 指明需要的参数类型，找int那一项
        # btn.rightClicked[int].connect(lambda content: print('按钮被鼠标右键点击击了', content))

        # 传递多个参数
        btn.leftClicked[int, str].connect(lambda c1, c2: print("鼠标左键被点击了", c1, c2))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressBar")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        pb = QProgressBar(self)
        pb.move(100, 100)

        pb.setMinimum(50)
        pb.setValue(75)
        print(pb.minimum())  # 默认最小值为0
        print(pb.maximum())  # 默认最大值为100
        # print(pb.value())  # 获取当前值
        # pb.reset()  # 重置，值会变成 最小值-1
        # pb.setRange(0, 0)  # 若最大最小值相同，则进入繁忙提示

        btn = QPushButton("测试按钮", self)
        btn.move(300, 100)

        def test():
            pb.reset()
            print(pb.minimum())
            print(pb.maximum())
            print(pb.value())

        btn.clicked.connect(test)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

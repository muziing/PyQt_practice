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
        pb.setValue(88)
        pb.setValue(60)

        # pb.setTextVisible(False)  # 隐藏文本标签
        print(pb.text())  # 可以获取文本标签内容

        # -----------方向-------------
        # pb.setOrientation(Qt.Horizontal)  # 水平
        pb.setOrientation(Qt.Vertical)  # 垂直，默认隐藏文本标签
        pb.setTextDirection(QProgressBar.BottomToTop)  # windows系统无法显示垂直时的文本标签，很迷
        pb.setTextDirection(QProgressBar.TopToBottom)

        # --------反转-------------
        pb.setInvertedAppearance(True)  # 进行反转


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

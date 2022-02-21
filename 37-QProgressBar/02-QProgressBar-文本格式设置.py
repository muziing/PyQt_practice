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
        pb.resize(300, 30)

        pb.setFormat("当前人数 %v / 总人数 %m ")
        """
        %p 百分比
        %v 当前值
        %m 总值
        可以通过字符串格式化方法来灵活使用
        """

        # pb.resetFormat()  # 重置，变回默认值（仅显示百分之）

        pb.setAlignment(Qt.AlignHCenter)  # 显示在进度条内，水平居中


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

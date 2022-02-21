import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox-数据限制")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        cbb = QComboBox(self)
        cbb.move(100, 100)
        cbb.resize(100, 20)
        cbb.setEditable(True)

        cbb.addItems([str(i) for i in range(5)])
        cbb.setMaxCount(7)  # 限制最多存储7条，达到7后无法添加新的
        cbb.setMaxVisibleItems(5)  # 限制每页最多只显示5条


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

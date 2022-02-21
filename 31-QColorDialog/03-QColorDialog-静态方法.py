import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QColorDialog-静态方法")
        self.resize(500, 500)
        self.move(400, 250)
        # self.setup_ui()
        self.setup_color()

    def setup_ui(self):
        cd = QColorDialog(QColor(20, 154, 151), self)  # 可以传入创建时的默认颜色
        cd.setWindowTitle("选择颜色")

        btn = QPushButton("测试按钮", self)
        btn.move(100, 100)
        # btn.clicked.connect(lambda: print(cd.customCount()))
        btn.clicked.connect(
            lambda: print(QColorDialog.customCount())
        )  # 是静态方法，也可以这样直接使用

        QColorDialog.setCustomColor(4, QColor(20, 154, 151))  # 修改指定索引位置的自定义颜色
        QColorDialog.setStandardColor(0, QColor(255, 0, 0))  # 修改指定索引位置的标准颜色

        cd.show()

    def setup_color(self):
        btn = QPushButton("测试按钮", self)
        btn.move(100, 100)

        def color_1(col):
            palette = QPalette()
            palette.setColor(QPalette.Background, col)
            self.setPalette(palette)

        def test():
            color = QColorDialog.getColor(QColor(20, 154, 151), self, "选择颜色")
            # 阻塞式弹出
            color_1(color)
            print(color)

        btn.clicked.connect(test)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

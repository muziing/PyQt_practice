from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget")
        self.resize(500, 500)
        self.page_1 = QWidget(self)
        self.page_2 = QPlainTextEdit(self)
        self.setup_page_1()
        self.setup_page_2()
        self.setup_tab_widget()

    def setup_page_1(self):
        lb_1 = QLabel("这是第一个标签页", self.page_1)

    def setup_page_2(self):
        self.page_2.setPlainText("这是第二个标签页")

    def setup_tab_widget(self):
        tw = QTabWidget(self)
        tw.move(50, 50)
        tw.resize(400, 400)
        tw.addTab(self.page_1, "Tab1")  # 把页添加到QTabWidget中
        tw.addTab(self.page_2, "Tab2")

        # -------- 标签位置 -----------
        tw.setTabPosition(QTabWidget.North)  # 标签在上方（默认值）
        # tw.setTabPosition(QTabWidget.South)  # 标签在下方
        # tw.setTabPosition(QTabWidget.West)  # 标签在左侧
        # tw.setTabPosition(QTabWidget.East)  # 标签在右侧

        # ------ 标签形状 ---------
        tw.setTabShape(QTabWidget.Rounded)  # 圆角
        # tw.setTabShape(QTabWidget.Triangular)  # 三角形（梯形）


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

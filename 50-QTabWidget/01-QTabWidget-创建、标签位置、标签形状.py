from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget")
        self.resize(500, 500)
        self.page_1 = QWidget()  # 创建页面时不需要指定父控件
        self.page_2 = QPlainTextEdit()
        self.setup_page_1()
        self.setup_page_2()
        self.setup_tab_widget()

    def setup_page_1(self):
        lb_1 = QLabel("这是第一个标签页", self.page_1)
        lb_1.move(100, 100)

    def setup_page_2(self):
        self.page_2.setPlainText("这是第二个标签页")

    def setup_tab_widget(self):
        tw = QTabWidget(self)
        tw.move(50, 50)
        tw.resize(400, 400)
        tw.addTab(self.page_1, "Tab1")  # 把页添加到QTabWidget中
        tw.addTab(self.page_2, "Tab2")

        # ------父控件关系------
        print(self.page_1.parentWidget())  # 父控件是一个 QStackedWidget
        print(self.page_2.parentWidget())
        print(tw)
        print(self.page_2.parentWidget().parentWidget())  # 父控件的父控件才是tw这个 QTabWidget

        # -------- 标签位置 -----------
        tw.setTabPosition(QTabWidget.North)  # 标签在上方（默认值）
        # tw.setTabPosition(QTabWidget.South)  # 标签在下方
        # tw.setTabPosition(QTabWidget.West)  # 标签在左侧
        # tw.setTabPosition(QTabWidget.East)  # 标签在右侧

        # ------ 标签形状 ---------
        tw.setTabShape(QTabWidget.Rounded)  # 圆角（默认值）
        # tw.setTabShape(QTabWidget.Triangular)  # 三角形（梯形）


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

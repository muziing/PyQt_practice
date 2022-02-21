import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget")
        self.resize(500, 500)
        self.page_1 = QWidget()  # 创建页面时不需要指定父控件
        self.page_2 = QPlainTextEdit()
        self.tab_widget = QTabWidget(self)  # 在主窗口上创建一个QTabWidget控件
        self.setup_page_1()
        self.setup_page_2()
        self.setup_tab_widget()

    def setup_page_1(self):
        """布局第一个页面的方法"""
        # 在每个页面中，只需像在其他QWidget内一样设置按钮标签等各种子控件即可
        lb_1 = QLabel("这是第一个标签页", self.page_1)
        lb_1.move(100, 100)

    def setup_page_2(self):
        """布局第二个页面的方法"""
        # 页面也可以是QWidget的各种子类，比如这里是一个QPlainWidget
        self.page_2.setPlainText("这是第二个标签页")

    def setup_tab_widget(self):
        """布局tab widget的方法"""
        tw = self.tab_widget
        tw.move(50, 50)
        tw.resize(400, 400)
        tw.addTab(self.page_1, "Tab1")  # 把页添加到QTabWidget中
        tw.insertTab(1, self.page_2, "Tab2")  # 也可以通过指定索引在指定位置插入标签页

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

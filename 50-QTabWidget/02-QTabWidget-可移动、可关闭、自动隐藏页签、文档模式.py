import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget")
        self.resize(500, 500)
        self.page_1 = QWidget()  # 创建页面时不需要指定父控件
        self.page_2 = QPlainTextEdit()
        self.tab_widget = QTabWidget(self)  # 创建一个QTabWidget
        self.setup_page_1()
        self.setup_page_2()
        self.setup_tab_widget()

    def setup_page_1(self):
        lb_1 = QLabel("这是第一个标签页", self.page_1)
        lb_1.move(100, 100)

    def setup_page_2(self):
        self.page_2.setPlainText("这是第二个标签页")

    def setup_tab_widget(self):
        """布局tab widget的方法"""
        tw = self.tab_widget
        tw.move(50, 50)
        tw.resize(400, 400)
        tw.addTab(self.page_1, "Tab1")  # 把页添加到QTabWidget中
        tw.addTab(self.page_2, "Tab2")

        # --------可移动-------
        # 类似浏览器中可以鼠标拖动交换页签顺序的效果，默认为False
        tw.setMovable(True)

        # --------可关闭--------
        tw.setTabsClosable(True)  # 这一步只是在外观上为每个标签添加了关闭按钮

        def close_tab(index):
            """真正关闭标签页的槽函数"""
            tw.tabBar().removeTab(index)

        tw.tabCloseRequested.connect(close_tab)  # 连接关闭的信号与槽

        # -----自动隐藏页签-------
        # 默认为False，即使只剩一个标签页，页还会保留页签
        tw.setTabBarAutoHide(True)  # 当只剩一个标签页的时候就已经隐藏了页签

        # -----文档模式---------
        # 此属性设置为True时，不会呈现选项卡部件框架，即选项卡页面和其后的窗口等页面无框架区分看起来是一个整体。
        # 此模式对于页面需要显示文档类型的情况非常有用，因为节省了选项卡部件框架占用的部分空间。
        tw.setDocumentMode(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

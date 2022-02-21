import sys

from PyQt5.Qt import *

"""
本节涉及到的几个方法都和窗口尺寸是否能完整容纳所有内容有关
在运行代码实验效果时注意拖动缩放窗口，观察不同设置下省略模式的不同表现
"""


class Window(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget")
        self.resize(400, 400)
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
        self.addTab(self.page_1, "Tab1")  # 把页添加到QTabWidget中
        self.addTab(self.page_2, "This is a very very very long label")
        self.setTabsClosable(True)

        # --------设置图标、图标尺寸-------------
        # 添加标签页时也可以设置图标
        self.insertTab(
            2, QWidget(), QIcon("../Icons/python_96px.ico"), "Another long label"
        )
        # 也可以在添加标签页后设置图标
        self.setTabIcon(0, QIcon("../Icons/OS_Ubuntu_128px.ico"))
        self.setIconSize(QSize(40, 40))
        # 设置的是图标尺寸的最大值，更的的图标文件会被缩小到此大小，但更小的图标文件不会被放大

        # -------省略号模式----------------
        # 当空间狭小，不足以显示页签内全部文本时，会按照设置的ElideMode使用省略号隐藏过长的文本
        # 可以通过缩放窗口体验
        self.setElideMode(Qt.ElideLeft)  # 省略号出现在左侧

        # -------按钮滚动标签页--------
        # 控制当选项卡栏有多个选项卡无足够空间显示时是否使用按钮滚动选项卡
        # 默认为True，当空间不足以显示全部页签时，添加一个滚动按钮以滚动显示被隐藏的页签
        self.setUsesScrollButtons(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

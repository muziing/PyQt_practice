import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget-信号")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        tw = QTabWidget(self)
        tw.resize(300, 300)
        tw.move(50, 50)
        tw.addTab(QWidget(), "tab1")
        tw.addTab(QWidget(), "tab2")
        tw.addTab(QWidget(), "tab3")
        tw.addTab(QWidget(), "tab4")

        # ---------信号----------
        tw.currentChanged.connect(lambda index: print(f"当前页面变成了{index}！"))
        tw.tabBarClicked.connect(lambda index: print(f"索引为{index}的页签被点击了！"))
        tw.tabBarDoubleClicked.connect(lambda index: print(f"索引为{index}的页签被双击了！"))

        tw.setTabsClosable(True)  # 这一步只是在外观上为每个标签添加了关闭按钮

        def close_tab(index):
            """真正关闭标签页的槽函数"""
            tw.tabBar().removeTab(index)

        tw.tabCloseRequested.connect(close_tab)  # 连接关闭的信号与槽


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget")
        self.resize(500, 500)
        self.page_1 = QWidget()  # 创建页面时不需要指定父控件
        self.tab_widget = QTabWidget(self)  # 在主窗口上创建一个QTabWidget控件
        self.setup_ui()
        self.setup_page_1()
        self.setup_tab_widget()

    def setup_ui(self):
        self.btn = QPushButton("测试按钮", self)
        self.btn.move(350, 20)

    def setup_page_1(self):
        """布局第一个页面的方法"""
        lb_1 = QLabel("这是第一个标签页", self.page_1)
        lb_1.move(100, 100)

    def setup_tab_widget(self):
        """布局tab widget的方法"""
        tw = self.tab_widget
        tw.move(50, 50)
        tw.resize(400, 400)
        tw.addTab(self.page_1, "Tab1")  # 把页添加到QTabWidget中
        tw.addTab(QWidget(), "Tab2")
        tw.addTab(QWidget(), "Tab3")
        tw.addTab(QWidget(), "Tab4")

        # -------移除页----------
        # self.btn.clicked.connect(lambda: tw.removeTab(2))  # 移除索引位置为2的页

        # -------页不可用-------
        # 设置页不可用后，仍然能看到页签，但是变成灰色、不可选中
        # self.btn.clicked.connect(lambda: tw.setTabEnabled(0, False))  # 设置页不可用

        # ------清空页-------
        # 相当于调用 tw.removeTab() 直到全部移除
        def test_slot():
            print("page_1: ", self.page_1)
            print("page_1.parentWidget: ", self.page_1.parentWidget())

            tw.clear()  # 清空TabWidget

            print("page_1: ", self.page_1)  # clear 后仍可打印页，说明页并没有被删除
            print("page_1.parentWidget: ", self.page_1.parentWidget())  # 父子关系页没有改变

        self.btn.clicked.connect(test_slot)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

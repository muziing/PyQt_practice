import sys

from PyQt5.QtWidgets import *

"""
堆栈窗口控件
原帖: https://blog.csdn.net/qq_40243295/article/details/105633221
"""


class QStackWidgetDemo(QWidget):
    """堆栈窗口控件（QStackWidget）"""

    def __init__(self):
        super(QStackWidgetDemo, self).__init__()
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle("堆栈窗口控件：QStackWidget")

        self.list = QListWidget()
        self.list.insertItem(0, "联系方式")
        self.list.insertItem(1, "个人信息")
        self.list.insertItem(2, "教育程度")

        # 三个页面
        self.stack1 = QWidget()  # 对于一个页面的窗口
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.tab1UI()  # 通过这三个方法，给每一页添加控件
        self.tab2UI()
        self.tab3UI()
        self.stack = QStackedWidget()
        self.stack.addWidget(self.stack1)  # 添加至堆栈中
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        hbox = QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addWidget(self.stack)
        self.setLayout(hbox)
        self.list.currentRowChanged.connect(self.display)

    # 通过这个函数来切换索引
    def display(self, index):
        self.stack.setCurrentIndex(index)

    def tab1UI(self):
        # 表单布局
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.stack1.setLayout(layout)

    def tab2UI(self):
        # 水平布局
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))
        layout.addRow(QLabel("性别"), sex)
        layout.addRow("生日", QLineEdit())
        self.stack2.setLayout(layout)

    def tab3UI(self):
        # 水平布局
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.stack3.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QStackWidgetDemo()
    main.show()
    sys.exit(app.exec_())

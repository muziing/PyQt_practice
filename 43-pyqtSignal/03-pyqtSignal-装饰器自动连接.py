import sys

from PyQt5.Qt import *

"""
1.
QtCore.QMetaObject.connectSlotsByName(obj)
将obj内部的子孙对象的信号，按照其objectNames连接到相关的槽函数

2.借助装饰器装饰固定规则的槽函数即可
代码: 
@pyqtSlot()
def on_objectName_信号():
    pass

等同于
obj.objectName.信号.connect(obj.objectName_信号)
def objectName_信号():
    pass
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqtSignal装饰器连接")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton("测试按钮", self)
        self.btn = btn
        btn.setObjectName("btn")
        btn.resize(200, 200)
        btn.move(100, 100)
        QMetaObject.connectSlotsByName(self)  # 非动态识别，必须先创建子孙对象，再调用这个方法才有效

    @pyqtSlot(bool)
    def on_btn_clicked(self, val):
        print("按钮被点击了", val)

    # ----------相当于下面的写法--------------
    def do_something(self):
        self.btn.clicked[bool].connect(self.btn_clicked)

    def btn_clicked(self, val: bool):
        print("按钮被点击了", val)

    # ------------------------------------


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

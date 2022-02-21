import sys

from PyQt5.Qt import *

"""
关于PyQt信号(Signal)与槽(Slot)机制，后面还有一个43-pyqtSignal目录讲解
可以在学习各种控件的过程中逐渐体会信号与槽的连接、传参等等
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号的操作")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # self.QObject信号的操作_destroy()
        self.QObject信号的操作_namechanged()

    def QObject信号的操作_destroy(self):
        self.obj = QObject()

        def destroy_slot(obj):
            print("对象被释放了", obj)

        self.obj.destroyed.connect(destroy_slot)

    def QObject信号的操作_namechanged(self):
        self.obj = QObject()

        def obj_name_slot(name):
            print("对象名称发生了改变", name)

        self.obj.objectNameChanged.connect(obj_name_slot)  # 建立信号与槽的连接
        self.obj.setObjectName("AAA")
        print(
            "此时有", self.obj.receivers(self.obj.objectNameChanged), "个槽与该信号连接"
        )  # 该信号连接的槽的数量

        def receivers_test_slot():
            pass

        self.obj.objectNameChanged.connect(receivers_test_slot)
        print(
            "此时有", self.obj.receivers(self.obj.objectNameChanged), "个槽与该信号连接"
        )  # 该信号连接的槽的数量

        # self.obj.objectNameChanged.disconnect()  # 取消信号与槽的连接

        print("连接是否被阻断： ", self.obj.signalsBlocked())  # 检查信号与槽的连接是否被阻断
        self.obj.blockSignals(True)  # 暂时阻断信号与槽的连接
        print("连接是否被阻断： ", self.obj.signalsBlocked())

        self.obj.setObjectName("BBB")

        self.obj.blockSignals(False)  # 恢复信号与槽的连接
        print("连接是否被阻断： ", self.obj.signalsBlocked())

        self.obj.setObjectName("CCC")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

import sys

from PyQt5.Qt import *

"""继承自QWidget.
在setContextMenuPolicy()中，
默认(Qt.DefaultContextMenu)为调用对象方法 contextMenuEvent ；
如果设置 Qt.CustomContextMenu，则发送 customContextMenuRequested 信号"""


class Window(QWidget):
    def contextMenuEvent(self, a0: QContextMenuEvent) -> None:
        # print("展示菜单")
        menu = QMenu(self)
        new_action = QAction(QIcon("../Icons/plus_48px.ico"), "新建", menu)
        new_action.triggered.connect(lambda: print("新建文件"))
        menu.addAction(new_action)
        menu.exec_(a0.globalPos())  # 把位置（全局）传递


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = Window()
# 2.2设置控件

window.setWindowTitle("右键菜单")
window.resize(500, 500)
window.move(400, 250)


def show_menu(point):
    """customContextMenuRequested 的槽函数"""
    # print("自定义上下文菜单", point)
    menu = QMenu(window)
    exit_action = QAction(QIcon("../Icons/cross_48px.ico"), "关闭", menu)
    exit_action.triggered.connect(lambda: exit())
    menu.addAction(exit_action)

    # 把相对控件的坐标 point 映射到全局位置
    dest_point = window.mapToGlobal(point)
    menu.exec_(dest_point)  # 把位置（全局）传递


window.setContextMenuPolicy(Qt.CustomContextMenu)
window.customContextMenuRequested.connect(show_menu)

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

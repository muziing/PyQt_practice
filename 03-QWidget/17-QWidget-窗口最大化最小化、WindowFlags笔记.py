import sys

from PyQt5 import QtGui
from PyQt5.Qt import *


class Window(QWidget):
    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        """点击用户区域，窗口在最大化最小化之间切换"""
        if self.isMaximized():  # 判断是否是最大化窗口
            self.showNormal()
        else:
            self.showMaximized()


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = Window()
# 2.2设置控件

window.setWindowTitle("窗口最大化最小化")
window.resize(500, 500)
window.move(400, 250)

window.setWindowFlags(Qt.WindowStaysOnTopHint)  # 设置顶层窗口的 Flag，以下为具体参数
# window.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)  # 窗口无法调整大小
# window.setWindowFlags(Qt.FramelessWindowHint)  # 窗口无边框
# window.setWindowFlags(Qt.CustomizeWindowHint)  # 有边框但无标题栏和按钮，不能移动和拖动
# window.setWindowFlags(Qt.WindowTitleHint)    # 添加标题栏和一个关闭按钮
# window.setWindowFlags(Qt.WindowSystemMenuHint)  # 添加系统目录和一个关闭按钮
# window.setWindowFlags(Qt.WindowMinMaxButtonsHint)  # 激活最小化、最大化和关闭按钮
# window.setWindowFlags(Qt.WindowMinimizeButtonHint)  # 激活最小化和关闭按钮，禁用最大化按钮
# window.setWindowFlags(Qt.WindowMaximizeButtonHint)  # 激活最大化和关闭按钮，禁用最小化按钮
# window.setWindowFlags(Qt.WindowCloseButtonHint)    # 添加一个关闭按钮
# window.setWindowFlags(Qt.WindowContextHelpButtonHint)  # 添加问号和关闭按钮，同对话框
# window.setWindowFlags(Qt.WindowStaysOnTopHint)    # 窗口始终置于顶层
# window.setWindowFlags(Qt.WindowStaysOnBottomHint)  # 窗口始终置于底层

# 2.3展示控件
window.show()
# window.showMaximized()  # 最大化
# window.showFullScreen()  # 全屏显示
# window.showMinimized()  # 最小化

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

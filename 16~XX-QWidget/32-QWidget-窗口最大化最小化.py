from PyQt5.Qt import *
from PyQt5 import QtGui
import sys


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

# 2.3展示控件
window.show()
# window.showMaximized()  # 最大化
# window.showFullScreen()  # 全屏显示
# window.showMinimized()  # 最小化

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

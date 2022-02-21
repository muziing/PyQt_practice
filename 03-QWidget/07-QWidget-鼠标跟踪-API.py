import sys

from PyQt5.Qt import *


class MyWindow(QWidget):
    # QMouseEvent
    def mouseMoveEvent(self, me):
        # print("鼠标移动了", me.globalPos())  # 坐标值为相对整个电脑屏幕
        print("鼠标移动了", me.localPos())  # 坐标值为相对本QWidget窗口


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = MyWindow()
# 2.2设置控件

window.setWindowTitle("鼠标跟踪")
window.resize(500, 500)
window.move(400, 250)
window.setMouseTracking(True)  # 启动鼠标追踪，即使不按下鼠标左键，也时刻追踪鼠标位置
print(window.hasMouseTracking())

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

import sys

from PyQt5.Qt import *


class MyObject(QObject):
    def timerEvent(self, evt):
        print(evt, "1")


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QObject定时器的使用")
window.resize(500, 500)
window.move(400, 250)

obj = MyObject()
timer_id = obj.startTimer(1000)

# obj.killTimer(timer_id)


# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

import sys

from PyQt5.Qt import *


class MyLabel(QLabel):
    def enterEvent(self, *args, **kwargs):
        print("鼠标进入")
        self.setText("欢迎光临")

    def leaveEvent(self, *args, **kwargs) -> None:
        print("鼠标离开")
        self.setText("谢谢惠顾")


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("鼠标操作的案例1")
window.resize(500, 500)
window.move(400, 250)

label = MyLabel(window)
label.resize(200, 200)
label.move(100, 100)
label.setStyleSheet("background-color: cyan;")

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

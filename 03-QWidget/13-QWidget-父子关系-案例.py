import sys

from PyQt5.Qt import *

"""点击哪个label，哪个label的背景颜色就变红。重写QLabel和QWidget（父控件）两种方法"""


# class MyLabel(QLabel):
#     def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
#         self.setStyleSheet("background-color: red;")


class Window(QWidget):
    def mousePressEvent(self, evt) -> None:
        local_x = evt.x()
        local_y = evt.y()
        sub_widget = self.childAt(local_x, local_y)
        if sub_widget is not None:
            sub_widget.setStyleSheet("background-color: red;")
        # print("被点击了", local_x, local_y)


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = Window()
# 2.2设置控件

window.setWindowTitle("父子关系案例")
window.resize(500, 500)
window.move(400, 250)

for i in range(1, 11):
    label = QLabel(window)
    label.setText(f"标签{i}")
    label.move(40 * i, 40 * i)

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

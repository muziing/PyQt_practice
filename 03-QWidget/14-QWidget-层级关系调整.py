import sys

from PyQt5 import QtGui
from PyQt5.Qt import *


class MyLabel(QLabel):
    """重写QLabel的mousePressEvent方法以实现点击谁就把谁放到顶层"""

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.raise_()


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QWidget层级关系调整")
window.resize(500, 500)
window.move(400, 250)

label1 = MyLabel(window)
label1.setText("标签1")
label1.resize(200, 200)
label1.setStyleSheet("background-color: red;")

label2 = MyLabel(window)
label2.setText("标签2")
label2.resize(200, 200)
label2.move(100, 100)
label2.setStyleSheet("background-color: green;")

"""默认后添加的控件覆盖前面的控件，为使label1能覆盖2，有以下三种方法"""
# label2.lower()
# label1.raise_()
# label2.stackUnder(label1)

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

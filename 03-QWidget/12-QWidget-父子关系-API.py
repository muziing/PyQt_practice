import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("父子关系的学习")
window.resize(500, 500)
window.move(400, 250)

label1 = QLabel(window)
label1.setText("标签1")
label1.move(0, 20)

label2 = QLabel(window)
label2.setText("标签2")
label2.move(50, 20)

label3 = QLabel(window)
label3.setText("标签3")
label3.move(100, 20)

# print(window.childAt(55, 0))  # 根据指定的父控件、坐标点，找到对应的子控件
# print(label2.parent())

print(window.childrenRect())  # 子控件组成的矩形区域

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

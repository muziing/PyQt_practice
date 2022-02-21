import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QPushButton-默认处理")
window.resize(500, 500)
window.move(400, 250)

btn1 = QPushButton("btn1", window)
btn1.pressed.connect(lambda: print("btn1被点击了"))
btn2 = QPushButton("btn2", window)
btn2.move(100, 0)
btn2.pressed.connect(lambda: print("btn2被点击了"))

# btn2.setAutoDefault(True)  # 用户点击了 btn2 后，btn2设置为默认
btn2.setDefault(True)  # 设置 btn2 为默认
print(btn1.autoDefault())
print(btn2.autoDefault())

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

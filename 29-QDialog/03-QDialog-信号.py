import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QDialog")
window.resize(500, 500)
window.move(400, 250)

d = QDialog(window)
d.setWindowTitle("对话框")

btn1 = QPushButton("btn1", d)
btn1.move(100, 20)
btn1.clicked.connect(lambda: d.accept())
btn2 = QPushButton("btn2", d)
btn2.move(200, 20)
btn2.clicked.connect(lambda: d.reject())
btn3 = QPushButton("btn3", d)
btn3.move(300, 20)
btn3.clicked.connect(lambda: d.done(8))


d.accepted.connect(lambda: print("点击了接受按钮"))
d.rejected.connect(lambda: print("点击了拒绝按钮"))
d.finished.connect(lambda val: print("完成", val))

d.show()

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

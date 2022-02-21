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
d.setSizeGripEnabled(True)  # 在右下角显示尺寸调整

btn1 = QPushButton("btn1", d)
btn1.move(100, 20)
btn1.clicked.connect(lambda: d.accept())  # accept为1

btn2 = QPushButton("btn2", d)
btn2.move(200, 20)
btn2.clicked.connect(lambda: d.reject())  # reject为0

btn3 = QPushButton("btn3", d)
btn3.move(300, 20)
btn3.clicked.connect(lambda: d.done(8))  # 关闭对话框，返回指定值8

btn4 = QPushButton("btn4", d)
btn4.move(400, 20)
btn4.clicked.connect(lambda: d.setResult(888))  # 不关闭对话框，可以通过d.result()获取

btn5 = QPushButton("btn5", d)
btn5.move(500, 20)
d.setResult(888)
btn5.clicked.connect(lambda: print(d.result()))

result = d.exec()
print(result)

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

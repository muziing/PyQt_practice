import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QLineEdit-创建")
window.resize(500, 500)
window.move(400, 250)

le = QLineEdit(window)
le.setText("muzing")  # 设置文本
# le.insert("ing")  # 在光标处插入文本

btn1 = QPushButton("插入内容", window)
btn1.move(200, 0)
btn1.pressed.connect(lambda: le.insert("123"))

lb = QLabel(window)
lb.move(20, 80)


def get_text():
    # lb.setText(le.text())
    lb.setText(le.displayText())
    lb.adjustSize()


btn2 = QPushButton("获取", window)
btn2.move(200, 80)
btn2.pressed.connect(get_text)
# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

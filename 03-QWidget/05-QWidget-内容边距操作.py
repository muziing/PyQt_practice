import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("内容边距的设定")
window.resize(500, 500)

label = QLabel(window)
label.setText("ABC")
label.resize(300, 300)
label.setStyleSheet("background-color: cyan; font-size: 30px;")

label.setContentsMargins(100, 200, 0, 0)

print(label.contentsRect())

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

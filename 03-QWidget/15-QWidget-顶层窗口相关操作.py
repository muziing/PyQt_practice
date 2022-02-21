import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.resize(500, 500)
window.move(400, 250)
icon = QIcon("../Icons/Photoshop.ico")
window.setWindowIcon(icon)  # 设置图标
# print(window.windowIcon())

window.setWindowTitle("这是窗口的标题")  # 设置标题
# print(window.windowTitle())

window.setWindowOpacity(0.78)  # 设置窗口不透明度
# print(window.windowOpacity())

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

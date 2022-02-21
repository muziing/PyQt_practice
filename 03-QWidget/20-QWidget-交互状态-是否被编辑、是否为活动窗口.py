import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("[*]交互状态")  # *星号只有设置setWindowModified(True)才会被显示
window.resize(500, 500)
window.move(400, 250)

window.setWindowModified(True)
print("窗口是否被编辑：", window.isWindowModified())

w2 = QWidget()  # 为验证活动窗口相关API而创建的另一个窗口
w2.show()
# 2.3展示控件
window.show()
w2.raise_()  # 即使被提到前面，也不一定是活动窗口

print("w2是否为活动窗口：", w2.isActiveWindow())
print("window是否为活动窗口：", window.isActiveWindow())
# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QFrame-功能作用")
window.resize(500, 500)
# window.move(400, 250)

frame = QFrame(window)
frame.resize(200, 200)

# frame.setFrameShape(QFrame.Box)
# frame.setFrameShape(QFrame.Panel)
# frame.setFrameShadow(QFrame.Raised)

frame.setFrameStyle(QFrame.Box | QFrame.Raised)

frame.setLineWidth(5)  # 外线宽度
frame.setMidLineWidth(6)  # 中线宽度

print(frame.frameWidth())

# frame.setFrameRect(QRect(50, 50, 50, 50))  # 框架矩形

frame.move(100, 100)


# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

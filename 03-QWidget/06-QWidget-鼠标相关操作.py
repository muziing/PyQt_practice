import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("鼠标操作")
window.resize(500, 500)
window.move(400, 250)

# window.setCursor(Qt.ForbiddenCursor)
# window.setCursor(Qt.OpenHandCursor)

label = QLabel(window)
label.setText("muzing")
label.resize(300, 300)
label.setStyleSheet("background-color: cyan;")

# label.setCursor(Qt.ForbiddenCursor)  # 进入控件范围内，鼠标变化

pixmap = QPixmap("../Icons/python_96px.ico")  # 图片路径
pixmap = pixmap.scaled(100, 100)  # 重新设置大小
cursor = QCursor(pixmap, 0, 0)  # 0, 0 为热点位置
label.setCursor(cursor)
# label.unsetCursor()  # 恢复鼠标

current_cursor = label.cursor()
# print(current_cursor.pos())  # 获取光标位置（相对于整个电脑屏幕）
current_cursor.setPos(100, 100)  # 设置光标位置

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

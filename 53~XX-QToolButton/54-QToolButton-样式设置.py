from PyQt5.Qt import *
import sys

"""
setToolButtonStyle(Qt.ToolButtonIconOnly)
风格取值：（可用 int 数字简写）
Qt.ToolButtonOnly 仅显示图标  int -> 0
Qt.ToolButtonTextOnly 仅显示文字  int -> 1
Qt.ToolButtonTextBesideIcon  文本显示在图标旁边  int -> 2
Qt.ToolButtonTextUnderIcon  文本显示在图标下方  int -> 3
Qt.ToolButtonFollowStyle  遵循风格  int -> 4
"""
# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QToolButton样式设置")
window.resize(500, 500)
window.move(400, 250)

tb = QToolButton(window)
tb.setText("ToolButton")
tb.setIcon(QIcon('../Icons/search_48px.ico'))
tb.setIconSize(QSize(50, 50))
# tb.setToolButtonStyle(Qt.ToolButtonIconOnly)  # 仅显示图标
# tb.setToolButtonStyle(Qt.ToolButtonTextOnly)  # 仅显示文字
# tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  # 文本显示在图标旁边
# tb.setToolButtonStyle(2)  # 文本显示在图标旁边
# tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 文本显示在图标下方
tb.setToolButtonStyle(Qt.ToolButtonFollowStyle)  # 遵循风格

print(tb.toolButtonStyle())

# 2.3展示控件
window.show()
# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

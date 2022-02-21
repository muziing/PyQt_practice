import sys

from PyQt5.Qt import *

"""
setToolButtonStyle(Qt.ToolButtonIconOnly)
风格取值：（可用 int 数字简写）
Qt.ToolButtonOnly 仅显示图标  int -> 0
Qt.ToolButtonTextOnly 仅显示文字  int -> 1
Qt.ToolButtonTextBesideIcon  文本显示在图标旁边  int -> 2
Qt.ToolButtonTextUnderIcon  文本显示在图标下方  int -> 3
Qt.ToolButtonFollowStyle  遵循风格  int -> 4
"""
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QToolButton样式设置")
window.resize(500, 500)
window.move(400, 250)

tb = QToolButton(window)
tb.setText("ToolButton")
tb.setIcon(QIcon("../Icons/search_48px.ico"))
tb.setIconSize(QSize(50, 50))
# tb.setToolButtonStyle(Qt.ToolButtonIconOnly)  # 仅显示图标
# tb.setToolButtonStyle(Qt.ToolButtonTextOnly)  # 仅显示文字
# tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  # 文本显示在图标旁边
# tb.setToolButtonStyle(2)  # 文本显示在图标旁边
# tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 文本显示在图标下方
tb.setToolButtonStyle(Qt.ToolButtonFollowStyle)  # 遵循风格

print(tb.toolButtonStyle())

window.show()
sys.exit(app.exec_())

import sys

from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QToolButton的使用")
window.resize(500, 500)
window.move(400, 250)

tb = QToolButton(window)
tb.setText("工具")
tb.setIcon(QIcon("../Icons/search_48px.ico"))  # 同时设置文本和图标，只显示图标
tb.setIconSize(QSize(50, 50))
tb.setToolTip("这是一个提示")  # 鼠标放在按钮上一段时间后出现提示信息

window.show()

sys.exit(app.exec_())

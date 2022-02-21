import sys

from PyQt5.Qt import *

"""QCommandLinkButton 继承自 QPushButton"""
# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QCommandLinkButton的使用")
window.resize(500, 500)
window.move(400, 250)

btn = QCommandLinkButton("标题", "描述", window)
btn.setText("标题2")
btn.setDescription("这是描述2")
btn.setIcon(QIcon("../Icons/play_48px.ico"))


# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

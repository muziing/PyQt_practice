from PyQt5.Qt import *
import sys
# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QToolButton的使用")
window.resize(500, 500)
window.move(400, 250)

tb = QToolButton(window)
tb.setText("工具")
tb.setIcon(QIcon('../Icons/search_48px.ico'))  # 同时设置文本和图标，只显示图标
tb.setIconSize(QSize(50, 50))
tb.setToolTip("这是一个提示")  # 鼠标放在按钮上一段时间后出现提示信息

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

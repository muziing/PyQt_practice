import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QCheckBox-功能使用")
window.resize(500, 500)
window.move(400, 250)


cb1 = QCheckBox("&Python", window)
cb1.setIcon(QIcon("../Icons/python_96px.ico"))
cb1.setIconSize(QSize(40, 40))
cb1.move(150, 100)
cb1.setTristate(True)  # 支持三态
# print(cb1.isTristate())
cb1.setCheckState(Qt.PartiallyChecked)  # 设置为半选中状态
# cb1.setCheckState(Qt.Checked)  # 设置为完全选中状态


cb2 = QCheckBox("&Java", window)
cb2.setIcon(QIcon("../Icons/Java_96px.ico"))
cb2.setIconSize(QSize(40, 40))
cb2.move(150, 150)


# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

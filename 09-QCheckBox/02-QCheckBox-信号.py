import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QCheckBox-信号")
window.resize(500, 500)
window.move(400, 250)

cb = QCheckBox("Python", window)
cb.setIcon(QIcon("../Icons/python_96px.ico"))
cb.setTristate(True)
# cb.stateChanged.connect(lambda state: print(state))
cb.toggled.connect(lambda isChecked: print(isChecked))

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

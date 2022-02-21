import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QLineEdit-文本修改状态")
window.resize(500, 500)
window.move(400, 250)

le = QLineEdit(window)


def cao():
    print(le.isModified())
    le.setModified(False)  # 重置文本修改状态


btn = QPushButton("显示", window)
btn.move(200, 0)
btn.clicked.connect(cao)

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

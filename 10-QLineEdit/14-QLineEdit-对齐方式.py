import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QLineEdit-对齐方式")
window.resize(500, 500)
window.move(400, 250)

le = QLineEdit(window)
le.resize(200, 200)
# le.setAlignment(Qt.AlignHCenter)  # 水平居中
# le.setAlignment(Qt.AlignVCenter)  # 垂直居中
# le.setAlignment(Qt.AlignCenter)  # 居中
# le.setAlignment(Qt.AlignTop)  # 上对齐
le.setAlignment(Qt.AlignRight | Qt.AlignBottom)  # 右下角
le.setTextMargins(0, 0, 20, 20)  # 离右下角稍有距离

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

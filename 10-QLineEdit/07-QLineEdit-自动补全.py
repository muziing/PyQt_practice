import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QLineEdit-自动补全")
window.resize(500, 500)
window.move(400, 250)

account_le = QLineEdit(window)
account_le.move(100, 150)
account_le.setPlaceholderText("请输入账号")

completer = QCompleter(["muzing", "W2", "wanger", "root"], account_le)  # 创建填充器
account_le.setCompleter(completer)  # 给 le 设置填充器

pwd_le = QLineEdit(window)
pwd_le.setPlaceholderText("请输入密码")
pwd_le.move(100, 180)

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

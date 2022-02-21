import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QLineEdit-文本输出模式")
window.resize(500, 500)
window.move(400, 250)
"""
    NoEcho = 1  # 类似 Linux 下密码输入
    Normal = 0
    Password = 2
    PasswordEchoOnEdit = 3  # 用户输入时为明文，结束编辑后变密文
    """
le = QLineEdit(window)
le.move(100, 150)
# le.setEchoMode(QLineEdit.NoEcho)
# le.setEchoMode(2)
le.setEchoMode(3)

lb = QLabel(window)
lb.move(110, 200)
btn = QPushButton("显示", window)
btn.move(130, 250)


def show_le_text():
    lb.setText(le.text())
    # lb.setText(le.displayText())  # 只显示用户看到的内容
    lb.adjustSize()


btn.clicked.connect(show_le_text)
# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

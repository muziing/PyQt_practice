import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QLineEdit-文本的设置与获取-案例")
window.resize(500, 500)
window.move(400, 250)

le_a = QLineEdit(window)
le_a.move(100, 150)

le_b = QLineEdit(window)
le_b.move(100, 200)

copy_btn = QPushButton("复制", window)
copy_btn.move(300, 200)
copy_btn.clicked.connect(lambda: le_b.setText(le_a.text()))

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

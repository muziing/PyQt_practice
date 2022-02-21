import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QLineEdit-文本边距设定")
window.resize(500, 500)
window.move(400, 250)

le = QLineEdit(window)
le.move(100, 100)
le.resize(300, 300)
# le .setContentsMargins(100, 0, 0, 0)  # 修改输入框的边距 (左, 上, 右, 下)
le.setStyleSheet("background-color: cyan;")
le.setTextMargins(100, -180, 0, 0)  # 修改文字区域的边距 (左, 上, 右, 下)
print(le.getTextMargins())

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

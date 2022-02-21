import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QPUshButton-扁平化")
window.resize(500, 500)
window.move(400, 250)

btn = QPushButton("按钮", window)
btn.move(190, 200)
btn.setStyleSheet("background-color: cyan")

btn.setFlat(True)
print("btn是否为扁平化：", btn.isFlat())
# 设置扁平化之后，按钮的背景也不再绘制

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

from PyQt5.Qt import *
import sys
# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QToolButton-自动提升")
window.resize(500, 500)
window.move(400, 250)

tb = QToolButton(window)
tb.setText("QToolButton")
tb.setIcon(QIcon('../Icons/image_48px.ico'))
tb.setAutoRaise(True)  # 设置自动提升 （类似 QPushButton 的扁平化）
print(tb.autoRaise())

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

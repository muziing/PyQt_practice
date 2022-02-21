import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("最小最大尺寸限定")
# window.resize(500, 500)
# window.setFixedSize(500, 500)
window.setMinimumSize(200, 200)
# window.setMinimumHeight(200)
window.setMaximumSize(500, 500)
# window.resize(1000, 1000)  # 同样受到500*500的限制
# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

import sys

from PyQt5.Qt import *

app = QApplication(sys.argv)

w1 = QWidget()

w1.setWindowTitle("w1")
w1.resize(500, 500)
w1.move(400, 250)

print(w1.windowState() == Qt.WindowNoState)
# w1.setWindowState(Qt.WindowMinimized)  # 最小化窗口
# w1.setWindowState(Qt.WindowMaximized)  # 最大化窗口

w1.show()

w2 = QWidget()
w2.setWindowTitle("w2")
w2.setWindowState(Qt.WindowActive)  # 设置为活动窗口
w2.show()

sys.exit(app.exec_())

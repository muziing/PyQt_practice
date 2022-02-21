import sys

from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QToolButton-自动提升")
window.resize(500, 500)
window.move(400, 250)

tb = QToolButton(window)
tb.setText("QToolButton")
tb.setIcon(QIcon("../Icons/image_48px.ico"))
tb.setAutoRaise(True)  # 设置自动提升 （类似 QPushButton 的扁平化）
print("tb的自动提升状态为", tb.autoRaise())

window.show()

sys.exit(app.exec_())

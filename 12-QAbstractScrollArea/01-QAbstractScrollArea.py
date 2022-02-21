import sys

from PyQt5.Qt import *

# 滚动区域的低级抽象
# 继承自QFrame
app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("QAbstractScrollArea")
window.resize(500, 500)
# window.move(400, 250)

te = QTextEdit("社会顺哥", window)

# te.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)  # 长度超出显示范围后自动添加滚动条（默认值） 0
te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # 始终有滚动条 2
# te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 始终没有滚动条 1
te.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

print(te.verticalScrollBarPolicy())

btn = QPushButton(window)
btn.setIcon(QIcon("../Icons/python_96px.ico"))

te.setCornerWidget(btn)  # 设置横纵滚动条构成角落位置的控件

window.show()

sys.exit(app.exec_())

import sys

from PyQt5.Qt import *

"""
QPushButton 默认无排他性
QRadioButton 默认有排他性
QCheckBox  默认无排他性
"""
app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QAbstractButton排他性")
window.resize(500, 500)
window.move(400, 250)

for i in range(3):
    btn = QCheckBox(window)
    btn.setText(f"btn{i}")
    btn.move(50 * i, 50 * i)

    btn.setAutoExclusive(True)  # 设置排他性
    print(btn.autoExclusive())
    # btn.setCheckable(True)

btn = QPushButton(window)
btn.setText("btn3")
btn.move(250, 250)
btn.setCheckable(True)  # btn3 没有设置排他性，不受btn0~2的影响，可以自由被选中

window.show()

sys.exit(app.exec_())

from PyQt5.Qt import *
import sys
"""
QPushButton 默认无排他性
QRadioButton 默认有排他性
QCheckBox  默认无排他性"""
# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

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

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

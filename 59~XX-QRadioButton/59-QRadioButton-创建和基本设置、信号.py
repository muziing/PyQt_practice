from PyQt5.Qt import *
import sys
# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QRadioButton的创建")
window.resize(500, 500)
window.move(400, 250)

rb_male = QRadioButton("男-&Male", window)
rb_male.setIcon(QIcon('../Icons/man_96px.ico'))
rb_male.setShortcut("Alt+M")
rb_male.move(100, 100)
rb_male.setChecked(True)

rb_female = QRadioButton("女-&Female", window)
rb_female.setIcon(QIcon('../Icons/woman_96px.ico'))
rb_female.move(100, 150)
rb_female.toggled.connect(lambda isChecked: print(isChecked))  # 选中状态发生改变时
rb_female.setAutoExclusive(False)  # 取消了独占性
"""独占性：在同一父控件下，且独占性为True的控件之间才存在"""
# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

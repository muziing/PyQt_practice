import sys

from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QRadioButton-多组互斥问题")
window.resize(500, 500)
window.move(400, 250)

red = QWidget(window)
red.resize(200, 200)
red.setStyleSheet("background-color: red;")
red.move(50, 50)

green = QWidget(window)
green.resize(200, 200)
green.setStyleSheet("background-color: green;")
green.move(red.x() + red.width(), red.y() + red.height())

# 处理多组互斥——糟糕的解决方案：创建多个父控件，同组的放在同一个父控件中
# 好的解决方案：QButtonGroup

rb_male = QRadioButton("男", red)
rb_male.move(10, 10)
rb_female = QRadioButton("女", red)
rb_female.move(60, 10)

rb_yes = QRadioButton("yes", green)
rb_yes.move(10, 20)
rb_no = QRadioButton("no", green)
rb_no.move(60, 20)

window.show()

sys.exit(app.exec_())

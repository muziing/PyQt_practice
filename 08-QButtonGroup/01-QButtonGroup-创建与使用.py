import sys

from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QButtonGroup的使用")
window.resize(500, 500)
window.move(400, 250)

rb_male = QRadioButton("男", window)
rb_male.move(100, 100)
rb_female = QRadioButton("女", window)
rb_female.move(180, 100)

sex_group = QButtonGroup(window)
sex_group.addButton(rb_male)  # 把rb_male按钮添加到sex_group按钮组
sex_group.addButton(rb_female)  # 把rb_female按钮添加到sex_group按钮组

rb_yes = QRadioButton("yes", window)
rb_yes.move(100, 220)
rb_no = QRadioButton("no", window)
rb_no.move(180, 220)

answer_group = QButtonGroup(window)
answer_group.addButton(rb_yes)
answer_group.addButton(rb_no)

"""
男、女属于同一按钮组，互斥，只能选中其中之一
yes、no属于另一按钮组，不受男女的影响
"""

window.show()

sys.exit(app.exec_())

import sys

from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QButtonGroup-查看按钮")
window.resize(500, 500)
window.move(400, 250)

rb_male = QRadioButton("男", window)
rb_male.move(100, 100)
rb_male.setChecked(True)
rb_female = QRadioButton("女", window)
rb_female.move(180, 100)

sex_group = QButtonGroup(window)
sex_group.addButton(rb_male, 1)  # 1 为设置的 id，默认为-1 系统会自动分配
sex_group.addButton(rb_female, 2)
sex_group.removeButton(rb_female)  # 从组中移除按钮

rb_yes = QRadioButton("yes", window)
rb_yes.move(100, 220)
rb_no = QRadioButton("no", window)
rb_no.move(180, 220)

answer_group = QButtonGroup(window)
answer_group.addButton(rb_yes)
answer_group.addButton(rb_no)

answer_group.setId(rb_yes, 1)  # 除了在 addButton 时设置 id，也可以独立设置
answer_group.setId(rb_no, 2)

print("rb_no的id是：", answer_group.id(rb_no))
print("answer_group中被选中按钮的id：", answer_group.checkedId())  # -1 表示没有按钮被选中

# answer_group.setExclusive(False)  # 把一个按钮组取消独占，里面的单选按钮不再互斥
# print(answer_group.exclusive())

print(sex_group.buttons())
print(sex_group.button(2))  # sex_group 中 id 为 2 的按钮
print(sex_group.checkedButton())  # 被选中的按钮

# 2.3展示控件
window.show()

sys.exit(app.exec_())

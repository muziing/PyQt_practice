from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QButtonGroup-信号")
window.resize(500, 500)
window.move(400, 250)

rb_male = QRadioButton("男", window)
rb_male.move(100, 100)
rb_female = QRadioButton("女", window)
rb_female.move(180, 100)

sex_group = QButtonGroup(window)
sex_group.addButton(rb_male, 1)
sex_group.addButton(rb_female, 2)


def test(val):
    # print(sex_group.id(val))
    print(val)


# sex_group.buttonToggled.connect(test)  # 按钮状态发生改变时发送的信号
sex_group.buttonClicked.connect(test)  # 按钮被点击 信号为按钮对象
# sex_group.buttonClicked[int].connect(test)  # 信号为按钮的 id
# sex_group.buttonPressed.connect(test)  # 按钮按下时发射此信号
# sex_group.buttonReleased().connect(test)  # 按钮松开时发射此信号

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

from PyQt5.Qt import *
import sys
# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QAbstractButton-状态设置")
window.resize(500, 500)
window.move(400, 250)

btn = QPushButton(window)
icon = QIcon('./Icons/minus_48px.ico')
btn.setIcon(icon)

push_button = QPushButton(window)
push_button.setText("这是QPushButton")
push_button.move(100, 100)
push_button.setStyleSheet("QPushButton:pressed {background-color: red;}")  # 通过QSS设置了按下时的样式

radio_button = QRadioButton(window)
radio_button.setText("这是radio")
radio_button.move(100, 150)

check_box = QCheckBox(window)
check_box.setText("这是check_box")
check_box.move(100, 200)

# 把三个按钮都置为按下状态
# push_button.setDown(True)
# radio_button.setDown(True)
# check_box.setDown(True)

push_button.setCheckable(True)  # 设置按钮为可被选中
print("push_button 是否能被选中：", push_button.isCheckable())
print("radio_button 是否能被选中：", radio_button.isCheckable())
print("check_box 是否能被选中：", check_box.isCheckable())

push_button.setChecked(True)  # 设置为被选中
radio_button.setChecked(True)
check_box.setChecked(True)
print("push_button是否被选中了：", push_button.isChecked())
print("radio_button是否被选中了：", radio_button.isChecked())
print("check_box是否被选中了：", check_box.isChecked())


def cao():
    push_button.toggle()  # 交换 非选中/被选中 状态
    radio_button.toggle()
    # check_box.toggle()
    check_box.setChecked(not check_box.isChecked())  # 等同于 toggle()


btn.pressed.connect(cao)

check_box.setEnabled(False)  # 设置不可用，但仍然可被 btn 的槽函数控制是否被选中

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

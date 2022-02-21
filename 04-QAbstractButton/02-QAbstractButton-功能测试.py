import sys

from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("按钮的功能测试")
window.resize(500, 500)
window.move(400, 250)

btn = QPushButton(window)

# ==============文本操作=============
btn.setText("1")


def plus_one():
    num = str(int(btn.text()) + 1)
    btn.setText(num)


btn.pressed.connect(plus_one)


# ==============图标操作=============
icon = QIcon("./Icons/cross_48px.ico")  # 通过文件路径设置图标
size = QSize(40, 40)  # 通过(int, int)设置图标大小
btn.setIcon(icon)
btn.setIconSize(size)
# print(btn.icon())
# print(btn.iconSize())  # 获取图标大小


# ==============快捷键的设定=============
# btn.setText("&abc")  # 快速添加快捷键，按键为 Alt + 紧贴'&'符号后面的字母
# btn.setShortcut("Alt+a")  # 通过字符串设置快捷键，注意加号'+'左右不能有空格
# btn.pressed.connect(lambda: print("按钮被点击了"))


# ==============自动重复=============
btn.setAutoRepeat(True)  # 启动自动重复
btn.setAutoRepeatDelay(1000)  # 按住多长时间（毫米）之后才开始自动重复
# btn.setAutoRepeatInterval(1000)  # 每隔 1000ms 检测一次
# print(btn.autoRepeat())
# print(btn.autoRepeatDelay())
# print(btn.autoRepeatInterval())


window.show()
sys.exit(app.exec_())

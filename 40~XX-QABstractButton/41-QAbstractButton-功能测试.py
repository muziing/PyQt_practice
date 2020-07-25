from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("按钮的功能测试")
window.resize(500, 500)
window.move(400, 250)

btn = QPushButton(window)

# ==============文本操作=============开始
# btn.setText('1')
#
#
# def plus_one():
#     num = str(int(btn.text()) + 1)
#     btn.setText(num)
#
#
# btn.pressed.connect(plus_one)
# ==============文本操作=============结束


# ==============图标操作=============开始
icon = QIcon('./Icons/cross_48px.ico')  # 通过文件路径设置图标
size = QSize(40, 40)  # 通过(int, int)设置图标大小
btn.setIcon(icon)
btn.setIconSize(size)
print(btn.icon())
print(btn.iconSize())  # 获取图标大小
# ==============图标操作=============结束


# ==============快捷键的设定=============开始
# btn.setText("&abc")  # 快速添加快捷键，按键为 Alt + 紧贴'&'符号后面的字母
btn.setShortcut("Alt+a")  # 通过字符串设置快捷键，注意加号'+'左右不能有空格
btn.pressed.connect(lambda: print("按钮被点击了"))
# ==============快捷键的设定=============结束

window.show()
sys.exit(app.exec_())

import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QLineEdit-光标位置控制")
window.resize(500, 500)
window.move(400, 250)

le = QLineEdit(window)
le.move(100, 100)

btn = QPushButton("按钮", window)
btn.move(100, 200)


def cursor_move():
    # le.cursorBackward(False, 2)  # 光标向后移动，不选中，步长为2
    # le.cursorBackward(True, 2)  # 光标向后移动，选中文本，步长为2
    # le.cursorForward(False, 2)  # 光标向前移动
    # le.cursorWordBackward(True)  # 向后移动一个单词的长度
    # le.cursorWordForward(True)  # 向后移动一个单词的长度
    # le.home(False)  # 移动光标到行首
    # le.end(False)  # 移动光标到行尾
    # le.setCursorPosition(int(len(le.text()) / 2))  # 移动光标到行中
    # print(le.cursorPosition())
    print(le.cursorPositionAt(QPoint(55, 5)))  # 获取这一点坐标的字符，在字符串中的位置
    le.setFocus()


btn.clicked.connect(cursor_move)

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

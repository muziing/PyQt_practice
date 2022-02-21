import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QLineEdit-编辑功能")
window.resize(500, 500)
window.move(400, 250)

le = QLineEdit(window)
le.move(100, 100)
le.setDragEnabled(True)  # 设置为可以 拖拽

le2 = QLineEdit(window)
le2.move(100, 150)
le2.setDragEnabled(False)  # 不能将le2中的文本拖拽到le中

btn = QPushButton("按钮", window)
btn.move(280, 100)


def cao():
    # le.backspace()  # 和键盘上 backspace 键有所不同，不能删除选中的多个字符
    # le.del_()
    le.clear()  # 清空 （也可以用setText('')来实现）
    # le.cursorBackward(True, 3)
    # # le.copy()  # 先选中一段文本，才能复制
    # le.cut()  # 剪切
    # le.setCursorPosition(0)
    # le.paste()
    # le.undo()  # 撤销
    # # print(le.isUndoAvailable())
    # le.redo()  # 重做
    # # print(le.isRedoAvailable())


btn.clicked.connect(cao)

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

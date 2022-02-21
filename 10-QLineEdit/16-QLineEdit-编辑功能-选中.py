import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QLineEdit-选中")
window.resize(500, 500)
window.move(400, 250)

le = QLineEdit(window)
le.move(100, 100)

btn = QPushButton("按钮", window)
btn.move(280, 100)


def cao():
    # le.setSelection(2, 1)  # 从第二个字符开始选择，选中长度为 1 的
    # le.selectAll()  # 选中所有
    # le.setSelection(0, len(le.text()))  # 选中所有
    # le.deselect()  # 取消选中
    print(le.hasSelectedText())  # 是否有选中的文本
    print(le.selectedText())  # 获取选中的文本
    print(le.selectionStart())  # 选中的开始位置
    print(le.selectionEnd())  # 选中的结束位置


btn.clicked.connect(cao)


# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

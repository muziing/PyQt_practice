import sys

from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QLineEdit-信号")
window.resize(500, 500)
window.move(400, 250)

le = QLineEdit(window)
le.move(100, 100)
btn = QPushButton("按钮", window)
btn.move(100, 150)

le.textEdited.connect(lambda val: print("文本框被编辑了", val))  # 被编辑时发射的信号，传出文本框当前内容
le.textChanged.connect(lambda val: print("文本框内容发生改变", val))  # 改变时发射的信号，传出文本框当前内容
le.setText("用代码改变文本框内容，以测试信号")  # 会触发textChange信号；不是用户做出的编辑，不会触发textEdited信号

# le.returnPressed.connect(lambda: print("回车键被按下了"))
# le.editingFinished.connect(lambda: print("结束编辑"))  # 失去焦点时认为是结束编辑，发射这个信号
# le.cursorPositionChanged.connect(lambda old_pos, new_pos: print(old_pos, new_pos))  # 光标的移动发射的信号，传出旧新两个光标位置参数
le.selectionChanged.connect(
    lambda: print("选中文本发生改变", le.selectedText())
)  # 光标按下并有移动即触发，不是选中范围改变才触发

window.show()

sys.exit(app.exec_())

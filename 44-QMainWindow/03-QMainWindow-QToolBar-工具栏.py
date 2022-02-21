import sys

from PyQt5.Qt import *

"""
Qt.ToolBarArea:
NoToolBarArea = 0
LeftToolBarArea = 1
RightToolBarArea = 2
TopToolBarArea = 4
BottomToolBarArea = 8
"""


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QToolBar-工具栏")
        self.resize(500, 500)
        self.move(400, 250)
        self.toolbar = QToolBar(self)
        self.text_edit = QTextEdit(self)
        self.setup_ui()

    def set_tool_bar(self):
        self.toolbar.setFloatable(False)  # 是否允许工具栏脱离主窗口悬浮，默认为True
        self.toolbar.addAction("关闭窗口", lambda: self.close())
        # 增加action时可设置图标、名称、槽函数
        self.toolbar.addAction(
            QIcon("../Icons/text-icons/undo_96px.ico"), "撤销", self.text_edit.undo
        )
        self.toolbar.addAction(
            QIcon("../Icons/text-icons/redo_96px.ico"), "重做", self.text_edit.redo
        )

    def setup_ui(self):
        self.setCentralWidget(self.text_edit)
        # ------工具栏--------
        self.set_tool_bar()  # 设置工具栏
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)  # 指定创建时工具栏停靠的区域


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

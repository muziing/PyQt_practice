import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainTextEdit-信号")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        pte = QPlainTextEdit(self)
        pte.move(75, 50)
        pte.resize(350, 350)

        pte.textChanged.connect(lambda: print("内容发生了改变"))
        # pte.selectionChanged.connect(lambda: print('选中发生了改变', pte.textCursor().selectedText()))
        # pte.modificationChanged.connect(lambda val: print('修改状态发生改变', val))
        # pte.cursorPositionChanged.connect(lambda: print('光标位置发生了改变'))
        # pte.blockCountChanged.connect(lambda bc: print('块的个数发生了改变', bc))

        # pte.copyAvailable.connect(lambda val: print('复制可用时', val))
        # pte.redoAvailable.connect(lambda val: print('重做可用时', val))
        # pte.undoAvailable.connect(lambda val: print('撤销可用时', val))

        pte.updateRequest.connect(
            lambda rect, dy: print("内容区域更新", rect, dy)
        )  # 重新绘制时发送的信号，dy为滚动距离


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

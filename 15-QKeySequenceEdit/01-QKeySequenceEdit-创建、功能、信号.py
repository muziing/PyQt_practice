import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QKeySequenceEdit")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        kse = QKeySequenceEdit(self)
        kse.move(100, 100)
        # ks = QKeySequence("Ctrl+C")
        # ks = QKeySequence(QKeySequence.Copy)
        ks = QKeySequence(Qt.CTRL + Qt.Key_C, Qt.CTRL + Qt.Key_A)
        kse.setKeySequence(ks)
        # kse.clear()

        btn = QPushButton("测试按钮", self)
        btn.move(350, 100)
        btn.clicked.connect(
            lambda: print(kse.keySequence().toString(), kse.keySequence().count())
        )

        kse.editingFinished.connect(lambda: print("结束编辑"))  # 编辑结束时发射的信号（往往是1s之后）
        kse.keySequenceChanged.connect(
            lambda key_val: print("键位序列发生改变", key_val.toString())
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

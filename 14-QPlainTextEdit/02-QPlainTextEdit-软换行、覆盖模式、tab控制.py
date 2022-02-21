import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainTextEdit")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        test_btn = QPushButton("测试按钮", self)
        test_btn.move(20, 20)
        pte = QPlainTextEdit(self)
        pte.move(100, 100)
        pte.resize(300, 300)

        # --------自动换行-------------
        print(pte.lineWrapMode())
        pte.setLineWrapMode(QPlainTextEdit.NoWrap)  # 取消自动换行
        """
        NoWrap = 0
        WidgetWidth = 1
        """

        # ------覆盖模式-----------
        print(pte.overwriteMode())  # 默认值为False
        # pte.setOverwriteMode(True)  # 覆盖单个字符，对中文支持不佳

        # -----Tab控制-------
        # pte.setTabChangesFocus(True)  # 将Tab键功能改为切换焦点
        pte.setTabChangesFocus(False)  # 将Tab键功能改为插入制表符
        pte.setTabStopDistance(100)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

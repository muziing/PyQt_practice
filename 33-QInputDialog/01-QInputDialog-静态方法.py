import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # result = QInputDialog.getInt(self, "窗口标题", "请输入一个整数", 666, step=10)
        # result = QInputDialog.getDouble(self, "窗口标题", "请输入一个小数", 66.6, decimals=3)
        # result = QInputDialog.getText(self, "窗口标题", "提示标签", echo=QLineEdit.Password)
        # result = QInputDialog.getMultiLineText(self, "窗口标题", "输入多行文本", "default")
        result = QInputDialog.getItem(
            self, "窗口标题", "选择一项", ["1", "2", "3"], 2, True
        )  # 默认选择第三项，可以编辑
        print(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

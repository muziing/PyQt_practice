import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QErrorMessage")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        em = QErrorMessage(self)
        em.setWindowTitle("错误提示")

        em.showMessage("在此处展示一些错误提示信息")  # 设置内容文本，调用这个方法还会使窗口自动弹出，非模态
        em.showMessage("在此处展示一些错误提示信息")
        em.showMessage("在此处展示一些错误提示信息")  # 取消勾选后可以跳过提示信息完全相同的其他提示框
        em.showMessage("另外的一些错误提示信息")  # 提示信息不同的其他提示框依然会显示

        # em.exec()  # 应用程序级的模态


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

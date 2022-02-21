import sys
from time import sleep

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressDialog")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # pd = QProgressDialog(self)  # 默认等待4秒后弹出，若在4秒内进度条走完，则不弹出显示
        pd = QProgressDialog("说明性文字", "取消按钮的文字", 1, 1000, self)  # 两个int为进度条范围
        pd.setAutoClose(False)  # 进度条走完后是否自动关闭，默认值为True
        pd.setAutoReset(False)  # 进度条走完后是否自动重置，默认值为True

        pd.open(lambda: print("对话框被取消"))  # 窗口级别模态窗口
        # pd.show()  # 非模态

        pd.setMinimumDuration(0)  # 设置最小等待时间
        # pd.setValue(50)
        for i in range(1, 101):
            # sleep(1)  # 简易测试，会导致程序卡死
            pd.setValue(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

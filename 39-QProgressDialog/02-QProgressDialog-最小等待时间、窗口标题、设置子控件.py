import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressDialog")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        pd = QProgressDialog(self)  # 默认等待4秒后弹出，若在4秒内进度条走完，则不弹出显示
        pd.setWindowTitle("正在下载……")  # 设置窗口标题
        pd.setMinimumDuration(0)  # 设置最小等待时间

        pd.setLabelText("Label中的说明性文字")
        print(pd.labelText())
        pd.setCancelButtonText("取消按钮")

        # --------设置子控件---------
        # pd.setCancelButton(QPushButton)
        # pd.setBar(QProgressBar)
        # pd.setLabel(QLabel)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

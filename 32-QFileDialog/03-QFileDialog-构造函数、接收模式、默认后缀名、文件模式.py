import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFiledialog-构造函数")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        def test():
            fd = QFileDialog(
                self, "选择一个文件", "./", "ALL(*, *);;Images(*.png *.jpg);;Python文件(*.py)"
            )
            # -------接收模式-----------
            # fd.setAcceptMode(QFileDialog.AcceptOpen)  # 打开
            fd.setAcceptMode(QFileDialog.AcceptSave)  # 保存
            # ------默认后缀名----------
            fd.setDefaultSuffix("txt")
            # ------设置文件模式--------
            fd.setFileMode(QFileDialog.AnyFile)  # 任何文件
            # fd.setFileMode(QFileDialog.ExistingFile)  # 存在的文件（单个）
            # fd.setFileMode(QFileDialog.ExistingFiles)  # 存在的文件（多个）
            # fd.setFileMode(QFileDialog.Directory)  # 目录
            fd.open()
            fd.fileSelected.connect(lambda file: print(file))

        btn = QPushButton(self)
        btn.setText("测试按钮")
        btn.move(200, 100)
        btn.clicked.connect(test)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

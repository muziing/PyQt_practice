import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFiledialog-静态方法")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # result = QFileDialog.getExistingDirectory(self, "选择一个文件夹", "../")  # 返回值为文件夹的绝对路径
        result = QFileDialog.getExistingDirectoryUrl(
            self, "选择一个文件夹", QUrl("../")
        )  # 返回值为QUrl
        print(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

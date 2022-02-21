import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog-信号")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        def test():
            fd = QFileDialog(
                self, "选择一个文件", "./", "ALL(*, *);;Images(*.png *.jpg);;Python文件(*.py)"
            )
            fd.setFileMode(QFileDialog.ExistingFiles)

            # fd.currentChanged.connect(lambda path: print("当前路径字符串发生改变时", path))
            # fd.currentUrlChanged.connect(lambda url: print("当前路径QUrl发生改变时", url))
            # fd.directoryEntered.connect(lambda path: print("当前目录字符串进入时", path))
            # fd.directoryUrlEntered.connect(lambda url: print("当前目录QUrl进入时", url))
            # fd.filterSelected.connect(lambda filter: print("当前名称字符串被选中时发送的字符串", filter))
            fd.fileSelected.connect(lambda val: print("单个文件被选中-字符串", val))
            fd.filesSelected.connect(lambda val: print("多个文件被选中-列表[字符串]", val))
            fd.urlSelected.connect(lambda val: print("单个文件被选中-QUrl", val))
            fd.urlsSelected.connect(lambda val: print("多个文件被选中-列表[url]", val))

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

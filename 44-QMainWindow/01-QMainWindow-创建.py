from PyQt5.Qt import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.td = QTextEdit()
        self.setWindowTitle("QMainWindow")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def open_file(self):
        result = QFileDialog.getOpenFileName(self, "选择一个py文件", "../",
                                             "ALL(*, *);;Images(*.png *.jpg);;Python文件(*.py)",
                                             "Python文件(*.py)")
        with open(result[0], 'r', encoding="UTF-8") as f:
            self.td.setText(f.read())

    def setup_ui(self):
        self.setCentralWidget(self.td)

        toolbar = QToolBar()
        toolbar.addAction("打开文件", self.open_file)
        toolbar.addAction("关闭", lambda: self.close())
        self.addToolBar(toolbar)

        sb = QStatusBar()
        sb.showMessage("一条状态栏消息")
        self.setStatusBar(sb)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

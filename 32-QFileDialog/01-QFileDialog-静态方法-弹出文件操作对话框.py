import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # result = QFileDialog.getOpenFileName(self, "选择一个py文件", "../",
        #                                      "ALL(*, *);;Images(*.png *.jpg);;Python文件(*.py)",
        #                                      "Python文件(*.py)")
        # result = QFileDialog.getOpenFileNames(self, "选择一个py文件", "../",
        #                                       "ALL(*, *);;Images(*.png *.jpg);;Python文件(*.py)",
        #                                       "Python文件(*.py)")
        # result = QFileDialog.getOpenFileUrl(self, '选择一个py文件', '../', '所有文件(*.*);;Python文件(*.py);;图片(*.png *.jpg)')
        result = QFileDialog.getSaveFileName(
            self,
            "保存为py文件",
            "../",
            "ALL(*, *);;Images(*.png *.jpg);;Python文件(*.py)",
            "Python文件(*.py)",
        )
        print(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog-功能作用")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        def test():
            fd = QFileDialog(self, "选择一个文件", "./")
            # ---------名称过滤器------------
            # fd.setNameFilter("图片(*.jpg *.png *.jpeg)")
            fd.setNameFilters(
                ("Python文件(*.py)", "图片(*.jpg *.png *.jpeg)")
            )  # 在可迭代对象如元组中写多个过滤器而非使用;;分隔

            # ------显示信息的详细程度-------
            fd.setViewMode(QFileDialog.Detail)
            # fd.setViewMode(QFileDialog.List)  # 在win10 Ubuntu 20.04 下没用

            # ------设置指定角色的标签名称---------
            fd.setLabelText(QFileDialog.FileName, "muzing的文件")
            fd.setLabelText(QFileDialog.Accept, "打打打 打开")
            fd.setLabelText(QFileDialog.Reject, "取取取 取消")
            # fd.setLabelText(QFileDialog.FileType, "")  # 仅保存时有效
            # fd.setLabelText(QFileDialog.LookIn, "LookIn")
            fd.open()

        btn = QPushButton("测试按钮", self)
        btn.move(200, 100)
        btn.clicked.connect(test)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

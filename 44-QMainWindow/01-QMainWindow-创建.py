from PyQt5.Qt import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit(self)
        self.status_bar = QStatusBar(self)
        self.menu_bar = QMenuBar(self)
        self.toolbar = QToolBar(self)

        self.setWindowTitle("QMainWindow")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, "选择一个py文件", "../",
                                                "ALL(*, *);;Images(*.png *.jpg);;Python文件(*.py)",
                                                "Python文件(*.py)")[0]
        if file_name:
            with open(file_name, 'r', encoding="UTF-8") as f:
                self.text_edit.setText(f.read())
            self.status_bar.showMessage(f"成功打开了文件{file_name}")

    def setup_ui(self):
        # -------中央控件-------
        self.setCentralWidget(self.text_edit)

        # -------菜单栏--------
        self.menu_bar.addAction("打开文件", self.open_file)
        self.setMenuBar(self.menu_bar)

        # ------工具栏--------
        self.toolbar.addAction("关闭窗口", lambda: self.close())
        self.toolbar.addAction(QIcon('../Icons/text-icons/undo_96px.ico'), "撤销", self.text_edit.undo)
        self.toolbar.addAction(QIcon('../Icons/text-icons/redo_96px.ico'), "重做", self.text_edit.redo)
        self.addToolBar(self.toolbar)

        # -----状态栏----------
        self.status_bar.showMessage("一条状态栏消息")
        self.setStatusBar(self.status_bar)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

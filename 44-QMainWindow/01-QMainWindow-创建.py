import sys

from PyQt5.Qt import *


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.text_edit = QTextEdit(self)
        self.status_bar = QStatusBar(self)
        self.menu_bar = QMenuBar(self)
        self.toolbar = QToolBar(self)

        self.setWindowTitle("QMainWindow")
        self.setWindowIcon(QIcon("../Icons/python_96px.ico"))
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(
            self, "选择一个py文件", "../", "Python文件(*.py);;ALL(*, *)", "Python文件(*.py)"
        )[0]
        if file_name:
            try:
                with open(file_name, "r", encoding="UTF-8") as f:
                    self.text_edit.setText(f.read())
                self.status_bar.showMessage(f"成功打开了文件{file_name}")
            except UnicodeDecodeError:
                self.status_bar.showMessage("打开文件失败！请检查文件类型", 3000)

    def set_menu_bar(self):
        file_menu = QMenu("文件", self.menu_bar)
        file_menu.addAction("打开文件", self.open_file)
        file_menu.addSeparator()  # 增加一条分割线
        file_menu.addAction("关闭窗口", lambda: self.close())
        self.menu_bar.addMenu(file_menu)

    def set_tool_bar(self):
        self.toolbar.setFloatable(False)  # 是否允许工具栏脱离主窗口悬浮，默认为True
        self.toolbar.addAction("关闭窗口", lambda: self.close())
        self.toolbar.addAction(
            QIcon("../Icons/text-icons/undo_96px.ico"), "撤销", self.text_edit.undo
        )
        self.toolbar.addAction(
            QIcon("../Icons/text-icons/redo_96px.ico"), "重做", self.text_edit.redo
        )

    def setup_ui(self):
        # -------中央控件-------
        self.setCentralWidget(self.text_edit)

        # -------菜单栏--------
        self.set_menu_bar()
        self.setMenuBar(self.menu_bar)

        # ------工具栏--------
        self.set_tool_bar()
        self.addToolBar(self.toolbar)

        # -----状态栏----------
        self.status_bar.showMessage("一条存在5s的状态栏消息", 5000)
        self.setStatusBar(self.status_bar)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

import sys

from PyQt5.Qt import *


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QMenuBar-菜单栏")
        self.resize(500, 500)
        self.move(400, 250)
        self.menu_bar = QMenuBar(self)
        self.text_edit = QTextEdit(self)
        self.setup_ui()

    def show_about(self):
        pass

    def set_menu_bar(self):
        file_menu = QMenu("文件", self.menu_bar)  # 建一个Menu菜单
        file_menu.addAction("打开文件")  # 添加行为
        file_menu.addSeparator()  # 增加一条分割线
        file_menu.addAction("关闭窗口", lambda: self.close())

        about_menu = QMenu("关于", self.menu_bar)
        about_menu.addAction("关于作者", self.show_about)

        self.menu_bar.addMenu(file_menu)  # 把文件菜单添加到菜单栏上
        self.menu_bar.addMenu(about_menu)

    def setup_ui(self):
        self.setCentralWidget(self.text_edit)
        self.set_menu_bar()
        self.setMenuBar(self.menu_bar)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

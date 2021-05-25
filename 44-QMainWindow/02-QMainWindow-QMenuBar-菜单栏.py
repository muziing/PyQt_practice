from PyQt5.Qt import *
import sys


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QMenuBar-菜单栏")
        self.resize(500, 500)
        self.move(400, 250)
        self.menu_bar = QMenuBar(self)
        self.text_edit = QTextEdit(self)
        self.setup_ui()

    def set_menu_bar(self):
        file_menu = QMenu("文件", self.menu_bar)
        file_menu.addAction("打开文件")
        file_menu.addSeparator()  # 增加一条分割线
        file_menu.addAction("关闭窗口", lambda: self.close())
        self.menu_bar.addMenu(file_menu)

    def setup_ui(self):
        self.setCentralWidget(self.text_edit)
        self.set_menu_bar()
        self.setMenuBar(self.menu_bar)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

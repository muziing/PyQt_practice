import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        cbb = QComboBox(self)
        cbb.move(100, 100)

        # ------添加条目项-----
        cbb.addItem(QIcon("../Icons/audio_mid_48px.ico"), "XX1")
        cbb.addItem(QIcon("../Icons/audio_mute_48px.ico"), "XX2")
        cbb.addItems([str(x) for x in range(5)])  # 通过可迭代类型（字符串）快速创建多个项

        # -----插入条目项-----
        # cbb.insertItem(1, '插入的项')
        cbb.insertItems(1, ("插入1", "插入2", "插入3"))

        # ----设置条目项-----
        cbb.setItemIcon(2, QIcon("../Icons/audio_low_48px.ico"))
        cbb.setItemText(5, "被修改的文字")

        # ----删除条目-----
        cbb.removeItem(7)

        # ----插入分割线----
        cbb.insertSeparator(4)

        # ----设置当前项（设置默认项）-------
        # cbb.setCurrentIndex(1)
        # cbb.setCurrentText("当前选项")  # 若text不在选项范围中，则无效
        cbb.setCurrentText("插入1")

        # ----用户可编辑--------
        cbb.setEditable(True)  # 用户编辑的项可以作为新项加入
        cbb.setEditText("可编辑的文本")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

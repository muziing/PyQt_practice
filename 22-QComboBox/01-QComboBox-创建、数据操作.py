from PyQt5.Qt import *
import sys


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
        cbb.addItem(QIcon('../Icons/audio_mid_48px.ico'), 'XX1')
        cbb.addItem(QIcon('../Icons/audio_mute_48px.ico'), 'XX2')
        cbb.addItems([str(x) for x in range(5)])  # 通过可迭代类型（字符串）快速创建多个项

        # -----插入条目项-----
        # cbb.insertItem(1, '插入的项')
        cbb.insertItems(1, ('插入1', '插入2', '插入3'))

        # ----设置条目项-----
        cbb.setItemIcon(2, QIcon('../Icons/audio_low_48px.ico'))
        cbb.setItemText(5, '被修改的文字')

        # ----删除条目-----
        cbb.removeItem(7)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

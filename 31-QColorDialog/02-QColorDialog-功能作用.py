from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QColorDialog-功能作用")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        cd = QColorDialog(QColor(20, 154, 151), self)  # 可以传入创建时的默认颜色
        cd.setWindowTitle('选择颜色')

        def color_1(col):
            palette = QPalette()
            palette.setColor(QPalette.Background, col)
            self.setPalette(palette)

        # cd.colorSelected.connect(color_1)
        # cd.show()

        def color_2():
            palette = QPalette()
            palette.setColor(QPalette.Background, cd.selectedColor())
            self.setPalette(palette)

        cd.open(color_2)  # 可以向open中传入一个槽函数，弹出对话框后自动连接


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

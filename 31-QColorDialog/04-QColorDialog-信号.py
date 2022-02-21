import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QColorDialog-信号")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton("测试按钮", self)
        btn.move(100, 100)

        def test():
            cd = QColorDialog(self)

            def sel_color(color):
                palette = QPalette()
                palette.setColor(QPalette.ButtonText, color)
                self.setPalette(palette)

            # cd.colorSelected.connect(sel_color)
            cd.currentColorChanged.connect(sel_color)

            cd.show()

        btn.clicked.connect(test)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

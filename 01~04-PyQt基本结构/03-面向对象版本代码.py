from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("社会我顺哥，人狠话不多")
        self.resize(500, 500)
        self.move(400, 250)

    def setup_ui(self):
        label = QLabel(self)
        label.setText("Hello world")
        label.move(200, 240)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.setup_ui()
    window.show()

    sys.exit(app.exec_())

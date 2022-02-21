import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        gl = QGridLayout()
        self.setLayout(gl)

        label1 = QLabel("QLabel_1")
        label1.setStyleSheet("background-color: red;")
        label2 = QLabel("QLabel_2")
        label2.setStyleSheet("background-color: yellow;")
        label3 = QLabel("QLabel_3")
        label3.setStyleSheet("background-color: cyan;")

        gl.addWidget(label1, 0, 0)
        gl.addWidget(label2, 0, 1)
        gl.addWidget(label3, 1, 0, 1, 2)

        print(gl.getItemPosition(1))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

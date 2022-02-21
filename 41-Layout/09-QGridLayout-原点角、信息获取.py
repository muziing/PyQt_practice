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

        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color: red;")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color: yellow;")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color: cyan;")

        gl.addWidget(label1, 0, 0)
        gl.addWidget(label2, 0, 1)
        gl.addWidget(label3, 1, 0, 1, 2)

        print(gl.rowCount())
        print(gl.columnCount())
        print(gl.itemAtPosition(0, 1).widget().text())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    print(window.layout().cellRect(0, 0))

    sys.exit(app.exec_())

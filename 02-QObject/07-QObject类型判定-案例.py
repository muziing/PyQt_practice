import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject类型判定案例")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        self.name()

    def name(self):
        label1 = QLabel(self)
        label1.setText("这是label1")
        label1.move(100, 100)

        label2 = QLabel(self)
        label2.setText("这是label2")
        label2.move(200, 100)

        btn = QPushButton(self)
        btn.setText("点我")
        btn.move(100, 200)

        for widget in self.children():
            if widget.inherits("QLabel"):
                # print(widget, "是")
                widget.setStyleSheet("background-color: cyan;")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

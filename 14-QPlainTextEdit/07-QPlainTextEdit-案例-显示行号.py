import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainTextEdit-案例-显示行号")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        pte = QPlainTextEdit(self)
        pte.move(75, 80)
        pte.resize(350, 350)

        line_num_parent = QWidget(self)
        line_num_parent.resize(30, 350)
        line_num_parent.move(45, 80)

        line_label = QLabel(line_num_parent)
        line_label.move(0, 6)
        line_nums = "\n".join([str(i) for i in range(1, 101)])
        line_label.setText(line_nums)

        pte.updateRequest.connect(
            lambda rect, dy: line_label.move(line_label.x(), line_label.y() + dy)
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

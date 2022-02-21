import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRubberBand")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # rb = QRubberBand(QRubberBand.Line, self)
        rb = QRubberBand(QRubberBand.Rectangle, self)
        rb.setGeometry(10, 10, 60, 60)
        print(rb.isVisible())
        rb.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

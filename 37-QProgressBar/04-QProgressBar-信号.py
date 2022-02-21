import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressBar")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        pb = QProgressBar(self)
        pb.move(100, 100)

        timer = QTimer(pb)

        def change_progress():
            if pb.value() == pb.maximum():
                timer.stop()
            pb.setValue(pb.value() + 1)

        timer.timeout.connect(change_progress)
        timer.start(500)

        pb.valueChanged.connect(lambda val: print(f"当前进度值为{val}"))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

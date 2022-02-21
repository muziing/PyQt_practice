import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject类型判定")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        self.QObject类型判定()

    def QObject类型判定(self):
        obj = QObject()
        w = QWidget()
        btn = QPushButton()
        label = QLabel()

        objs = [obj, w, btn, label]
        for o in objs:
            # print(o, "是否为控件", o.isWidgetType())
            print(o.inherits("QWidget"))  # 对象是否继承自QWidget
            # print(o.inherits("QPushbutton"))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

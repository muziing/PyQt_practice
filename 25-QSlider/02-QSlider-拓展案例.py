import sys

from PyQt5.Qt import *


class MSlider(QSlider):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setTickPosition(QSlider.TicksBothSides)
        self.setup_ui()

    def setup_ui(self):
        self.label = QLabel(self)
        self.label.setText("0")
        self.label.setStyleSheet("color: red;")
        self.label.hide()

    def get_label_pos(self) -> (int, int):
        """计算label应该处于的位置"""
        x = int((self.width() - self.label.width()) / 2)
        y = int(
            (1 - self.value() / (self.maximum() - self.minimum()))
            * (self.height() - self.label.height())
        )
        return x, y

    def mousePressEvent(self, ev) -> None:
        super(MSlider, self).mousePressEvent(ev)
        self.label.move(*self.get_label_pos())
        self.label.show()
        self.label.setText(str(self.value()))
        self.label.adjustSize()

    def mouseMoveEvent(self, ev) -> None:
        super(MSlider, self).mouseMoveEvent(ev)
        self.label.move(*self.get_label_pos())
        self.label.setText(str(self.value()))
        self.label.adjustSize()

    def mouseReleaseEvent(self, ev) -> None:
        super(MSlider, self).mouseReleaseEvent(ev)
        self.label.hide()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSlider-拓展案例")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 0.创建两个控件
        slider = MSlider(self)
        slider.move(200, 200)
        slider.resize(30, 200)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

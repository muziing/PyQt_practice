import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSlider")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        sd = QSlider(self)
        """QSlider的创建等方法见QAbstractSlider"""
        sd.move(100, 100)
        sd.resize(50, 300)

        # -------刻度控制---------
        sd.setTickPosition(QSlider.TicksRight)
        """
        NoTicks = 0  无刻度线
        TicksAbove = 1  （水平滑块）上方刻度线
        TicksBelow = 2  （水平滑块）下方刻度线
        TicksBothSides = 3  两侧刻度线
        TicksLeft = 1  （垂直滑块）左侧刻度线
        TicksRight = 2  （垂直滑块）右侧刻度线
        """
        print(sd.tickPosition())
        sd.setTickInterval(5)  # 默认刻度线间距与PageUp/PageDown步长相同，也可以用这个方法单独设置刻度线密度而不影响Page步长


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

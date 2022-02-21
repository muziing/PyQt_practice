import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSlider")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText("0")
        label.move(300, 100)
        label.resize(100, 30)
        sd = QSlider(self)
        sd.move(100, 100)
        sd.valueChanged.connect(lambda val: label.setText(str(val)))
        sd.setValue(80)

        # --------滑块按下---------
        sd.setSliderDown(True)  # 手动设置滑块按下
        print(sd.isSliderDown())

        # -----可用信号----------
        # sd.valueChanged.connect(lambda val: print("value changed", val))
        # sd.sliderPressed.connect(lambda: print("slider pressed"))
        # sd.sliderReleased.connect(lambda: print("slider released"))
        # sd.sliderMoved.connect(lambda val: print("slider moved", val))
        sd.rangeChanged.connect(lambda *val: print("range changed", val))
        sd.setRange(50, 150)

        sd.actionTriggered.connect(lambda val: print("actionTriggered", val))
        """
        SliderRangeChange = 0
        SliderSingleStepAdd = 1
        SliderSingleStepSub = 2
        SliderPageStepAdd = 3
        SliderPageStepSub = 4
        SliderToMinimum = 5
        SliderToMaximum = 6
        SliderMove = 7
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

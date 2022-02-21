import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QABsTractSlider")
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

        # ------------追踪设置-----------
        """value是否跟着滑块的位置变化而立即变化，默认值为True。即使设置为False，松开鼠标后也会更新"""
        print(f"Tracking默认为{sd.hasTracking()}")
        # sd.setTracking(False)  # 手动设置为不追踪

        # -----------滑块位置-----------
        sd.setSliderPosition(88)  # 在非追踪状态下，会出现滑块位置在88但值为0的情况

        # ----------倒立外观----------
        # sd.setInvertedAppearance(True)  # 设置倒立外观，键盘方向键上下控制数值增减而不是滑块上下
        # sd.setInvertedControls(True)  # 设置键盘方向键上下控制的反转

        # --------滑块方向---------
        sd.setOrientation(Qt.Horizontal)  # 滑块方向设为水平


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

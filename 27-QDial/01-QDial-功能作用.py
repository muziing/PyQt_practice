import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDial的学习")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        dia = QDial(self)
        dia.move(200, 200)
        dia.setRange(0, 200)  # 设置数值范围
        dia.setNotchesVisible(True)  # 显示刻度, 大刻度即为PgUp/PgDn的步长
        dia.valueChanged.connect(lambda val: print("值发生了改变", val))
        dia.setPageStep(5)  # 默认值为10
        dia.setWrapping(True)  # 让刻度包裹整个圆，不留下方的缺口
        dia.setNotchTarget(25)  # 控制刻度密度


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

import sys

from PyQt5.Qt import *

"""替换鼠标图标、创建一个Label并使其跟随鼠标移动"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.move(350, 250)
        self.setWindowTitle("鼠标相关操作案例")
        self.setMouseTracking(True)

        pixmap = QPixmap("../Icons/snowflake_128px.ico").scaled(50, 50)
        cursor = QCursor(pixmap)
        self.setCursor(cursor)

        label = QLabel(self)
        self.label = label
        label.setText("世界是一只飞在空中的花朵")
        # label.move(80, 100)
        self.label.setStyleSheet("background-color: cyan; font-size: 24px;")

    def mouseMoveEvent(self, mv):
        # print("鼠标移动", mv.localPos())
        label = self.findChild(QLabel)
        label.move(int(mv.localPos().x()), int(mv.localPos().y()))


app = QApplication(sys.argv)

window = Window()

window.show()
sys.exit(app.exec_())

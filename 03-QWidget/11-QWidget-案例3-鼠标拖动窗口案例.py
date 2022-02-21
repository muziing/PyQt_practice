import sys

from PyQt5 import QtGui
from PyQt5.Qt import *

"""鼠标可以在用户区域内实现对整个窗口的拖动。（原先只能拖动标题栏时移动）"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("窗口移动的学习")
        self.resize(500, 500)
        self.move(400, 250)
        self.move_flag = False  # 设置一个标记，确保只有在执行mousePressEvent之后才会执行mouseMoveEvent
        self.setup_ui()

    def setup_ui(self):
        pass

    def mousePressEvent(self, evt):
        # print("鼠标按下")
        if evt.button() == Qt.LeftButton:  # 仅在鼠标左键按下时可以拖动
            self.move_flag = True  # 设置一个标记，确保只有在执行mousePressEvent之后才会执行mouseMoveEvent
            # 确定两个点（鼠标第一次按下的点，窗口当前所在的原始点）
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()
            # print(self.mouse_x, self.mouse_y)
            self.origen_x = self.x()
            self.origen_y = self.y()

    def mouseMoveEvent(self, evt) -> None:
        # print("鼠标移动")
        if self.move_flag:
            # print(evt.globalX(), evt.globalY())
            # 计算的是移动向量
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y
            dest_x = self.origen_x + move_x
            dest_y = self.origen_y + move_y
            self.move(dest_x, dest_y)

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.move_flag = False  # 鼠标释放后重置标记，避免无法释放拖动
        # print("鼠标释放")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.setMouseTracking(True)  # 当开启鼠标跟踪后情况有所变化，所以才需要move_flag标记
    window.show()

    sys.exit(app.exec_())

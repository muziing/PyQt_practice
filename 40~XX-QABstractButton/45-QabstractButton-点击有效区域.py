from PyQt5.Qt import *
from PyQt5 import QtGui
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QAbstractButton-点击有效区域")
window.resize(500, 500)
window.move(400, 250)


class Btn(QPushButton):
    def hitButton(self, point) -> bool:
        # print(point)
        # 案例：仅按钮右半部分为有效点击区域
        # if point.x() > self.width() / 2:
        #     # 只有在按钮的有半部分点击才有效
        #     return True
        # else:
        #     return False

        # 案例：仅正方形按钮内切圆之内的范围才是有效点击区域
        # 通过给定的点坐标，计算与圆心的距离，如果距离小于半径，则认为是有效区域，返回 True
        circle_center_x = self.width() / 2
        circle_center_y = self.height() / 2
        hit_x = point.x()
        hit_y = point.y()
        distance = ((hit_x - circle_center_x) ** 2 + (hit_y - circle_center_y) ** 2) ** 0.5
        # print(distance)
        if distance < self.width() / 2:
            return True
        else:
            return False

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        super().paintEvent(a0)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(0, 240, 240), 6))
        painter.drawEllipse(self.rect())



btn = Btn(window)
btn.setText("点击")
btn.resize(200, 200)
btn.move(100, 100)
btn.pressed.connect(lambda: print("按钮被点击了"))

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

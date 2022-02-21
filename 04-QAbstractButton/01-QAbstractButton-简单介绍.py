import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QAbstractButton")
window.resize(500, 500)
window.move(400, 250)


class Btn(QAbstractButton):
    """自定义的按钮控件，体验从按钮抽象基类继承"""

    def paintEvent(self, evt) -> None:
        # print("绘制")
        # 绘制按钮上要展示的一个界面内容
        # 手动绘制
        painter = QPainter(self)  # 创建一个画家；告诉画在什么地方
        pen = QPen(QColor(20, 154, 151), 5)  # 创建并设置一个笔
        painter.setPen(pen)  # 把笔给画家
        painter.drawText(30, 30, self.text())  # 把按钮文字画在按钮上
        painter.drawEllipse(0, 0, 100, 120)  # 画个椭圆


btn = Btn(window)
btn.setText("ABC")
btn.resize(110, 150)

btn.clicked.connect(lambda: print("点击了这个按钮"))  # 按钮被按下则执行里面的lambda函数（槽函数）

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

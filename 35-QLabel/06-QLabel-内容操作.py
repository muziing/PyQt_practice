import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel-内容操作")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.move(100, 100)

        # --------文本类型----------
        # label.setText("<img src='../Icons/OS_Ubuntu_128px.ico' width=80 height=80>")

        # --------数值类型---------
        # label.setNum(888.88)

        # ---------图形图像--------
        # label.setPixmap(QPixmap('../Icons/OS_Ubuntu_128px.ico'))  # 用于展示QPixmap，对图像显示有优化

        # pic = QPicture()  # 创建绘画设备（画布）
        # painter = QPainter(pic)
        # painter.setBrush(QBrush(QColor(0, 128, 128)))  # 设置画刷
        # painter.drawEllipse(0, 0, 200, 200)  # 绘制椭圆
        # label.setPicture(pic)  # 用于展示QPicture

        # -------动图----------
        movie = QMovie("../Icons/打墙火柴人.gif")
        label.setMovie(movie)
        movie.setSpeed(200)  # 播放速度（百分比）
        movie.start()
        # movie.setPaused(True)  # 暂停播放

        # label.clear()  # 清空


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

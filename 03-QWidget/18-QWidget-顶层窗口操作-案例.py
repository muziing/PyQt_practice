import sys

from PyQt5 import QtGui
from PyQt5.Qt import *

"""案例：创建一个无边框、半透明的窗口；自定义关闭、最大化、最小化三个按钮；实现能够点击用户区域拖动窗口"""


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置了无边框的Flag
        self.setWindowOpacity(0.85)  # 设置不透明度
        self.setWindowTitle("顶层窗口操作-案例")
        self.setWindowIcon(QIcon("../Icons/snowflake_128px.ico"))
        self.resize(500, 500)
        self.move(400, 240)
        # 公共数据 （通过保存为 self的属性来实现跨方法使用）
        self.top_margin = 1  # 三个按钮距离顶部的距离
        self.btn_w = 32  # 按钮宽度
        self.btn_h = 32  # 按钮高度

        self.setup_ui()

    def setup_ui(self):
        """在窗口的右上角添加关闭、最大化、最小化 三个按钮。注意三个按钮的位置没有在本方法中确定"""
        close_btn = QPushButton(self)
        self.close_btn = close_btn  # 通过把局部变量存储为对象属性来实现跨方法使用
        close_btn.setIcon(QIcon("../Icons/cross_48px.ico"))
        # close_btn.setText("关闭")
        close_btn.resize(self.btn_w, self.btn_h)

        max_btn = QPushButton(self)
        self.max_btn = max_btn  # 通过把局部变量存储为对象属性来实现跨方法使用
        max_btn.setIcon(QIcon("../Icons/expand_48px.ico"))
        # max_btn.setText("最大化")
        max_btn.resize(self.btn_w, self.btn_h)

        mini_btn = QPushButton(self)
        self.mini_btn = mini_btn  # 通过把局部变量存储为对象属性来实现跨方法使用
        mini_btn.setIcon(QIcon("../Icons/minus_48px.ico"))
        # mini_btn.setText("最小化")
        mini_btn.resize(self.btn_w, self.btn_h)

        # 监听按钮，连接信号与槽
        close_btn.pressed.connect(lambda: self.close())
        mini_btn.pressed.connect(lambda: self.showMinimized())

        def max_normal():
            """最大化/恢复 按钮的槽函数"""
            if self.isMaximized():
                max_btn.setIcon(QIcon("../Icons/expand_48px.ico"))
                self.label.setText("Hello World")
                self.label.setStyleSheet("font-size: 30px;")
                self.label.adjustSize()
                self.showNormal()
            else:
                self.label.setText("Life is short, use Python.")
                self.label.setStyleSheet("font-size: 40px;")
                self.label.adjustSize()
                self.showMaximized()
                max_btn.setIcon(QIcon("../Icons/contract_48px.ico"))

        max_btn.pressed.connect(max_normal)

        label = QLabel("Hello World", self)
        self.label = label
        label.setStyleSheet("font-size: 30px;")
        label.adjustSize()
        lab_x = int((self.width() - label.width()) / 2)
        lab_y = int((self.height() - label.height()) / 2)
        label.move(lab_x, lab_y)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        """当窗口大小改变时，重新移动三个按钮的位置"""
        self.close_btn.move(self.width() - self.btn_w, self.top_margin)
        self.max_btn.move(self.width() - self.btn_w * 2, self.top_margin)
        self.mini_btn.move(self.width() - self.btn_w * 3, self.top_margin)
        self.label.move(
            int((self.width() - self.label.width()) / 2),
            int((self.height() - self.label.height()) / 2),
        )

    def mousePressEvent(self, evt):
        # print("鼠标按下")
        if evt.button() == Qt.LeftButton:  # 仅在鼠标左键按下时可以拖动
            self.move_flag = True  # 设置一个标记，确保只有在执行 mousePressEvent之后才会执行 mouseMoveEvent
            # 确定两个点（鼠标第一次按下的点，窗口当前所在的原始点）
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()
            # print(self.mouse_x, self.mouse_y)
            self.origen_x = self.x()
            self.origen_y = self.y()

    def mouseMoveEvent(self, evt) -> None:
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


app = QApplication(sys.argv)

# window = QWidget(flags=Qt.FramelessWindowHint)  # (之前面向过程写法保留的一行）设置了无边框的Flag
window = Window()
window.show()

sys.exit(app.exec_())

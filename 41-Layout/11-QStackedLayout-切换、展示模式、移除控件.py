import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # 1. 创建一个布局管理器对象
        sl = QStackedLayout()
        # 2. 把布局对象设置给需要布局的父控件 父布局
        self.setLayout(sl)
        # 3. 通过布局管理器对象，管理布局一些子控件
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color: red;")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color: yellow;")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color: cyan;")

        sl.addWidget(label1)
        sl.addWidget(label2)
        sl.addWidget(label3)

        # ---------切换-----------
        sl.setCurrentIndex(2)
        # timer = QTimer(self)
        # timer.timeout.connect(lambda: sl.setCurrentIndex((sl.currentIndex() + 1) % sl.count()))
        # timer.start(1000)
        #
        # sl.currentChanged.connect(lambda val: print(val))  # 当页面切换时发送currentChanged信号

        # --------展示模式-------
        """
        QStackedLayout.StackOne  只有当前控件可见（默认值）
        QStackedLayout.StackAll  所有小部件可见，当前控件显示在最前
        """
        # sl.setStackingMode(QStackedLayout.StackOne)
        # sl.setStackingMode(QStackedLayout.StackAll)
        # sl.currentWidget().hide()
        # sl.currentWidget().setFixedSize(50, 50)

        # ------移除控件------
        sl.removeWidget(label3)  # 移除控件后自动显示下面的
        sl.widgetRemoved.connect(lambda val: print(val))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

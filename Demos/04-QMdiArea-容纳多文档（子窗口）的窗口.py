import sys

from PyQt5.QtWidgets import *

"""
容纳多文档的窗口
容纳多文档的 QMdiArea
多文档子窗口类 QMdiSubWindow
将QMdiSubWindow添加至QMdiArea中
原帖: https://blog.csdn.net/qq_40243295/article/details/105633221
"""


class MultiDemo(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(MultiDemo, self).__init__(parent)
        self.setWindowTitle("容纳多文档的窗口")
        # 层叠，平铺
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")  # 新创建窗口
        file.addAction("cascade")  # 显示方式，层叠
        file.addAction("Tiled")  # 显示方式,平铺
        file.triggered.connect(self.window_action)

    def window_action(self, q):
        print(q.text())
        if q.text() == "New":
            MultiDemo.count = MultiDemo.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("子窗口" + str(MultiDemo.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text() == "cascade":
            self.mdi.cascadeSubWindows()
        elif q.text() == "Tiled":
            self.mdi.tileSubWindows()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MultiDemo()
    main.show()
    sys.exit(app.exec_())

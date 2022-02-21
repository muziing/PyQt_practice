import sys

from PyQt5.Qt import *

"""
停靠控件，可以把小窗拖入并停靠到主窗口上
原帖: https://blog.csdn.net/qq_40243295/article/details/105633221
"""


class DockDemo(QMainWindow):
    def __init__(self, parent=None):
        """停靠部件QDockWidget"""
        super(DockDemo, self).__init__(parent)
        self.setWindowTitle("停靠控件：QDockWidget")

        self.items = QDockWidget("Dockable", self)
        self.listWidget = QListWidget()
        self.listWidget.addItem("item1")
        self.listWidget.addItem("item2")
        self.listWidget.addItem("item3")

        self.items.setWidget(self.listWidget)
        self.setCentralWidget(QLineEdit())
        self.items.setFloating(True)
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DockDemo()
    main.show()
    sys.exit(app.exec_())

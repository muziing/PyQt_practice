import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox-信号")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        cbb = QComboBox(self)
        cbb.move(100, 100)
        cbb.addItems(["abc", "123"])
        cbb.addItem("字符串", {"name": "muzing"})
        """
        activated(int index)                    某个条目被选中时（必须是用户交互，造成值的改变才会发射）
        activated(QString text)                 某个条目被选中时（必须是用户交互，造成值的改变才会发射）
        currentIndexChanged(int index)          当前选中的索引发生改变时（用户交互、代码控制）
        currentIndexChanged(QString text)       当前选中的索引发生改变时（用户交互、代码控制）
        currentTextChanged(QString text)        当前的文本内容发生改变时
        editTextChanged(QString text)           编辑的文本发生改变时
        highlighted(int index)                  高亮（光标停留在某项上，则获得高亮）
        highlighted(QString text)               高亮
        """

        cbb.activated.connect(lambda val: print("条目被激活", val))
        cbb.activated[str].connect(lambda val: print("条目被激活", val))
        cbb.currentIndexChanged.connect(lambda val: print("当前索引发生改变", val))
        cbb.currentIndexChanged[str].connect(lambda val: print("当前索引发生改变", val))
        cbb.highlighted.connect(lambda val: print("高亮发生改变", val))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

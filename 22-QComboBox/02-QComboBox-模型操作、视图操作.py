import sys
from pprint import pprint

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox-模型操作、视图操作")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        cbb = QComboBox(self)
        cbb.move(100, 100)
        cbb.resize(200, 20)

        # -----模型操作-------
        pprint(QAbstractItemModel.__subclasses__())
        model = QStandardItemModel()

        item_1 = QStandardItem("item_1")
        item_2 = QStandardItem("item_2")
        item_22 = QStandardItem("item_22")
        item_2.appendRow(item_22)
        model.appendRow(item_1)
        model.appendRow(item_2)

        cbb.setModel(model)
        # 此时因为视图还是列表视图，无法显示二级选项

        # -----视图操作---------
        cbb.setView(QTreeView(cbb))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

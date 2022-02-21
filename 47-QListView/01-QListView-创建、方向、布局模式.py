import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListView")
        self.resize(500, 500)
        self.move(400, 250)
        self.data_list = [f"Item{i}" for i in range(40)]  # 将数据列表保存在属性中
        self.setup_ui()

    def setup_ui(self):
        list_view = QListView(self)  # 创建list view对象
        slm = QStringListModel()  # 创建model模型
        slm.setStringList(self.data_list)
        list_view.setModel(slm)  # 为视图设置模型
        list_view.clicked.connect(self.clicked_list)  # 会传出用户点击项的索引

        # -------方向---------
        # list_view.setFlow(QListView.LeftToRight)
        list_view.setFlow(QListView.TopToBottom)

        # ------布局模式（分批列出）-------
        list_view.setBatchSize(5)  # 每批列出的项目个数
        # list_view.setLayoutMode(QListView.Batched)  # 分批列出
        list_view.setLayoutMode(QListView.SinglePass)  # 一次性列出

    def clicked_list(self, model_index):
        # 弹出一个消息提升框，展示用户点击哪个项
        QMessageBox.information(
            self, "QListView", "你选择了: " + self.data_list[model_index.row()]
        )
        print("点击的是：" + str(model_index.row()))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

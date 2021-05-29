from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListView")
        self.resize(500, 500)
        self.move(400, 250)
        self.data_list = ['Item1', 'Item2', 'Item3', 'Item4']  # 将数据列表保存在属性中
        self.setup_ui()

    def setup_ui(self):
        list_view = QListView(self)  # 创建list view对象
        slm = QStringListModel()  # 创建model模型
        slm.setStringList(self.data_list)
        list_view.setModel(slm)  # 为视图设置模型
        list_view.clicked.connect(self.clicked_list)  # 会传出用户点击项的索引

    def clicked_list(self, model_index):
        # 弹出一个消息提升框，展示用户点击哪个项
        QMessageBox.information(self, "QListView", "你选择了: " + self.data_list[model_index.row()])
        print("点击的是：" + str(model_index.row()))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListView-大小调整模式、移动")
        self.resize(500, 500)
        self.data_list = [f"Item{i}" for i in range(15)]  # 将数据列表保存在属性中
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout(self)  # 创建布局管理器
        self.setLayout(layout)
        list_view = QListView()  # 创建list view对象
        list_view.resize(200, 200)
        slm = QStringListModel()  # 创建model模型
        slm.setStringList(self.data_list)  # 为模型设置数据
        list_view.setModel(slm)  # 为视图设置模型
        list_view.setWrapping(True)  # 打开自动换行

        # ---------布局网格-----------
        list_view.setGridSize(QSize(100, 100))  # 此属性设置非空则开启网格布局

        # ---------大小调整模式--------
        # list_view.setResizeMode(QListView.Fixed)  # 项目只会在视图第一次显示时进行布局
        list_view.setResizeMode(QListView.Adjust)  # 每次视图大小改变时，项目都重新布局
        # 可以缩小窗口高度同时保证宽度可以容纳多列来观察效果

        # --------移动模式---------
        # list_view.setMovement(QListView.Static)  # 用户不能移动项目
        # list_view.setMovement(QListView.Free)  # 用户可以自由移动项目
        list_view.setMovement(QListView.Snap)  # 项目在移动时对齐到指定的网格（需要开启网格布局）

        layout.addWidget(list_view, 0, 0)  # 通过布局管理器实现list_view大小随窗口大小改变而变化的效果


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

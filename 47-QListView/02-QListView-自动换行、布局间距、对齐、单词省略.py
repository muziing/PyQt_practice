import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListView-自动换行、布局间距、对齐、单词省略")
        self.resize(500, 500)
        self.data_list = [f"Item{i}" for i in range(15)]  # 将数据列表保存在属性中
        self.data_list.append("Something very very long")  # 再添加一个特殊的很长的项
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton("增大Spacing", self)
        btn.move(350, 200)
        list_view = QListView(self)  # 创建list view对象
        list_view.move(100, 100)
        list_view.resize(200, 200)
        slm = QStringListModel()  # 创建model模型
        slm.setStringList(self.data_list)  # 为模型设置数据
        list_view.setModel(slm)  # 为视图设置模型

        # -------自动换行---------
        list_view.setWrapping(True)  # 打开自动换行
        # 对于 Flow 为 TopToBottom，应该叫做“自动换列”，垂直空间不能一次全部显示所有项时，再右侧再加一列显示，而不是加滚动条

        # -------布局间距--------
        list_view.setSpacing(10)  # 默认为0

        def test_slot():
            """测试按钮的槽函数"""
            list_view.setSpacing(list_view.spacing() + 5)  # 修改此值会导致重新布局

        btn.clicked.connect(test_slot)

        # --------对齐-----------
        # setItemAlignment 只有在 ListMode 为 TopToBottom 且 wrapping 打开时才有效
        # list_view.setItemAlignment(Qt.AlignTop)  # 垂直靠上对齐
        list_view.setItemAlignment(Qt.AlignVCenter | Qt.AlignLeft)  # 垂直居中，水平靠左对齐

        # ------单词省略------
        list_view.setWordWrap(True)  # 启用单词省略，太长的文本将收到省略号...中
        # list_view.setTextElideMode(Qt.ElideLeft)  # 省略号在最左侧
        list_view.setTextElideMode(Qt.ElideMiddle)  # 省略号在中间
        # list_view.setTextElideMode(Qt.ElideNone)  # 无省略号，但是最后的内容仍然会被省略


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

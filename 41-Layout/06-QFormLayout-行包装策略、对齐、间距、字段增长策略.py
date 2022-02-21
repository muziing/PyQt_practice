import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout-行包装策略")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        name_le = QLineEdit()
        age_sb = QSpinBox()
        submit_button = QPushButton("提交")

        # 1.创建布局管理器
        layout = QFormLayout()
        # 2.把布局管理器赋值给需要布局的父控件
        self.setLayout(layout)

        # 3.把需要布局的子控件交给布局管理器进行布局
        layout.addWidget(name_le)

        layout.addRow("姓名（&n）:", name_le)
        layout.addRow("年龄(&g):", age_sb)
        layout.addRow(submit_button)

        # --------行包装策略----------
        layout.setRowWrapPolicy(QFormLayout.DontWrapRows)  # 字段总是放在标签旁边（默认设置）
        # layout.setRowWrapPolicy(QFormLayout.WrapLongRows)
        # 标签被赋予足够的水平空间以适合最宽的标签，其余空间被赋予字段
        # 如果字段的最小大小比可用空间宽，则该字段将换行到下一行
        # layout.setRowWrapPolicy(QFormLayout.WrapAllRows)  # 字段总是位于其标签下方

        # -----------对齐------------
        # 整个表单的对齐，默认为左上
        # layout.setFormAlignment(Qt.AlignLeft | Qt.AlignBottom)  # 下对齐
        layout.setFormAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # 垂直方向居中

        # 标签的对齐
        layout.setLabelAlignment(Qt.AlignRight)

        # ----------间距------------
        layout.setVerticalSpacing(60)
        layout.setHorizontalSpacing(60)

        # -------字段增长策略--------
        layout.setFieldGrowthPolicy(
            QFormLayout.FieldsStayAtSizeHint
        )  # 这些领域永远不会超过其有效大小的提示
        layout.setFieldGrowthPolicy(
            QFormLayout.ExpandingFieldsGrow
        )  # 水平大小策略为Expanding或MinimumExpanding的字符将增长


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

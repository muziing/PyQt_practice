import sys

from PyQt5.Qt import *

"""
修改行
删除行
移除行
标签
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout-行操作")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        name_label = QLabel("姓名：")
        age_label = QLabel("年龄：")
        name_le = QLineEdit()
        age_sb = QSpinBox()

        male_rb = QRadioButton("男")
        female_rb = QRadioButton("女")
        h_layout = QHBoxLayout()
        h_layout.addWidget(male_rb)
        h_layout.addWidget(female_rb)

        layout = QFormLayout()
        self.setLayout(layout)

        layout.setWidget(0, QFormLayout.LabelRole, name_label)  # 设置行，行号、左右位置、设置为
        layout.setWidget(0, QFormLayout.FieldRole, name_le)  # 这种方法只能设置原来空白的单元格，否则无效
        layout.addRow(age_label, age_sb)
        # layout.addRow(name_label)
        # layout.setLayout(0, QFormLayout.LabelRole, h_layout)

        # 移除和删除行
        age_sb.destroyed.connect(lambda: print("年龄步长调节器被释放"))
        age_label.destroyed.connect(lambda: print("年龄label被释放"))
        # layout.removeRow(1)  # 释放
        # layout.removeRow(age_sb)  # 也可以移除一整行
        layout.removeWidget(age_label)  # 只是移除了和布局管理器的父子关系
        age_label.setParent(None)  # 彻底移除了
        # print(layout.takeRow(1).fieldItem)  # 移除但不释放，返回 QFormLayout.TakeRowResult object
        # print(layout.takeRow(1).labelItem)  # 移除但不释放，返回 QFormLayout.TakeRowResult object
        # # 此时会因为一些控件在布局管理器中，一些控件还存在但不在布局管理器中，导致显示混乱，可以通过隐藏后者来解决
        # age_label.hide()
        # age_sb.hide()
        # print(dir(QFormLayout.TakeRowResult))

        print(layout.labelForField(name_le))  # 提取标签
        # layout.labelForField(name_le).setText('XXX')  # 可以用提取出的标签直接修改对象


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

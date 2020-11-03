from PyQt5.Qt import *
import sys


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

        male_rb = QRadioButton('男')
        female_rb = QRadioButton('女')
        h_layout = QHBoxLayout()
        h_layout.addWidget(male_rb)
        h_layout.addWidget(female_rb)

        layout = QFormLayout()
        self.setLayout(layout)

        layout.setWidget(0, QFormLayout.LabelRole, name_label)  # 设置行，行号、左右位置、设置为
        layout.setWidget(0, QFormLayout.FieldRole, name_le)  # 这种方法只能设置原来空白的单元格，否则无效
        # layout.addRow(name_label)
        # layout.setLayout(0, QFormLayout.LabelRole, h_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

from PyQt5.Qt import *
import sys

"""
编辑日期和时间的单行文本框
既可以用剪头调节，也可以用键盘编辑输入
可以单独调节某个部分
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDateTimeEdit")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # -------创建---------
        # dte = QDateTimeEdit(self)  # 当不传入日期时间时，显示默认日期时间
        dte = QDateTimeEdit(QDateTime.currentDateTime(), self)  # 同时初始化了控件展示的section
        # dte = QDateTimeEdit(QDate.currentDate(), self)
        # dte = QDateTimeEdit(QTime.currentTime(), self)
        dte.move(100, 100)

        btn = QPushButton("测试按钮", self)
        btn.move(100, 200)
        # btn.clicked.connect()

        # ------section操作-------
        print(dte.sectionCount())  # 返回section个数
        print(dte.currentSectionIndex())
        dte.setCurrentSection(QDateTimeEdit.SecondSection)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

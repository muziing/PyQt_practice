from PyQt5.Qt import *
import sys

"""
编辑日期和时间的单行文本框
既可以用箭头调节，也可以用键盘编辑输入
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
        # ----------创建-----------
        # dte = QDateTimeEdit(self)  # 使用默认日期时间显示
        dte = QDateTimeEdit(QDateTime.currentDateTime(), self)  # 显示当前日期时间
        # dte = QDateTimeEdit(QDate.currentDate(), self)  # 当前日期，并把section初始化为只有日期
        # dte = QDateTimeEdit(QTime.currentTime(), self)  # 当前时间，并把section初始化为只有时间
        dte.move(100, 100)

        # --------显示格式------------
        dte.setDisplayFormat("yyyy.MM.dd hh:mm:ss.zzz")
        # dte.setDisplayFormat("yy")  # 当年份只取两位时，默认对应21世纪，比如2021年就显示21
        print(dte.displayFormat())  # 返回显示日期时间的格式字符串

        # --------section操作--------
        print(dte.sectionCount())  # 获取section数


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

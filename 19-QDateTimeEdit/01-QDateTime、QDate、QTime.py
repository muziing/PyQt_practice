import sys
import time

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDateTime")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # QDateTime QDate QTime 这三个类之间没有继承关系

        # QDateTime
        # -------------创建----------------
        # dt = QDateTime()
        # dt = QDateTime(2021, 5, 8, 12, 30)  # 创建时设置年、月、日、时、分
        dt = QDateTime.currentDateTime()  # 静态方法，获取当前时间
        # dt = QDateTime.currentDateTimeUtc()  # 静态方法，获取当前的UTC时间
        print("dt:", dt)

        # -------------调整日期时间------------
        dt_add_year = dt.addYears(1)  # 增加1年，返回一个新的QDateTime对象
        print("dt_add_year:", dt_add_year)
        print("dt_add_secs", dt.addSecs(600))  # 增加小时或分钟没有专门的函数，需要通过增加秒来设置
        dt.setTime(QTime(12, 5, 31, 0))  # 设置时间

        # -----------计算时间差-----------
        print(
            "offset from UTC", QDateTime.offsetFromUtc(QDateTime.currentDateTime())
        )  # 本地时间与UTC时间之差（单位为s）
        print(dt.secsTo(QDateTime.currentDateTime()))  # 计算两个时间之差，单位s

        # ----------展示时间-------
        dte = QDateTimeEdit(dt, self)  # 方便查看起见，展示一下dt的信息
        dte.move(100, 100)

        # QDate
        # ---------构造----------
        # qd = QDate(2020, 1, 1)  # 构造时传入年月日信息
        qd = QDate.currentDate()
        print(QDate.currentDate())  # 获取当前日期

        # --------调整日期------
        # 类似QDateTime

        # ---------计算时间差-----
        print("dates to 2001.1.1:", QDate(2001, 1, 1).daysTo(qd))

        # ---------获取时间--------
        print("day of week", qd.dayOfWeek())  # 这一周的第几日
        print("day of year", qd.dayOfYear())  # 这一年的第几日
        print("days in month", qd.daysInMonth())  # 这一月总共多少天
        print("days in year", qd.daysInYear())  # 这一年总共多少天

        # QTime
        # --------构造--------
        # my_time = QTime(12, 00)
        my_time = QTime.currentTime()

        # -------调整时间-------
        # 类似QDAteTime

        # --------计算时间差------
        print("secs to:", my_time.secsTo(QTime(12, 0)))

        # -------计时----------
        my_time.start()  # 开始计时
        time.sleep(1)
        print(my_time.elapsed())  # 从开始计时到执行此函数中间所用时间，单位ms


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

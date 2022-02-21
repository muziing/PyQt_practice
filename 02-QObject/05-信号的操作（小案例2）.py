import sys

from PyQt5.Qt import *

# 要求： 每次改变窗口标题，都自动加上muzing前缀，能重复使用
app = QApplication(sys.argv)

window = QWidget()


# 连接窗口标题变化的 信号 与 槽


def cao(title):
    # print('窗口标题变成了：', title)
    window.blockSignals(True)  # 避免出现死循环
    window.setWindowTitle("muzing " + title)
    window.blockSignals(False)  # 恢复连接，使下一次还能进行修改


window.windowTitleChanged.connect(cao)

window.setWindowTitle("信号的操作案例")
window.setWindowTitle("修改后的标题")
window.resize(500, 500)
window.move(400, 250)

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

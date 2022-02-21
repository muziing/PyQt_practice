import sys

from PyQt5.Qt import *

"""案例要求：将20个大小相同的子控件以3列均匀填满窗口"""
app = QApplication(sys.argv)

window = QWidget()
window.show()
window.resize(500, 500)

# 总的控件个数
widget_count = 20
# 一行有多少列
column_count = 3
# 计算一个控件的宽度
widget_width = int(window.width() / column_count)
# 总共多少行 （编号 // 列数 + 1）
row_count = (widget_count - 1) // column_count + 1
widget_height = int(window.height() / row_count)

for i in range(0, widget_count):
    w = QWidget(window)
    w.resize(widget_width, widget_height)
    widget_x = i % column_count * widget_width
    widget_y = i // column_count * widget_height
    w.move(widget_x, widget_y)
    w.setStyleSheet("background-color: green; border: 3px solid cyan;")
    w.show()

sys.exit(app.exec_())

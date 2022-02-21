import sys

from PyQt5.Qt import *

"""
QWidget
1.所有可视控件的基类
2.是一个最简单的空白控件
3.控件是用户界面的最小元素
4.每个控件都是矩形的，它们按Z轴顺序排序
5.控件由其父控件和前面的控件裁剪
6.没有父控件的控件，称之为窗口
"""

app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 500)

red = QWidget(window)
red.resize(100, 100)
red.setStyleSheet("background-color: red;")
red.move(300, 0)

green = QWidget(window)
green.resize(100, 100)
green.setStyleSheet("background-color: green;")
green.move(300, 50)  # 体现QWidget沿z轴绘制，后面的控件可以覆盖前面的控件

window.show()
# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

import sys

from PyQt5.Qt import *


class Window(QWidget):
    def mousePressEvent(self, evt) -> None:
        # print(self.focusWidget())
        # self.focusNextChild()  # 焦点切换到下一个子控件
        # self.focusPreviousChild()  # 焦点切换到上一个子控件
        pass


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = Window()
# 2.2设置控件

window.setWindowTitle("焦点控制")
window.resize(500, 500)
window.move(400, 250)

le1 = QLineEdit(window)
le1.move(50, 50)

le2 = QLineEdit(window)
le2.move(50, 100)

le3 = QLineEdit(window)
le3.move(50, 150)

# 是个静态方法，设置了子控件获取焦点的先后顺序
QWidget.setTabOrder(le1, le3)
QWidget.setTabOrder(le3, le2)

# le2.setFocus()  # 设置获得焦点
# le2.clearFocus()  # 清空获得的焦点
# le2.setFocusPolicy(Qt.TabFocus)  # 设置获取焦点策略为仅通过Tab键获取
# le2.setFocusPolicy(Qt.ClickFocus)  # 设置获取焦点策略为仅通过鼠标点击获取
le2.setFocusPolicy(Qt.StrongFocus)  # 设置获取焦点策略为鼠标点击、Tab两种方式，也是默认值
# le2.setFocusPolicy(Qt.NoFocus)  # 设置不能通过两种方式获得焦点

# 2.3展示控件
window.show()
# 获取当前窗口内部，所有子控件当中获取焦点的那个控件
print(window.focusWidget())
# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

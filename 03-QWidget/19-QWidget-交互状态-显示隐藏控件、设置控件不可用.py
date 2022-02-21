import sys

from PyQt5.Qt import *


class Window(QWidget):
    def paintEvent(self, evt):
        print("窗口被绘制了")
        return super().paintEvent(evt)


class Btn(QPushButton):
    def paintEvent(self, evt):
        print("按钮被绘制了")
        return super().paintEvent(evt)


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = Window()
# 2.2设置控件

window.setWindowTitle("交互状态")
window.resize(500, 500)
window.move(400, 250)

btn = Btn(window)
btn.setText("按钮")
# btn.pressed.connect(lambda: print("按钮被点击了"))
btn.pressed.connect(lambda: btn.setVisible(False))  # 按钮功能：使自己不可见
# btn.setEnabled(False)  # 使按钮不可用
# btn.setVisible(False)  # 使按钮不可见

# 2.3展示控件
window.show()
# window.setVisible(True)  # show()等方法都是setVisible方法的马甲
# window.setHidden(False)

print(btn.isHidden())  # 当 window没有被绘制时，也是 False
print(btn.isVisible())
print(btn.isVisibleTo(window))  # 父控件如果被显示时，子控件是否跟着被显示

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

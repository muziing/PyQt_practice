from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QAbstractButton-模拟点击")
window.resize(500, 500)
window.move(400, 250)

btn = QPushButton(window)
btn.setText("这是按钮1")
btn.pressed.connect(lambda: print("按钮1被点击了"))

# btn.click()  # 模拟用户点击，不带动画
btn.animateClick(1000)  # 模拟持续按下 1000 ms 后再松开，带动画

btn2 = QPushButton(window)
btn2.setText("按钮2")
btn2.move(50, 100)


def test():
    # btn.click()
    btn.animateClick(500)  # 动画点击


btn2.pressed.connect(test)

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

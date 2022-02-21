import sys

from PyQt5.Qt import *

if __name__ == "__main__":
    app = QApplication(sys.argv)

    win1 = QWidget()
    win1.setStyleSheet("background-color: red;")
    win1.setWindowTitle("这是win1")
    win1.resize(500, 500)
    win1.show()

    win2 = QWidget()
    win2.setStyleSheet("background-color: green;")
    win2.resize(1000, 100)
    # 子控件显示受父控件约束
    # 生命周期也被父对象接管
    win2.setParent(win1)
    win2.show()

    win3 = QWidget()
    win3.resize(500, 500)
    win3.move(800, 0)
    win3.setWindowTitle("这是win3")

    label1 = QLabel(win3)
    label1.setText("这是label1")
    label2 = QLabel(win3)
    label2.setText("这是label2")
    label2.move(100, 0)
    btn1 = QPushButton(win3)
    btn1.setText("btn1")
    btn1.move(0, 50)

    for sub_widget in win3.findChildren(QLabel):  # 只筛选Win3下面QLabel类型的子控件
        print(sub_widget)
        sub_widget.setStyleSheet("background-color: cyan;")
    win3.show()
    sys.exit(app.exec_())

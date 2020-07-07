import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QDesktopWidget, QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon


class QuitApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        #设置主窗口的标题
        self.setWindowTitle('退出')
        #设置窗口的尺寸
        self.resize(400, 300)
        # 添加 Button
        self.button1 = QPushButton('退出应用程序')
        # 将信号与槽关联
        self.button1.clicked.connect(lambda: self.onClick_Button())
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    # 按钮单击事件的方法
    def onClick_Button(self):
        sender = self.sender()
        print((sender.text() + '按钮被按下'))
        app = QApplication.instance()
        # 退出应用程序
        app.quit()

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newleft = int((screen.width() - size.width()) / 2)
        newtop = int((screen.height() - size.height()) / 2)
        self.move(newleft, newtop)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('./snowflake.ico'))
    main = QuitApplication()
    main.center()
    main.show()

    sys.exit(app.exec_())

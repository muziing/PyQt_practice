import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QDesktopWidget, QMenu,
                             QMessageBox, QSystemTrayIcon, QWidget, qApp)


class SystemTray:
    # 程序托盘类
    def __init__(self, w):
        self.app = app
        self.w = w
        # 禁止默认的closed方法，只能使用qapp.quit()的方法退出程序
        QApplication.setQuitOnLastWindowClosed(False)
        self.w.show()  # 不设置显示则为启动最小化到托盘
        self.tp = QSystemTrayIcon(self.w)
        self.initUI()
        self.run()

    def initUI(self):
        # 设置托盘图标

        self.tp.setIcon(QIcon("../Icons/python_96px.ico"))

    def quitApp(self):
        # 退出程序
        self.w.show()  # w.hide() #设置退出时是否显示主窗口
        re = QMessageBox.question(
            self.w, "提示", "退出系统", QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if re == QMessageBox.Yes:
            self.tp.setVisible(False)  # 隐藏托盘控件，托盘图标刷新不及时，提前隐藏
            qApp.quit()  # 退出程序

    def message(self):
        # 提示信息被点击方法
        print("弹出的信息被点击了")

    def act(self, reason):
        # 主界面显示方法
        # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
        if reason == 2 or reason == 3:
            self.w.show()

    def run(self):

        a1 = QAction("&显示(Show)", triggered=self.w.show)
        a2 = QAction("&退出(Exit)", triggered=self.quitApp)

        tpMenu = QMenu()
        tpMenu.addAction(a1)
        tpMenu.addAction(a2)
        self.tp.setContextMenu(tpMenu)
        self.tp.show()  # 不调用show不会显示系统托盘消息，图标隐藏无法调用

        # 信息提示
        # 参数1：标题
        # 参数2：内容
        # 参数3：图标（0没有图标 1信息图标 2警告图标 3错误图标），0还是有一个小图标
        self.tp.showMessage("Hello", "我藏好了", icon=0)
        # 绑定提醒信息点击事件
        self.tp.messageClicked.connect(self.message)
        # 绑定托盘菜单点击事件
        self.tp.activated.connect(self.act)
        sys.exit(self.app.exec_())  # 持续对app的连接


class Window(QWidget):
    # 主窗口类
    def __init__(self):
        # move()方法移动了窗口到屏幕坐标x=300, y=300的位置.
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        # 主窗口布局实现略。。。
        self.setWindowTitle("Test")  # 设置标题
        self.setWindowIcon(QIcon("../Icons/python_96px.ico"))  # 设置标题图标
        self.resize(300, 250)  # 设置窗体大小
        self.setFixedSize(self.width(), self.height())  # 固定窗口大小
        self.center()  # 窗体屏幕居中显示
        self.tray()  # 程序实现托盘

    def tray(self):
        # 创建托盘程序
        ti = SystemTray(self)

    def center(self):
        # 窗口居中方法
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    # 创建一个app程序
    app = QApplication(sys.argv)
    # 创建窗口
    win = Window()
    sys.exit(app.exec_())

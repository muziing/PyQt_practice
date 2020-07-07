import sys
import test
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = test.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # 显示窗口
    MainWindow.show()
    # 进入程序主循环、并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())

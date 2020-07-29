from PyQt5.Qt import *
import sys
# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("菜单和弹出模式")
window.resize(500, 500)
window.move(400, 250)


tb = QToolButton(window)
tb.setText("工具")

menu = QMenu(tb)
sub_menu = QMenu(tb)
sub_menu.setTitle("子菜单")
sub_menu.setIcon(QIcon('../Icons/plus_48px.ico'))
action = QAction(QIcon('../Icons/cross_48px.ico'), "关闭", menu)
action.triggered.connect(lambda: exit())

menu.addMenu(sub_menu)
menu.addSeparator()
menu.addAction(action)
tb.setMenu(menu)

tb.clicked.connect(lambda: print("工具按钮被点击了"))

# tb.setPopupMode(QToolButton.DelayedPopup)  # 设置菜单弹出方式 这是默认模式 长按按钮弹出
tb.setPopupMode(QToolButton.MenuButtonPopup)  # 点击后弹出（有分隔）
# tb.setPopupMode(QToolButton.InstantPopup)  # 点击后弹出（无分隔）


# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

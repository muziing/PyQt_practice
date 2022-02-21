import sys

from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QToolButton-可用信号")
window.resize(500, 500)
window.move(400, 250)

tb = QToolButton(window)
tb.setText("工具")

menu = QMenu(tb)
sub_menu = QMenu(tb)
sub_menu.setTitle("子菜单")
sub_menu.setIcon(QIcon("../Icons/plus_48px.ico"))
action1 = QAction(QIcon("../Icons/menu_48px.ico"), "行为", menu)
action1.setData([1, 2, 3])
# action1.triggered.connect(lambda: print("行为本身发射的信号"))
action2 = QAction(QIcon("../Icons/image_48px.ico"), "行为2", menu)
action2.setData({"key": "value"})

menu.addMenu(sub_menu)
menu.addSeparator()
menu.addAction(action1)
menu.addAction(action2)
tb.setMenu(menu)
tb.setPopupMode(QToolButton.MenuButtonPopup)


def do_action(act):
    print("tb发射的信号", act.data())


tb.triggered.connect(do_action)
window.show()

sys.exit(app.exec_())

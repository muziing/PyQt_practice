from PyQt5.Qt import *
import sys
# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QToolButton箭头")
window.resize(500, 500)
window.move(400, 250)

tb = QToolButton(window)
tb.setText("这是一个QToolButton")
# 注意：即使设置了文字和图标，也不一定显示
tb.setIcon(QIcon('../Icons/search_48px.ico'))
tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
# tb.setArrowType(Qt.NoArrow)
# tb.setArrowType(Qt.UpArrow)  # 向上的箭头
# tb.setArrowType(Qt.DownArrow)
# tb.setArrowType(Qt.LeftArrow)
tb.setArrowType(Qt.RightArrow)

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

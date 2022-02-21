import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("交互状态-关闭")
window.resize(500, 500)
window.move(400, 250)

btn = QPushButton(window)
btn.setText("按钮")
btn.destroyed.connect(lambda: print("按钮被释放了"))
# btn.setVisible(False)
# btn.setHidden(True)
# btn.hide()
# btn.deleteLater()
btn.setAttribute(Qt.WA_DeleteOnClose, True)  # 关闭时释放对象
btn.close()
# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

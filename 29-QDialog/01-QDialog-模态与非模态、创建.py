import sys

from PyQt5.Qt import *

"""
对话窗口的基类
对话窗口是顶级窗口，主要用于短期任务和与用户的简短通信
QDialog可能是模态的或非模态对话框：
"""

"""
模态对话框：
分类：应用程序级别与窗口级别

应用程序级别：
默认值
当该种模态的对话框出现时，用户必须首先对对话框进行交互，直到关闭对话框，然后
exec()

窗口级别：
该模态仅仅阻塞与对话框关联的窗口，但是依然允许用户与程序中其他窗口交互
open()

应用场景：文件选择、是否同意……
"""

"""
非模态对话框：
不会阻塞与对话框关联的窗口以及与其他窗口进行交互

show()
结合 setModal(True)也可以实现模态对话框
结合setWindowModality(Qt.WindowModal)也可以实现模态对话框 Qt.WindowModal Qt.ApplicationModal

应用场景：查找替换
"""

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QDialog")
window.resize(500, 500)
window.move(400, 250)

d = QDialog(window)
d.setWindowTitle("对话框")
# d.setModal(True)  # 设置为窗口级模态
d.setWindowModality(Qt.WindowModal)  # 设置为窗口级别模态
# d.setWindowModality(Qt.ApplicationModal)  # 设置为应用程序级别模态
# d.exec()  # 应用程序级的模态
# d.open()  # 窗口级的模态
d.show()  # 非模态

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

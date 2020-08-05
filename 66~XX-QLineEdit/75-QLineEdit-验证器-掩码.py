from PyQt5.Qt import *
import sys
"""
要求：
总共输入5位  左边2（必须是大写字母） - 右边2（必须是数字）"""
# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QlineEdit-验证器-掩码")
window.resize(500, 500)
window.move(400, 250)

le_a = QLineEdit(window)
le_a.move(100, 100)
le_a.setInputMask('>AA-99')  # 掩码 ';' 后面的字符为占位符
# le_a.setInputMask('>AA-99;#')  # 掩码 ';' 后面的字符为占位符

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

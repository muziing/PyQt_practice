import sys

from PyQt5.Qt import *

"""
要求：
总共输入5位  左边2（必须是大写字母） - 右边2（必须是数字）
"""

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QLineEdit-验证器-掩码")
window.resize(500, 500)
window.move(400, 250)

le_a = QLineEdit(window)
le_a.move(100, 100)
le_a.setInputMask(">AA-99")  # 掩码 ';' 后面的字符为占位符
# le_a.setInputMask('>AA-99;#')  # 掩码 ';' 后面的字符为占位符

window.show()

sys.exit(app.exec_())

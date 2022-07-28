import sys

from PyQt5.Qt import *

"""
掩码是另一种更为严格的输入验证方式，用户输入的每一位都必须严格
符合掩码设置的要求

掩码详情见：https://doc.qt.io/qt-5/qlineedit.html#inputMask-prop

案例：
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

import sys

from PyQt5.Qt import *

"""
单行文本编辑器可以设置验证器（Validator），比如限制只能输入一定范围内的数字等，设置验证器后，
只有满足验证器要求的字符才能被输入，否则用户输入不会显示在编辑器内

案例：设置一个年龄验证器，限制用户只能输入18～180之间的数字
"""

# 通过继承重写QValidator，创建一个自定义的验证器类
class AgeValidator(QValidator):
    def validate(self, input_str: str, pos_int: int):
        print(input_str, pos_int)
        try:
            if 18 < int(input_str) <= 180:
                return QValidator.Acceptable, input_str, pos_int
            elif 1 <= int(input_str) <= 17:
                return QValidator.Intermediate, input_str, pos_int
            else:
                return QValidator.Invalid, input_str, pos_int
        except Exception:
            # 如果用户还没有输入，输入字符为空
            if not input_str:
                return QValidator.Intermediate, input_str, pos_int
            return QValidator.Invalid, input_str, pos_int

    # 如果用户输入不满足要求，最后还会调用fixup方法修复
    def fixup(self, p_str: str) -> str:
        try:
            if int(p_str) < 18:  # 若用户最终输入小于18,则返回18
                return "18"
            return "180"  # 否则返回180
        except Exception:
            return "18"


# 通过继承重写QIntValidator，更简单地实现年龄验证器
class MyAgeValidator(QIntValidator):
    def fixup(self, input: str) -> str:
        if len(input) == 0 or int(input) < 18:
            return "18"
        elif int(input) > 180:
            return "180"
        return input


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit-验证器的使用")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):

        le = QLineEdit(self)
        le.move(100, 100)

        # 验证器举例：数字 18-180
        # 创建验证器实例
        # validator = AgeValidator(le)
        validator = MyAgeValidator(18, 180, le)
        # 为le设置验证器
        le.setValidator(validator)

        # 对照没有设置验证器的line edit观察效果
        le2 = QLineEdit(self)
        le2.move(100, 150)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

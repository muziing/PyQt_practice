import sys

from PyQt5.Qt import *


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
            if len(input_str) == 0:
                return QValidator.Intermediate, input_str, pos_int
            return QValidator.Invalid, input_str, pos_int

    def fixup(self, p_str: str) -> str:
        try:
            if int(p_str) < 18:
                return "18"
            return "180"
        except Exception:
            return "18"


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
        # validator = AgeValidator(le)
        validator = MyAgeValidator(18, 180, le)
        le.setValidator(validator)

        le2 = QLineEdit(self)
        le2.move(100, 150)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

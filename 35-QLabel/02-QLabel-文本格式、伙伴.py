import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel("<h1>muzing</h1>", self)
        label.move(150, 155)

        # ---------文本格式-------------
        label.setTextFormat(Qt.PlainText)  # 纯文本
        # label.setTextFormat(Qt.RichText)  # 富文本
        # label.setTextFormat(Qt.AutoText)  # 自动识别是否富文本（默认值）

        # -----------伙伴---------------
        le_1 = QLineEdit(self)
        le_1.move(250, 150)
        le_2 = QLineEdit(self)
        le_2.move(250, 200)

        label.setText("账号(&S)")
        label.setBuddy(le_1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

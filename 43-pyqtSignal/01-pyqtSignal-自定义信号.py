import sys

from PyQt5.Qt import *


class Btn(QPushButton):
    # someSignal = pyqtSignal(int, str)  # 如果期望信号发射时携带信息，直接在定义时写明信息的数据类型
    rightClicked = pyqtSignal()  # 定义信号一定是类属性，不能是实例属性（在def方法里面写的属性是示例属性）

    def mousePressEvent(self, e) -> None:
        super().mousePressEvent(e)
        if e.button() == Qt.RightButton:  # 当按下的键是鼠标右键时
            self.rightClicked.emit()  # 发送信号


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        btn = Btn("测试按钮", self)
        btn.move(100, 100)

        btn.clicked.connect(lambda: print("按钮被点击了"))
        btn.rightClicked.connect(lambda: print("按钮被鼠标右键点击击了"))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

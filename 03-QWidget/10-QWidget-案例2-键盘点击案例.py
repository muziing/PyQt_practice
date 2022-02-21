import sys

from PyQt5.Qt import *


class MyLabel(QLabel):
    def keyPressEvent(self, evt):
        if evt.key() == Qt.Key_Tab:
            self.setText("Tab键被点击了")
        # 注意Ctrl、Alt等修饰键的写法
        if evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_S:
            self.setText("Ctrl + S 被点击了")
        # 多个修饰键之间用按位或来连接
        if (
            evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier
            and evt.key() == Qt.Key_S
        ):
            self.setText("Ctrl + Shift + S 被点击了")


app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QWidget案例2")
window.resize(500, 500)
window.move(400, 250)

label = MyLabel(window)
label.resize(200, 200)
label.move(140, 120)
label.setStyleSheet("background-color: cyan;")
label.grabKeyboard()

window.show()

sys.exit(app.exec_())

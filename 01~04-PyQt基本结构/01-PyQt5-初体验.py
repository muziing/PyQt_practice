from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("社会我顺哥，人狠话不多")
window.resize(500, 500)
window.move(400, 250)

label = QLabel(window)
label.setText("Hello world")
label.move(200, 240)

window.show()

sys.exit(app.exec_())

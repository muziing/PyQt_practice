from PyQt5.Qt import *
import sys


""" QMessageBox.StandardButton
QMessageBox.Ok 使用AcceptRole定义的“确定”按钮
QMessageBox.Open 使用AcceptRole定义的“打开”按钮
QMessageBox.Save 使用AcceptRole定义的“保存”按钮
QMessageBox.Cancel 使用AcceptRole定义的“取消”按钮
QMessageBox.Close 使用AcceptRole定义的“关闭”按钮
QMessageBox.Discard “丢弃”或“不保存”按钮，具体取决于使用DestructiveRole定义的平台
QMessageBox.Apply 使用ApplyRole定义的“应用”按钮
QMessageBox.Reset 使用ResetRole定义的“重置”按钮
QMessageBox.RestoreDefaults 使用ResetRole定义的“恢复默认值”按钮
QMessageBox.Help 使用HelpRole定义的“帮助”按钮
QMessageBox.SaveAll 使用AcceptRole定义的“全部保存”按钮
QMessageBox.Yes 使用YesRole定义的“是”按钮
QMessageBox.YesToAll 使用YesRole定义的“Yes to All” 按钮

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # mb = QMessageBox(self)
        mb = QMessageBox(QMessageBox.Critical, '窗口标题', '主标题', QMessageBox.Ok | QMessageBox.Discard, self)
        # mb.setModal(False)  # 强行设置为非模态
        # mb.setWindowModality(Qt.NonModal)  # 强行设置为非模态
        # mb.show()  # 一定为模态，即使使用show()方法也仍为模态
        mb.open()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()
    
    sys.exit(app.exec_())

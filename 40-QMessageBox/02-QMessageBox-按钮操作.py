import sys

from PyQt5.Qt import *

"""
QMessageBox.ButtonRole
QMessageBox.InvalidRole  该按钮无效
QMessageBox.AcceptRole  单击该按钮将使对话框被接受（例如，确定）
QMessageBox.RejectRole  单击该按钮会导致拒绝对话框（例如取消）
QMessageBox.DestructiveRole  单击该按钮会导致破坏性更改（例如，对于 Discarding Change
QMessageBox.ActionRole  单击该按钮将导致更改对话框中的元素
QMessageBox.HelpRole  可以单击该按钮以请求帮助
QMessageBox.YesRole  按钮是一个“是”按钮
QMessageBox.NoRole  按钮是一个“否”按钮
QMessageBox.ApplyRole  该按钮应用当前更改
QMessageBox.ResetRole  该按钮将对话框的字段重置为默认值
"""

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
QMessageBox.No  使用NoRole定义的“否”按钮
QMessageBox.NoToAll  使用NoRole定义的“No to All”按钮
QMessageBox.Abort  使用RejectRole定义的”中止“按钮
QMessageBox.Retry  使用AcceptRole定义的”重试“按钮
QMessageBox.Ignore  使用AcceptRole定义的”忽略“按钮
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox-按钮操作")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        mb = QMessageBox(self)
        mb.setWindowTitle("消息提示")

        # 添加移除按钮
        # mb.addButton(QPushButton("Yes!Yes!Yes!", mb), QMessageBox.YesRole)
        yes_btn = mb.addButton("Yes!Yes!Yes!", QMessageBox.YesRole)
        # mb.removeButton(yes_btn)  # 移除按钮

        # 设置标准按钮
        mb.setStandardButtons(QMessageBox.Apply | QMessageBox.No)

        # 默认按钮(默认哪个按钮获取到焦点）
        mb.setDefaultButton(QMessageBox.Apply)

        # 退出按钮（按下键盘Esc键时激活的按钮）
        mb.setEscapeButton(QMessageBox.No)

        # 按钮信号槽
        apply_btn = mb.button(QMessageBox.Apply)  # 获取按钮对象

        def test(btn):
            if btn == yes_btn:
                print("点击了yes按钮")
            elif btn == apply_btn:
                print("点击了apply按钮")

            role = mb.buttonRole(btn)
            if role == QMessageBox.YesRole:
                print("点击了Yes按钮")
            elif role == QMessageBox.NoRole:
                print("点击了No按钮")

        mb.buttonClicked.connect(test)

        mb.open()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

import sys

from PyQt5.Qt import *


class AccountTool:
    ACCOUNT_ERROR = 0
    PWD_ERROR = 1
    SUCCESS = 2

    @staticmethod  # 设置为静态方法
    def check_login(account, pwd):
        # 把账号密码发送给服务器，等待服务器返回结果
        if account != "muzing":
            return AccountTool.ACCOUNT_ERROR
        if pwd != "123456":
            return AccountTool.PWD_ERROR
        return AccountTool.SUCCESS


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("登录案例")
        self.resize(500, 500)
        self.setMinimumSize(400, 400)
        # self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # 添加三个控件
        self.account_le = QLineEdit(self)
        self.account_le.setPlaceholderText("请输入账号")
        self.pwd_le = QLineEdit(self)
        self.pwd_le.setPlaceholderText("请输入密码")
        self.pwd_le.setEchoMode(QLineEdit.Password)
        self.login_btn = QPushButton("登   录", self)
        self.login_btn.clicked.connect(self.login_cao)

    def login_cao(self):
        account = self.account_le.text()
        pwd = self.pwd_le.text()

        state = AccountTool.check_login(account, pwd)

        if state == AccountTool.ACCOUNT_ERROR:
            print("账号错误")
            self.account_le.setText("")
            self.pwd_le.setText("")
            self.account_le.setFocus()
            return None
        if state == AccountTool.PWD_ERROR:
            print("密码错误")
            self.pwd_le.setText("")
            self.pwd_le.setFocus()  # 让密码输入框获得焦点
            return None
        if state == AccountTool.SUCCESS:
            print("登录成功")

        # 优化前的代码
        # if account == "muzing":
        #     if pwd == "123456":
        #         print("登录成功")
        #     else:
        #         print("密码错误")
        #         self.pwd_le.setText('')
        #         self.pwd_le.setFocus()  # 让密码输入框获得焦点
        # else:
        #     print("账号错误")
        #     self.account_le.setText('')
        #     self.pwd_le.setText('')
        #     self.account_le.setFocus()

    def resizeEvent(self, evt) -> None:
        widget_w = 180
        widget_h = 38
        margin = 40

        self.account_le.resize(widget_w, widget_h)
        self.pwd_le.resize(widget_w, widget_h)
        self.login_btn.resize(widget_w, widget_h)

        x = int((self.width() - widget_w) / 2)
        self.account_le.move(x, int(self.height() / 5))
        self.pwd_le.move(x, self.account_le.y() + self.account_le.height() + margin)
        self.login_btn.move(x, self.pwd_le.y() + self.pwd_le.height() + margin)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

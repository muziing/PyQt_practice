import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit-插入表格")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        te = QTextEdit(self)
        self.te = te
        te.setText("abc")
        test_btn = QPushButton("测试按钮", self)
        test_btn.move(350, 140)
        test_btn.clicked.connect(self.test_btn_cao)

    def test_btn_cao(self):
        self.cursor_insert_table()

    def cursor_insert_table(self):
        tc = self.te.textCursor()  # 创建光标对象
        ttf = QTextTableFormat()
        ttf.setAlignment(Qt.AlignRight)  # 右对齐
        ttf.setCellPadding(6)  # 内边距
        ttf.setCellSpacing(3)  # 外边距
        ttf.setColumnWidthConstraints(
            (
                QTextLength(QTextLength.PercentageLength, 50),
                QTextLength(QTextLength.PercentageLength, 40),
                QTextLength(QTextLength.PercentageLength, 10),
            )
        )  # 设置列宽约束，百分比约束
        table = tc.insertTable(5, 3, ttf)  # 返回QTextTable
        # table.appendColumns(2)  # 对表格进行追加2列


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

import sys

from PyQt5.Qt import *

"""
适用于段落和字符：
段落是一个格式化的字符串，为了适应控件的宽度，会自动换行
默认情况下，在读取纯文本时，一个换行符表示一个段落
文档由零个或多个段落组成。段落由硬线断开分隔
段落中的每个字符都有自己的属性，例如字体和颜色

内容的编辑：
文本的选择由QTextCursor类处理，该类提供创建选择检索文本内容删除选择的功能
QPlainTextEdit包含一个QTextDocument对象，可以使用document()方法检索该对象

与QTextEdit功能相似，但针对纯文本处理进行了优化，差异：
QPlainTextEdit是一个简略版的类，使用QTextEdit和QTextDocument作为背后实现的技术支撑
性能优于QTextEdit，主要是因为在文本文档中使用QPlainTextDocumentLayout简化文本布局
纯文本文档布局不支持表格或嵌入框架，并使用逐行滚动的方式替换像素精确高度计算
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainTextEdit")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        pte = QPlainTextEdit(self)
        self.pte = pte
        pte.resize(300, 300)
        pte.move(100, 100)
        self.占位提示文本()
        # self.只读设置()
        self.格式设置()

    def 占位提示文本(self):
        self.pte.setPlaceholderText("请输入信息")
        print(self.pte.placeholderText())

    def 只读设置(self):
        self.pte.setReadOnly(True)
        print(self.pte.isReadOnly())

    def 格式设置(self):
        tcf = QTextCharFormat()
        tcf.setFontUnderline(True)
        tcf.setUnderlineColor(QColor(0, 128, 128))
        self.pte.setCurrentCharFormat(tcf)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

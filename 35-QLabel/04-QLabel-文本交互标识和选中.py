import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel-文本交互标识和选中")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.move(100, 100)
        label.setText("muzing的个人博客链接为 <a href=https://muzing.top>https://muzing.top")
        label.setTextFormat(Qt.RichText)
        label.setOpenExternalLinks(True)
        # 可以使用鼠标选择文本并使用上下文菜单或标准键盘快捷键将其复制到剪切板
        # label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # 可以使用键盘上的光标键选择文本，显示文本光标
        # label.setTextInteractionFlags(Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse)

        # 可以使用鼠标突出显示和激活链接
        label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        # 可以使用选项卡聚焦链接并使用Enter激活
        label.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard)

        # 链接可打开
        # label.setTextInteractionFlags(
        #     Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse | Qt.LinksAccessibleByKeyboard)
        # label.setTextInteractionFlags(Qt.TextBrowserInteraction)  # QTextBrowser的默认值，与上面等效

        # 可以编辑
        # label.setTextInteractionFlags(Qt.TextEditable | Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse)
        # label.setTextInteractionFlags(Qt.TextEditorInteraction)  # 文本编辑器的默认值，与上面等效

        # 选中（仅可编辑状态下可用）
        # label.setSelection(1, 2)  # 起始位置与选中个数
        # print(label.hasSelectedText())  # 是否被选中
        # print(label.selectedText())  # 被选中的文本
        # print(label.selectionStart())  # 被选中文本的起始位置


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

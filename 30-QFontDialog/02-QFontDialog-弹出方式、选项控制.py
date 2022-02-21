import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog-功能作用")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton("测试按钮", self)
        btn.move(100, 100)
        label = QLabel(self)
        label.move(100, 200)
        label.setText("https://muzing.top")

        fd = QFontDialog(self)

        def cfc(font):
            label.setFont(font)
            label.adjustSize()

        fd.currentFontChanged.connect(cfc)

        def font_sel():
            print("字体已经被选择", fd.selectedFont().family())

        # ------------选项控制-----------------
        """
        QFontDialog.FontDialogOption:
        QFontDialog.NoButtons  不显示“确定”和”取消“按钮。（对“实时对话框”有用）
        QFontDialog.DontUseNativeDialog  在Mac上使用Qt的标准字体对话框而不是Apple的原生字体对话框
        QFontDialog.ScalableFonts  显示可缩放字体
        QFontDialog.NonScalableFonts  显示不可缩放的字体
        QFontDialog.MonospacedFonts  显示等宽字体
        QFontDialog.ProportionalFonts  显示比例字体
        """
        # fd.setOption(QFontDialog.MonospacedFonts, on=True)
        fd.setOptions(QFontDialog.NoButtons | QFontDialog.MonospacedFonts)
        print(fd.testOption(QFontDialog.NoButtons))
        print(fd.testOption(QFontDialog.DontUseNativeDialog))

        # -------------弹出方式------------------
        btn.clicked.connect(
            lambda: fd.open(font_sel)
        )  # 在open方法中传入一个槽函数，则打开FontDialog后自动连接

        # if fd.exec():  # 用户点击确定键则返回1，取消键和关闭窗口返回0
        #     print(fd.selectedFont().family())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

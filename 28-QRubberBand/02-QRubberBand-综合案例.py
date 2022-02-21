import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRubberBand-综合案例")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # 0. 添加许多子控件
        for i in range(0, 32):
            cb = QCheckBox(self)
            cb.setText(f"{i}")
            cb.move(i % 4 * 50, i // 4 * 60)

        # 1. 创建一个橡皮筋选中控件
        self.rb = QRubberBand(QRubberBand.Rectangle, self)

    def mousePressEvent(self, a0) -> None:
        # 2. 尺寸大小：鼠标点击的位置点，00
        self.origin_pos = a0.pos()
        self.rb.setGeometry(QRect(self.origin_pos, QSize()))
        # 3. 展示橡皮筋控件
        self.rb.show()

    def mouseMoveEvent(self, a0) -> None:
        # 4. 调整橡皮筋选中的位置以及尺寸
        self.rb.setGeometry(QRect(self.origin_pos, a0.pos()).normalized())
        # QRect.normalized() 方法解决反向拖动矩形出现负数的情况

    def mouseReleaseEvent(self, a0) -> None:
        # 5. 获取橡皮筋控件的尺寸范围
        rect = self.rb.geometry()
        # 6. 遍历所有子控件，查看哪些子控件在区域范围
        for child in self.children():
            if rect.contains(child.geometry()) and child.inherits("QCheckBox"):
                child.toggle()
        self.rb.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

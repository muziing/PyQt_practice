import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # input_d = QInputDialog(self, Qt.FramelessWindowHint)  # 可以传入WindowFlags
        input_d = QInputDialog(self)
        # -------取子控件------
        # input_d.setComboBoxItems(["1", "2", "abc"])
        input_d.setLabelText("请输入你的姓名")
        input_d.setOkButtonText("好的")
        input_d.setCancelButtonText("我想取消")

        # -------设置选项-----------
        # input_d.setOptions(QInputDialog.UseListViewForComboBoxItems)
        """
        QInputDialog.InputDialogOption:
        
        QInputDialog.NoButtons  不显示“确定”和“取消”按钮（对“实时对话框”有用）
        QInputDialog。UseListViewForComboBoxItems  用QListView而不是不可编辑的QComboBox来显示使用setComboBoxItems
        QInputDialog。UsePlainTextEditForTextInput  使用QPlainTextEdit进行多行文本输入
        """
        # print(input_d.options())

        # -------输入模式---------
        input_d.setInputMode(QInputDialog.TextInput)
        """
        QInputDialog.InputMode:
        
        QInputDialog.TextInput
        QInputDialog.IntInput
        QInputDialog.DoubleInput
        """

        # -------各个小分类详细设置--------
        """
        InputMode  整型
            setIntMaximum(int)
            setIntMinimum(int)
            setIntRange(int, int)
            setIntStep(int)
            setIntValue(int)
        
        Double  浮点型
            setDoubleMaximum(float)
            setDoubleDecimals(int)
            setDoubleMinimum(float)
            setDoubleRange(float, float)
            setDoubleStep(float)
            setDoubleValue(float)
        
        Text  字符串
            setTextEchoMode(QLineEdit.EchoMode)
            setTextValue(str)
        
        ComboBox  下拉列表
            setComboBoxItems(Iterable[str])
            setComboBoxEditable(bool)
        """

        input_d.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

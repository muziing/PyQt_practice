from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # self.QObject继承结构测试()
        # self.QObject对象名称和属性的操作()
        # self.QObject案例测试()
        self.QObject对象的父子关系操作()

    def QObject继承结构测试(self):
        mros = QObject.mro()
        for mro in mros:
            print(mro)

    def QObject对象名称和属性的操作(self):
        # 测试API
        obj = QObject()
        obj.setObjectName("notice")  # 给一个Qt对象设置一个名称，一般是唯一的，当做对象的ID使用
        print(obj.objectName())  # 获取一个Qt对象的名称

        obj.setProperty("notice_level", "error")  # 给一个Qt对象动态的添加一个属性与值
        obj.setProperty("notice_level2", "warning")

        print(obj.property("notice_level"))  # 获取一个对象的属性值
        print(obj.dynamicPropertyNames())  # 获取一个对象中所有通过setProperty()设置的属性名称

    def QObject案例测试(self):

        with open("QObject.qss", "r") as f:
            qApp.setStyleSheet(f.read())  # QSS样式表

        label = QLabel(self)
        label.setText("社会我顺哥")
        label.setObjectName("notice")  # 根据QSS中设置的规则，只有ObjectName为notice的QLabel才会改变样式

        label2 = QLabel(self)
        label2.move(0, 60)
        label2.setText("人狠话不多")
        label2.setObjectName("notice")
        label2.setProperty("notice_level", "normal")

    def QObject对象的父子关系操作(self):
        # 测试API
        obj0 = QObject()
        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()
        obj4 = QObject()
        obj5 = QObject()
        print('obj0', obj0)
        print('obj1', obj1)
        print('obj2', obj2)
        print('obj3', obj3)
        print('obj4', obj4)
        print('obj5', obj5)

        obj1.setParent(obj0)
        obj2.setParent(obj0)
        obj2.setObjectName('2')

        # label = QLabel()
        # label.setParent(obj0)

        obj3.setParent(obj1)
        obj3.setObjectName('3')
        obj4.setParent(obj2)
        obj5.setParent(obj2)

        # print(obj4.parent())
        # print(obj0.children())
        print(obj0.findChild(QObject))
        print(obj0.findChild(QObject, '2'))
        print(obj0.findChild(QObject, '3'))
        print(obj0.findChild(QObject, '3', Qt.FindDirectChildrenOnly))
        print(obj0.findChildren(QObject))
        # print(obj0.findChild(QLabel))  # 会报错


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

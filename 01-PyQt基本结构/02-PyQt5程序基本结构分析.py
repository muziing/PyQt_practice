# 0.导入需要的包和模块
import sys

from PyQt5.Qt import *  # 主要包含了我们常用的一些类，汇总到了一块

# 代码 执行方式 1.Pycharm 2. 命令行 python + 代码名称
# 当通过命令行启动这个程序的时候，可以设定一种功能（接收命令行传递的参数，来执行不同的业务逻辑）
# sys.argv "从程序外部获取参数的桥梁"


# argv = sys.argv
# print(argv)
# try:
#     if argv[1] == '1':
#         print("传入了1")
# except IndexError:
#     print("可能未从外部传入参数")

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)
# print(app.arguments())

print(qApp.arguments())  # 全局变量

# 2.控件的操作
# 创建控件，设置控件（大小，位置，样式……），事件，信号的处理
# 2.1创建控件
# 当我们创建一个控件之后，如果该控件无父控件，则把它作为顶层控件（窗口）
# 系统会自动给窗口添加一些装饰（标题栏），窗口控件具备一些特性（设置标题、图标等）
window = QWidget()
# 2.2设置控件
window.setWindowTitle("这是一个窗口标题")
window.resize(500, 500)

# 控件也可以作为一个容器（承载其他控件）
label = QLabel(window)
label.setText("label里的文字")
label.show()

# 2.3展示控件
# 刚创建好一个控件之后（该控件无父控件），默认不会展示该控件，只有手动调用show()

window.show()

# 3.应用程序的执行， 进入到消息循环
# 让整个程序开始执行，并且进入到消息循环（无限循环）
# 检测整个程序所接收到的用户的交互信息
sys.exit(app.exec_())

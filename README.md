# PyQt5 代码笔记

***用代码学 PyQt5 !***

![PyQt Version](https://img.shields.io/badge/PyQt-5.15-blue)
![license](https://img.shields.io/badge/license-GPL--3.0-brightgreen)
![Github stars](https://img.shields.io/github/stars/muziing/PyQt_practice.svg)
![GitHub forks](https://img.shields.io/github/forks/muziing/PyQt_practice.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

## 重要说明！

本项目的新版 **[「PySide6 代码教程」](https://github.com/muziing/PySide6-Code-Tutorial)** 已经开始动工啦！

相比本项目，有如下升级：

- Python `3.10` + PySide `6.3`，版本更新、功能更强大
- 项目结构更清晰，不再将控件、信号与槽、QSS 等等各种知识混杂在一起
- 代码中注释讲解比例更高更清晰
- PySide 由 Qt 官方提供支持，比 PyQt 许可更宽松、文档更全面

欢迎新老读者[前往](https://github.com/muziing/PySide6-Code-Tutorial)阅读和提供贡献！

## 基本说明

- 每个模块（`.py`文件）都可运行，展示了各种控件的各种功能属性作用，代码中有注释讲解
- 在自己的机器上实际运行一下，仔细观察一下每个属性值的改变会怎样影响控件的外观行为，可能比静态的文档教程更有效。
- 目前还在更新完善中，也期待小伙伴加入，共同完善这个仓库（提交 PR 或者 [联系作者](https://muzing.top/about/) ）
- 由于作者精力有限，暂停 [Gitee仓库](https://gitee.com/muzing/PyQt_practice) 的更新维护，最新修改以 [GitHub仓库](https://github.com/muziing/PyQt_practice) 为准

## 使用方法

1. Star 本仓库
2. 克隆本仓库到本地（ `git clone https://github.com/muziing/PyQt_practice.git` ），或[下载 zip](https://github.com/muziing/PyQt_practice/archive/refs/heads/master.zip) 归档并解压
3. 在命令行执行 `pip install -r requirements.txt` 安装依赖
4. 进入你感兴趣的控件对应的文件夹，运行任何一个`.py`文件观察效果
5. 对于大多数目录，首个文件都是一个 Markdown 文档，为 Qt 官方文档对应的中文翻译并简单整理版

以 [47-QListView](./47-QListView) 目录下的 [02-QListView-自动换行、布局间距、对齐、单词省略.py](./47-QListView/02-QListView-自动换行、布局间距、对齐、单词省略.py) 为例：

```python
# 02-QListView-自动换行、布局间距、对齐、单词省略.py
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListView-自动换行、布局间距、对齐、单词省略")
        self.resize(500, 500)
        self.data_list = [f"Item{i}" for i in range(15)]  # 将数据列表保存在属性中
        self.data_list.append("Something very very long")  # 再添加一个特殊的很长的项
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton("增大Spacing", self)
        btn.move(350, 200)
        list_view = QListView(self)  # 创建list view对象
        list_view.move(100, 100)
        list_view.resize(200, 200)
        slm = QStringListModel()  # 创建model模型
        slm.setStringList(self.data_list)  # 为模型设置数据
        list_view.setModel(slm)  # 为视图设置模型

        # -------自动换行---------
        list_view.setWrapping(True)  # 打开自动换行
        # 对于 Flow 为 TopToBottom，应该叫做“自动换列”，垂直空间不能一次全部显示所有项时，再右侧再加一列显示，而不是加滚动条

        # -------布局间距--------
        list_view.setSpacing(10)  # 默认为0

        def test_slot():
            """测试按钮的槽函数"""
            list_view.setSpacing(list_view.spacing() + 5)  # 修改此值会导致重新布局

        btn.clicked.connect(test_slot)

        # --------对齐-----------
        # setItemAlignment 只有在 ListMode 为 TopToBottom 且 wrapping 打开时才有效
        # list_view.setItemAlignment(Qt.AlignTop)  # 垂直靠上对齐
        list_view.setItemAlignment(Qt.AlignVCenter | Qt.AlignLeft)  # 垂直居中，水平靠左对齐

        # ------单词省略------
        list_view.setWordWrap(True)  # 启用单词省略，太长的文本将收到省略号...中
        # list_view.setTextElideMode(Qt.ElideLeft)  # 省略号在最左侧
        list_view.setTextElideMode(Qt.ElideMiddle)  # 省略号在中间
        # list_view.setTextElideMode(Qt.ElideNone)  # 无省略号，但是最后的内容仍然会被省略


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

```

1. 直接运行这段代码即可看到程序窗口和上面的 QListView 控件
2. 注释/取消注释第 26 行代码，以观察自动换行属性的效果
3. 按下"增大Spacing"按钮，以观察不同的 Spacing 值的显示效果
4. 每次注释掉40/41行代码中的一个，运行另一行，以观察不同的 ItemAlignment 值的对齐效果
5. 每次注释掉45/46/47行代码中的一个，运行剩下的那行，以观察不同的省略号模式的效果
6. 在同一目录（[47-QListView](./47-QListView)）下的第一个文件 [00-QListView-列表视图.md](./47-QListView/00-QListView-列表视图.md) 中查看更多信息

## PyQt 相关分享

[一些 PyQt 相关文档、教程、Demo、QSS 美化等收集整理](share.md)

[GitHub PyQt 相关仓库收集](https://github.com/stars/muziing/lists/pyqt)

## [仓库文件目录](toc.md)

**[点击图片以在线浏览带有超链接的思维导图](https://www.processon.com/view/link/60f23569637689739c3a5cbb)**

[![思维导图目录](http://processon.com/chart_image/60f231530791291daf471f7f.png)](https://www.processon.com/view/link/60f23569637689739c3a5cbb)

### 01 [PyQt基本结构](./01-PyQt基本结构)

0. [PyQt5-初体验.py](./01-PyQt基本结构/01-PyQt5-初体验.py)
1. [PyQt5程序基本结构分析.py](./01-PyQt基本结构/02-PyQt5程序基本结构分析.py)
2. [面向对象版本代码.py](./01-PyQt基本结构/03-面向对象版本代码.py)
3. [控件类的继承关系.py](./01-PyQt基本结构/04-控件类的继承关系.py)

### 02 [QObject](./02-QObject)

0. [QObject.py](./02-QObject/01-QObject.py)
1. [QObject_2.py](./02-QObject/02-QObject_2.py)
2. [信号的操作.py](./02-QObject/03-信号的操作.py)
3. [信号的操作（小案例1）.py](./02-QObject/04-信号的操作（小案例1）.py)
4. [信号的操作（小案例2）.py](./02-QObject/05-信号的操作（小案例2）.py)
5. [QObject类型判定.py](./02-QObject/06-QObject类型判定.py)
6. [QObject类型判定-案例.py](./02-QObject/07-QObject类型判定-案例.py)
7. [QObject对象删除.py](./02-QObject/08-QObject对象删除.py)
8. [PyQt事件机制.py](./02-QObject/09-PyQt事件机制.py)
9. [QObject定时器.py](./02-QObject/10-QObject定时器.py)
10. [QObject定时器-案例.py](./02-QObject/11-QObject定时器-案例.py)

### 03 [QWidget](./03-QWidget)

0. [QWidget-用户界面的基类.md](./03-QWidget/00-QWidget-用户界面的基类.md)
1. [QWidget-简介.py](./03-QWidget/01-QWidget-简介.py)
2. [QWidget-大小位置.py](./03-QWidget/02-QWidget-大小位置.py)
3. [QWidget-案例.py](./03-QWidget/03-QWidget-案例.py)
4. [QWidget-最大最小尺寸-API.py](./03-QWidget/04-QWidget-最大最小尺寸-API.py)
5. [QWidget-内容边距操作.py](./03-QWidget/05-QWidget-内容边距操作.py)
6. [QWidget-鼠标相关操作.py](./03-QWidget/06-QWidget-鼠标相关操作.py)
7. [QWidget-鼠标跟踪-API.py](./03-QWidget/07-QWidget-鼠标跟踪-API.py)
8. [QWidget-鼠标相关操作-案例.py](./03-QWidget/08-QWidget-鼠标相关操作-案例.py)
9. [QWidget-案例1-鼠标移入移出.py](./03-QWidget/09-QWidget-案例1-鼠标移入移出.py)
10. [QWidget-案例2-键盘点击案例.py](./03-QWidget/10-QWidget-案例2-键盘点击案例.py)
11. [QWidget-案例3-鼠标拖动窗口案例.py](./03-QWidget/11-QWidget-案例3-鼠标拖动窗口案例.py)
12. [QWidget-父子关系-API.py](./03-QWidget/12-QWidget-父子关系-API.py)
13. [QWidget-父子关系-案例.py](./03-QWidget/13-QWidget-父子关系-案例.py)
14. [QWidget-层级关系调整.py](./03-QWidget/14-QWidget-层级关系调整.py)
15. [QWidget-顶层窗口相关操作.py](./03-QWidget/15-QWidget-顶层窗口相关操作.py)
16. [QWidget-窗口状态.py](./03-QWidget/16-QWidget-窗口状态.py)
17. [QWidget-窗口最大化最小化、WindowFlags笔记.py](./03-QWidget/17-QWidget-窗口最大化最小化、WindowFlags笔记.py)
18. [QWidget-顶层窗口操作-案例.py](./03-QWidget/18-QWidget-顶层窗口操作-案例.py)
19. [QWidget-交互状态-显示隐藏控件、设置控件不可用.py](./03-QWidget/19-QWidget-交互状态-显示隐藏控件、设置控件不可用.py)
20. [QWidget-交互状态-是否被编辑、是否为活动窗口.py](./03-QWidget/20-QWidget-交互状态-是否被编辑、是否为活动窗口.py)
21. [QWidget-交互状态-关闭与释放.py](./03-QWidget/21-QWidget-交互状态-关闭与释放.py)
22. [QWidget-交互状态-案例-登录界面.py](./03-QWidget/22-QWidget-交互状态-案例-登录界面.py)
23. [QWidget-信息提示.py](./03-QWidget/23-QWidget-信息提示.py)
24. [QWidget-焦点控制.py](./03-QWidget/24-QWidget-焦点控制.py)

### 04 [QAbstractButton](./04-QAbstractButton)

0. [QAbstractButton-按钮的抽象基类.md](./04-QAbstractButton/00-QAbstractButton-按钮的抽象基类.md)
1. [QAbstractButton-简单介绍.py](./04-QAbstractButton/01-QAbstractButton-简单介绍.py)
2. [QAbstractButton-功能测试.py](./04-QAbstractButton/02-QAbstractButton-功能测试.py)
3. [QAbstractButton-状态设置.py](./04-QAbstractButton/03-QAbstractButton-状态设置.py)
4. [QAbstractButton-排他性.py](./04-QAbstractButton/04-QAbstractButton-排他性.py)
5. [QAbstractButton-模拟点击.py](./04-QAbstractButton/05-QAbstractButton-模拟点击.py)
6. [QAbstractButton-点击有效区域.py](./04-QAbstractButton/06-QAbstractButton-点击有效区域.py)
7. [QAbstractButton-可用信号.py](./04-QAbstractButton/07-QAbstractButton-可用信号.py)

### 05 [QPushButton](./05-QPushButton)

0. [QPushButton-普通按钮.md](./05-QPushButton/00-QPushButton-普通按钮.md)
1. [QPushButton-构造函数.py](./05-QPushButton/01-QPushButton-构造函数.py)
2. [QPushButton-菜单.py](./05-QPushButton/02-QPushButton-菜单.py)
3. [QPushButton-扁平化.py](./05-QPushButton/03-QPushButton-扁平化.py)
4. [QPushButton-默认处理.py](./05-QPushButton/04-QPushButton-默认处理.py)
5. [QPushButton-右键菜单.py](./05-QPushButton/05-QPushButton-右键菜单.py)
6. [QCommandLinkButton.py](./05-QPushButton/06-QCommandLinkButton.py)

### 06 [QToolButton](./06-QToolButton)

0. [QToolButton-工具栏按钮.md](./06-QToolButton/00-QToolButton-工具栏按钮.md)
1. [QToolButton-创建与基本显示.py](./06-QToolButton/01-QToolButton-创建与基本显示.py)
2. [QToolButton-样式设置.py](./06-QToolButton/02-QToolButton-样式设置.py)
3. [QToolButton-箭头.py](./06-QToolButton/03-QToolButton-箭头.py)
4. [QToolButton-自动提升.py](./06-QToolButton/04-QToolButton-自动提升.py)
5. [QToolButton-菜单和弹出模式.py](./06-QToolButton/05-QToolButton-菜单和弹出模式.py)
6. [QToolButton-可用信号.py](./06-QToolButton/06-QToolButton-可用信号.py)

### 07 [QRadioButton](./07-QRadioButton)

0. [QRadioButton-单选按钮.md](./07-QRadioButton/00-QRadioButton-单选按钮.md)
1. [QRadioButton-创建和基本设置、信号.py](./07-QRadioButton/01-QRadioButton-创建和基本设置、信号.py)
2. [QRadioButton-多组互斥问题.py](./07-QRadioButton/02-QRadioButton-多组互斥问题.py)

### 08 [QButtonGroup](./08-QButtonGroup)

0. [QButtonGroup-按钮组.md](./08-QButtonGroup/00-QButtonGroup-按钮组.md)
1. [QButtonGroup-创建与使用.py](./08-QButtonGroup/01-QButtonGroup-创建与使用.py)
2. [QButtonGroup-查看按钮、移除按钮、id操作、取消独占.py](./08-QButtonGroup/02-QButtonGroup-查看按钮、移除按钮、id操作、取消独占.py)
3. [QButtonGroup-信号.py](./08-QButtonGroup/03-QButtonGroup-信号.py)

### 09 [QCheckBox](./09-QCheckBox)

0. [QCheckButton-复选框.md](./09-QCheckBox/00-QCheckButton-复选框.md)
1. [QCheckBox-功能使用.py](./09-QCheckBox/01-QCheckBox-功能使用.py)
2. [QCheckBox-信号.py](./09-QCheckBox/02-QCheckBox-信号.py)

### 10 [QLineEdit](./10-QLineEdit)

0. [QLineEdit-单行文本编辑器.md](./10-QLineEdit/00-QLineEdit-单行文本编辑器.md)
1. [QLineEdit-创建、插入与获取内容.py](./10-QLineEdit/01-QLineEdit-创建、插入与获取内容.py)
2. [QLineEdit-文本的设置与获取-案例.py](./10-QLineEdit/02-QLineEdit-文本的设置与获取-案例.py)
3. [QLineEdit-文本输出模式.py](./10-QLineEdit/03-QLineEdit-文本输出模式.py)
4. [QLineEdit-登录案例.py](./10-QLineEdit/04-QLineEdit-登录案例.py)
5. [QLineEdit-占位文本设置、清空按钮.py](./10-QLineEdit/05-QLineEdit-占位文本设置、清空按钮.py)
6. [QLineEdit-添加自定义行为-明密文切换.py](./10-QLineEdit/06-QLineEdit-添加自定义行为-明密文切换.py)
7. [QLineEdit-自动补全.py](./10-QLineEdit/07-QLineEdit-自动补全.py)
8. [QLineEdit-长度和只读限制.py](./10-QLineEdit/08-QLineEdit-长度和只读限制.py)
9. [QLineEdit-验证器的使用.py](./10-QLineEdit/09-QLineEdit-验证器的使用.py)
10. [QLineEdit-验证器-掩码.py](./10-QLineEdit/10-QLineEdit-验证器-掩码.py)
11. [QLineEdit-文本修改状态.py](./10-QLineEdit/11-QLineEdit-文本修改状态.py)
12. [QLineEdit-光标位置控制.py](./10-QLineEdit/12-QLineEdit-光标位置控制.py)
13. [QLineEdit-文本边距设定.py](./10-QLineEdit/13-QLineEdit-文本边距设定.py)
14. [QLineEdit-对齐方式.py](./10-QLineEdit/14-QLineEdit-对齐方式.py)
15. [QLineEdit-编辑功能.py](./10-QLineEdit/15-QLineEdit-编辑功能.py)
16. [QLineEdit-编辑功能-选中.py](./10-QLineEdit/16-QLineEdit-编辑功能-选中.py)
17. [QLineEdit-信号.py](./10-QLineEdit/17-QLineEdit-信号.py)

### 11 [QFrame](./11-QFrame)

0. [QFrame-框架控件的基类.md](./11-QFrame/00-QFrame-框架控件的基类.md)
1. [QFrame-创建.py](./11-QFrame/01-QFrame-创建.py)
2. [QFrame-功能作用.py](./11-QFrame/02-QFrame-功能作用.py)

### 12 [QAbstractScrollArea](./12-QAbstractScrollArea)

0. [QAbstractScrollArea-滚动区域的低级抽象.md](./12-QAbstractScrollArea/00-QAbstractScrollArea-滚动区域的低级抽象.md)
1. [QAbstractScrollArea.py](./12-QAbstractScrollArea/01-QAbstractScrollArea.py)

### 13 [QTextEdit](./13-QTextEdit)

0. [QTextEdit-文本编辑器.md](./13-QTextEdit/00-QTextEdit-文本编辑器.md)
1. [QTextEdit-创建.py](./13-QTextEdit/01-QTextEdit-创建.py)
2. [QTextEdit-占位文本的设置.py](./13-QTextEdit/02-QTextEdit-占位文本的设置.py)
3. [QTextEdit-文本内容的设置.py](./13-QTextEdit/03-QTextEdit-文本内容的设置.py)
4. [QTextEdit-文本光标-插入文字、图片、句子.py](./13-QTextEdit/04-QTextEdit-文本光标-插入文字、图片、句子.py)
5. [QTextEdit-文本光标-插入列表.py](./13-QTextEdit/05-QTextEdit-文本光标-插入列表.py)
6. [QTextEdit-文本光标-插入表格.py](./13-QTextEdit/06-QTextEdit-文本光标-插入表格.py)
7. [QTextEdit-文本光标-插入文本块.py](./13-QTextEdit/07-QTextEdit-文本光标-插入文本块.py)
8. [QTextEdit-文本光标-插入文本框架.py](./13-QTextEdit/08-QTextEdit-文本光标-插入文本框架.py)
9. [QTextEdit-文本光标-格式操作.py](./13-QTextEdit/09-QTextEdit-文本光标-格式操作.py)

### 14 [QPlainTextEdit](./14-QPlainTextEdit)

0. [QPlainTextEdit-纯文本编辑器.md](./14-QPlainTextEdit/00-QPlainTextEdit-纯文本编辑器.md)
1. [QPlainTextEdit-创建、占位提示文本、只读、字符格式.py](./14-QPlainTextEdit/01-QPlainTextEdit-创建、占位提示文本、只读、字符格式.py)
2. [QPlainTextEdit-软换行、覆盖模式、tab控制.py](./14-QPlainTextEdit/02-QPlainTextEdit-软换行、覆盖模式、tab控制.py)
3. [QPlainTextEdit-文本操作、块操作.py](./14-QPlainTextEdit/03-QPlainTextEdit-文本操作、块操作.py)
4. [QPlainTextEdit-放大缩小、滚动内容以显示光标.py](./14-QPlainTextEdit/04-QPlainTextEdit-放大缩小、滚动内容以显示光标.py)
5. [QPlainTextEdit-光标操作.py](./14-QPlainTextEdit/05-QPlainTextEdit-光标操作.py)
6. [QPlainTextEdit-信号.py](./14-QPlainTextEdit/06-QPlainTextEdit-信号.py)
7. [QPlainTextEdit-案例-显示行号.py](./14-QPlainTextEdit/07-QPlainTextEdit-案例-显示行号.py)

### 15 [QKeySequenceEdit](./15-QKeySequenceEdit)

0. [QKeySequenceEdit-快捷键编辑器.md](./15-QKeySequenceEdit/00-QKeySequenceEdit-快捷键编辑器.md)
1. [QKeySequenceEdit-创建、功能、信号.py](./15-QKeySequenceEdit/01-QKeySequenceEdit-创建、功能、信号.py)
2. [QKeySequence-补充.py](./15-QKeySequenceEdit/02-QKeySequence-补充.py)

### 16 [QAbstractSpinBox](./16-QAbstractSpinBox)

0. [QAbstractSpinBox-数字设定框的抽象基类.md](./16-QAbstractSpinBox/00-QAbstractSpinBox-数字设定框的抽象基类.md)
1. [QAbstractSpinBox-创建、模拟子类化、获取与设置控件内容.py](./16-QAbstractSpinBox/01-QAbstractSpinBox-创建、模拟子类化、获取与设置控件内容.py)
2. [QAbstractSpinBox-长按累加加速、只读.py](./16-QAbstractSpinBox/02-QAbstractSpinBox-长按累加加速、只读.py)
3. [QAbstractSpinBox-对齐方式、周边框架、清空文本内容、按钮标识.py](./16-QAbstractSpinBox/03-QAbstractSpinBox-对齐方式、周边框架、清空文本内容、按钮标识.py)
4. [QAbstractSpinBox-内容验证、信号.py](./16-QAbstractSpinBox/04-QAbstractSpinBox-内容验证、信号.py)

### 17 [QSpinBox](./17-QSpinBox)

0. [QSpinBox-数字设定框.md](./17-QSpinBox/00-QSpinBox-数字设定框.md)
1. [QSpinBox-创建、最大值最小值范围、数值循环.py](./17-QSpinBox/01-QSpinBox-创建、最大值最小值范围、数值循环.py)
2. [QSpinBox-步长设置、前后缀和特殊文本、进制设置.py](./17-QSpinBox/02-QSpinBox-步长设置、前后缀和特殊文本、进制设置.py)
3. [QSpinBox-值的设置和获取、自定义展示格式.py](./17-QSpinBox/03-QSpinBox-值的设置和获取、自定义展示格式.py)
4. [QSpinBox-信号.py](./17-QSpinBox/04-QSpinBox-信号.py)

### 18 [QDoubleSpinBox](./18-QDoubleSpinBox)

0. [QDoubleSpinBox-浮点数设定框.md](./18-QDoubleSpinBox/00-QDoubleSpinBox-浮点数设定框.md)
1. [QDoubleSpinBox-创建、数值范围、数值循环、设置步长、前后缀.py](./18-QDoubleSpinBox/01-QDoubleSpinBox-创建、数值范围、数值循环、设置步长、前后缀.py)
2. [QDoubleSpinBox-最小值特殊文本、小数位数、设置与获取数值、自定义展示格式.py](./18-QDoubleSpinBox/02-QDoubleSpinBox-最小值特殊文本、小数位数、设置与获取数值、自定义展示格式.py)
3. [QDoubleSpinBox-信号.py](./18-QDoubleSpinBox/03-QDoubleSpinBox-信号.py)

### 19 [QDateTimeEdit](./19-QDateTimeEdit)

0. [QDateTimeEdit-日期时间编辑器.md](./19-QDateTimeEdit/00-QDateTimeEdit-日期时间编辑器.md)
1. [QDateTime、QDate、QTime.py](./19-QDateTimeEdit/01-QDateTime、QDate、QTime.py)
2. [QDateTimeEdit-创建、显示格式、section操作.py](./19-QDateTimeEdit/02-QDateTimeEdit-创建、显示格式、section操作.py)

### 20 [QDateEdit](./20-QDateEdit)

0. [QDateEdit-日期编辑器.md](./20-QDateEdit/00-QDateEdit-日期编辑器.md)

### 21 [QTimeEdit](./21-QTimeEdit)

0. [QTimeEdit-时间编辑器.md](./21-QTimeEdit/00-QTimeEdit-时间编辑器.md)

### 22 [QComboBox](./22-QComboBox)

0. [QComboBox-组合下拉框.md](./22-QComboBox/00-QComboBox-组合下拉框.md)
1. [QComboBox-创建、数据操作.py](./22-QComboBox/01-QComboBox-创建、数据操作.py)
2. [QComboBox-模型操作、视图操作.py](./22-QComboBox/02-QComboBox-模型操作、视图操作.py)
3. [QComboBox-数据获取.py](./22-QComboBox/03-QComboBox-数据获取.py)
4. [QComboBox-数据限制.py](./22-QComboBox/04-QComboBox-数据限制.py)
5. [QComboBox-功能.py](./22-QComboBox/05-QComboBox-功能.py)
6. [QComboBox-信号.py](./22-QComboBox/06-QComboBox-信号.py)
7. [QComboBox-案例.py](./22-QComboBox/07-QComboBox-案例.py)

### 23 [QFontComboBox](./23-QFontComboBox)

0. [QFontComboBox-字体下拉框.md](./23-QFontComboBox/00-QFontComboBox-字体下拉框.md)
1. [QFontComboBox-功能作用.py](./23-QFontComboBox/01-QFontComboBox-功能作用.py)

### 24 [QAbstractSlider](./24-QAbstractSlider)

0. [QAbstractSlider-滑块控件抽象基类.md](./24-QAbstractSlider/00-QAbstractSlider-滑块控件抽象基类.md)
1. [QAbstractSlider-创建、数值范围、当前数值、步长.py](./24-QAbstractSlider/01-QAbstractSlider-创建、数值范围、当前数值、步长.py)
2. [QAbstractSlider-是否追踪、滑块位置、倒立外观、操作反转、滑块方向.py](./24-QAbstractSlider/02-QAbstractSlider-是否追踪、滑块位置、倒立外观、操作反转、滑块方向.py)
3. [QAbstractSlider-是否按下、信号.py](./24-QAbstractSlider/03-QAbstractSlider-是否按下、信号.py)

### 25 [QSlider](./25-QSlider)

0. [QSlider-滑块控件.md](./25-QSlider/00-QSlider-滑块控件.md)
1. [QSlider-刻度控制.py](./25-QSlider/01-QSlider-刻度控制.py)
2. [QSlider-拓展案例.py](./25-QSlider/02-QSlider-拓展案例.py)
3. [QSlider-鼠标跳转优化.py](./25-QSlider/03-QSlider-鼠标跳转优化.py)

### 26 [QScrollBar](./26-QScrollBar)

0. [QScrollBar-滚动条.md](./26-QScrollBar/00-QScrollBar-滚动条.md)
1. [QScrollBar-功能作用.py](./26-QScrollBar/01-QScrollBar-功能作用.py)

### 27 [QDial](./27-QDial)

0. [QDial-转盘控件.md](./27-QDial/00-QDial-转盘控件.md)
1. [QDial-功能作用.py](./27-QDial/01-QDial-功能作用.py)

### 28 [QRubberBand](./28-QRubberBand)

0. [QRubberBand-选择框线.md](./28-QRubberBand/00-QRubberBand-选择框线.md)
1. [QRubberBand-创建.py](./28-QRubberBand/01-QRubberBand-创建.py)
2. [QRubberBand-综合案例.py](./28-QRubberBand/02-QRubberBand-综合案例.py)

### 29 [QDialog](./29-QDialog)

0. [QDialog-对话框窗口基类.md](./29-QDialog/00-QDialog-对话框窗口基类.md)
1. [QDialog-模态与非模态、创建.py](./29-QDialog/01-QDialog-模态与非模态、创建.py)
2. [QDialog-是否显示尺寸调整控件、常用操作槽、设置和获取数值.py](./29-QDialog/02-QDialog-是否显示尺寸调整控件、常用操作槽、设置和获取数值.py)
3. [QDialog-信号.py](./29-QDialog/03-QDialog-信号.py)

### 30 [QFontDialog](./30-QFontDialog)

0. [QFontDialog-字体选择对话框.md](./30-QFontDialog/00-QFontDialog-字体选择对话框.md)
1. [QFontDialog-创建.py](./30-QFontDialog/01-QFontDialog-创建.py)
2. [QFontDialog-弹出方式、选项控制.py](./30-QFontDialog/02-QFontDialog-弹出方式、选项控制.py)
3. [QFontDialog-静态方法.py](./30-QFontDialog/03-QFontDialog-静态方法.py)

### 31 [QColorDialog](./31-QColorDialog)

0. [QColorDialog-颜色选择对话框.md](./31-QColorDialog/00-QColorDialog-颜色选择对话框.md)
1. [QColorDialog-创建.py](./31-QColorDialog/01-QColorDialog-创建.py)
2. [QColorDialog-功能作用.py](./31-QColorDialog/02-QColorDialog-功能作用.py)
3. [QColorDialog-静态方法.py](./31-QColorDialog/03-QColorDialog-静态方法.py)
4. [QColorDialog-信号.py](./31-QColorDialog/04-QColorDialog-信号.py)

### 32 [QFileDialog](./32-QFileDialog)

0. [QFileDialog-文件选择对话框.md](./32-QFileDialog/00-QFileDialog-文件选择对话框.md)
1. [QFileDialog-静态方法-弹出文件操作对话框.py](./32-QFileDialog/01-QFileDialog-静态方法-弹出文件操作对话框.py)
2. [QFileDialog-静态方法-弹出文件夹操作对话框.py](./32-QFileDialog/02-QFileDialog-静态方法-弹出文件夹操作对话框.py)
3. [QFileDialog-构造函数、接收模式、默认后缀名、文件模式.py](./32-QFileDialog/03-QFileDialog-构造函数、接收模式、默认后缀名、文件模式.py)
4. [QFileDialog-名称过滤器、显示信息详细程度、设置指定角色的标签名称.py](./32-QFileDialog/04-QFileDialog-名称过滤器、显示信息详细程度、设置指定角色的标签名称.py)
5. [QFileDialog-信号.py](./32-QFileDialog/05-QFileDialog-信号.py)

### 33 [QInputDialog](./33-QInputDialog)

0. [QInputDialog-输入对话框.md](./33-QInputDialog/00-QInputDialog-输入对话框.md)
1. [QInputDialog-静态方法.py](./33-QInputDialog/01-QInputDialog-静态方法.py)
2. [QInputDialog-创建、功能作用.py](./33-QInputDialog/02-QInputDialog-创建、功能作用.py)
3. [QInputDialog-信号.py](./33-QInputDialog/03-QInputDialog-信号.py)

### 34 [QCalendarWidget](./34-QCalendarWidget)

0. [QCalendarWidget-日历控件.md](./34-QCalendarWidget/00-QCalendarWidget-日历控件.md)

### 35 [QLabel](./35-QLabel)

0. [QLabel-标签控件.md](./35-QLabel/00-QLabel-标签控件.md)
1. [QLabel-创建、对齐、间距、缩进.py](./35-QLabel/01-QLabel-创建、对齐、间距、缩进.py)
2. [QLabel-文本格式、伙伴.py](./35-QLabel/02-QLabel-文本格式、伙伴.py)
3. [QLabel-内容缩放（图片）.py](./35-QLabel/03-QLabel-内容缩放（图片）.py)
4. [QLabel-文本交互标识和选中.py](./35-QLabel/04-QLabel-文本交互标识和选中.py)
5. [QLabel-外部链接、换行.py](./35-QLabel/05-QLabel-外部链接、换行.py)
6. [QLabel-内容操作.py](./35-QLabel/06-QLabel-内容操作.py)
7. [QLabel-信号.py](./35-QLabel/07-QLabel-信号.py)

### 36 [QLCDNumber](./36-QLCDNumber)

0. [QLCDNumber-液晶数字显示器.md](./36-QLCDNumber/00-QLCDNumber-液晶数字显示器.md)

### 37 [QProgressBar](./37-QProgressBar)

0. [QProgressBar-进度条控件.md](./37-QProgressBar/00-QProgressBar-进度条控件.md)
1. [QProgressBar-基本、区间范围和当前数值.py](./37-QProgressBar/01-QProgressBar-基本、区间范围和当前数值.py)
2. [QProgressBar-文本格式设置.py](./37-QProgressBar/02-QProgressBar-文本格式设置.py)
3. [QProgressBar-文本标签操作、方向、反转.py](./37-QProgressBar/03-QProgressBar-文本标签操作、方向、反转.py)
4. [QProgressBar-信号.py](./37-QProgressBar/04-QProgressBar-信号.py)

### 38 [QErrorMessage](./38-QErrorMessage)

0. [QErrorMessage-错误消息对话框.md](./38-QErrorMessage/00-QErrorMessage-错误消息对话框.md)
1. [QErrorMessage-创建、功能作用.py](./38-QErrorMessage/01-QErrorMessage-创建、功能作用.py)
2. [QErrorMessage-Debug.py](./38-QErrorMessage/02-QErrorMessage-Debug.py)

### 39 [QProgressDialog](./39-QProgressDialog)

0. [QProgressDialog-进度条对话框.md](./39-QProgressDialog/00-QProgressDialog-进度条对话框.md)
1. [QProgressDialog-创建.py](./39-QProgressDialog/01-QProgressDialog-创建.py)
2. [QProgressDialog-最小等待时间、窗口标题、设置子控件.py](./39-QProgressDialog/02-QProgressDialog-最小等待时间、窗口标题、设置子控件.py)

### 40 [QMessageBox](./40-QMessageBox)

0. [QMessageBox-消息提示框.md](./40-QMessageBox/00-QMessageBox-消息提示框.md)
1. [QMessageBox-创建.py](./40-QMessageBox/01-QMessageBox-创建.py)
2. [QMessageBox-按钮操作.py](./40-QMessageBox/02-QMessageBox-按钮操作.py)

### 41 [Layout](./41-Layout)

0. [Layout-布局管理器.md](./41-Layout/00-Layout-布局管理器.md)
1. [Layout-简单使用.py](./41-Layout/00-Layout-简单使用.py)
2. [QBoxLayout-创建、方向、插入、删除.py](./41-Layout/01-QBoxLayout-创建、方向、插入、删除.py)
3. [QBoxLayout-空白、伸缩因子.py](./41-Layout/02-QBoxLayout-空白、伸缩因子.py)
4. [QVBoxLayout、QHBoxLayout.py](./41-Layout/03-QVBoxLayout、QHBoxLayout.py)
5. [QFormLayout-创建、行操作(1).py](./41-Layout/04-QFormLayout-创建、行操作(1).py)
6. [QFormLayout-行操作(2).py](./41-Layout/05-QFormLayout-行操作(2).py)
7. [QFormLayout-行包装策略、对齐、间距、字段增长策略.py](./41-Layout/06-QFormLayout-行包装策略、对齐、间距、字段增长策略.py)
8. [QGridLayout-创建、元素操作.py](./41-Layout/07-QGridLayout-创建、元素操作.py)
9. [QGridLayout-最小列宽行高、拉伸系数、间距控制.py](./41-Layout/08-QGridLayout-最小列宽行高、拉伸系数、间距控制.py)
10. [QGridLayout-原点角、信息获取.py](./41-Layout/09-QGridLayout-原点角、信息获取.py)
11. [QStackedLayout-创建、添加插入获取控件.py](./41-Layout/10-QStackedLayout-创建、添加插入获取控件.py)
12. [QStackedLayout-切换、展示模式、移除控件.py](./41-Layout/11-QStackedLayout-切换、展示模式、移除控件.py)

### 42 [QSS](./42-QSS)

0. [QSS-Qt样式表.md](./42-QSS/00-QSS-Qt样式表.md)
1. [QSS-简介.py](./42-QSS/01-QSS-简介.py)
2. [QSS-导入外部样式表.py](./42-QSS/02-QSS-导入外部样式表.py)

### 43 [pyqtSignal](./43-pyqtSignal)

0. [pyqtSignal-自定义信号.py](./43-pyqtSignal/01-pyqtSignal-自定义信号.py)
1. [pyqtSignal-重载、多个参数.py](./43-pyqtSignal/02-pyqtSignal-重载、多个参数.py)
2. [pyqtSignal-装饰器自动连接.py](./43-pyqtSignal/03-pyqtSignal-装饰器自动连接.py)

### 44 [QMainWindow](./44-QMainWindow)

0. [QMainWindow-主窗口控件.md](./44-QMainWindow/00-QMainWindow-主窗口控件.md)
1. [QMainWindow-创建.py](./44-QMainWindow/01-QMainWindow-创建.py)
2. [QMainWindow-QMenuBar-菜单栏.py](./44-QMainWindow/02-QMainWindow-QMenuBar-菜单栏.py)
3. [QMainWindow-QToolBar-工具栏.py](./44-QMainWindow/03-QMainWindow-QToolBar-工具栏.py)
4. [QMainWindow-QStatusBar-状态栏.py](./44-QMainWindow/04-QMainWindow-QStatusBar-状态栏.py)

### 45 [QDockWidget](./45-QDockWidget)

0. [QDockWidget-浮动停靠控件.md](./45-QDockWidget/00-QDockWidget-浮动停靠控件.md)

### 46 [QAbstractItemView](./46-QAbstractItemView)

0. [QAbstractItemView-项目视图的抽象基类.md](./46-QAbstractItemView/00-QAbstractItemView-项目视图的抽象基类.md)

### 47 [QListView](./47-QListView)

0. [QListView-列表视图.md](./47-QListView/00-QListView-列表视图.md)
1. [QListView-创建、方向、布局模式.py](./47-QListView/01-QListView-创建、方向、布局模式.py)
2. [QListView-自动换行、布局间距、对齐、单词省略.py](./47-QListView/02-QListView-自动换行、布局间距、对齐、单词省略.py)
3. [QListView-布局网格、大小调整模式、移动.py](./47-QListView/03-QListView-布局网格、大小调整模式、移动.py)

### 48 [QTableView](./48-QTableView)

0. [QTableView-表格视图.md](./48-QTableView/00-QTableView-表格视图.md)

### 49 [QTreeView](./49-QTreeView)

0. [QTreeView-树视图.md](./49-QTreeView/00-QTreeView-树视图.md)

### 50 [QTabWidget](./50-QTabWidget)

0. [QTabWidget-标签页控件.md](./50-QTabWidget/00-QTabWidget-标签页控件.md)
1. [QTabWidget-创建、父控件关系、标签位置、标签形状.py](./50-QTabWidget/01-QTabWidget-创建、父控件关系、标签位置、标签形状.py)
2. [QTabWidget-可移动、可关闭、自动隐藏页签、文档模式.py](./50-QTabWidget/02-QTabWidget-可移动、可关闭、自动隐藏页签、文档模式.py)
3. [QTabWidget-设置图标、图标尺寸、省略号模式、按钮滚动.py](./50-QTabWidget/03-QTabWidget-设置图标、图标尺寸、省略号模式、按钮滚动.py)
4. [QTabWidget-移除页、页不可用、清空页.py](./50-QTabWidget/04-QTabWidget-移除页、页不可用、清空页.py)
5. [QTabWidget-信号.py](./50-QTabWidget/05-QTabWidget-信号.py)

### 51 [QStackedWidget](./51-QStackedWidget)

0. [QStackedWidget-堆载窗口控件.md](./51-QStackedWidget/00-QStackedWidget-堆载窗口控件.md)

### 52 [QListWidget](./52-QListWidget)

0. [QListWidget-列表控件.md](./52-QListWidget/00-QListWidget-列表控件.md)

### 53 [QUndoView](./53-QUndoView)

0. [QUndoView-撤销视图控件.md](./53-QUndoView/00-QUndoView-撤销视图控件.md)

### 54 [QHeaderView](./54-QHeaderView)

0. [QHeaderView-表头视图.md](./54-QHeaderView/00-QHeaderView-表头视图.md)

共54个目录，249个文件。

代码行数统计工具: github.com/AlDanial/cloc v1.92

| Language |    files |    blank |  comment |     code |
|:---------|---------:|---------:|---------:|---------:|
| Python   |      202 |     2139 |     1539 |     5336 |
| Markdown |       51 |     1403 |        0 |     2274 |
| -------- | -------- | -------- | -------- | -------- |
| SUM:     |      253 |     3542 |     1539 |     7610 |

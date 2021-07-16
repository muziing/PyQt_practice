# Qt Style Sheets 样式表

> 暂时偷了个懒，直接把我的博客 [使用QSS美化PyQt5界面 - muzing的杂货铺](https://muzing.top/posts/28a1d80f/) 转载过来了，后面可能会更新QSS语法详解

QSS 全称 Qt Style Sheets（Qt样式表），用于美化Qt程序界面，类似于CSS，但不如CSS强大，只能简单美化。



## 官方文档

[Customizing Qt Widgets Using Style Sheets](https://doc.qt.io/qt-5/stylesheet-customizing.html)

[Qt Style Sheets Reference](https://doc.qt.io/qt-5/stylesheet-reference.html)

官方参考文档才是最官方全面的文档，有时间最好仔细阅读一下。

主要包括：

- 可应用样式表的控件列表
- 属性列表
- 图标列表
- 属性值列表
- 伪类选择器列表
- 子控件控制列表

内容非常多，在此就不展开了。



## 基本语法

类似CSS，QSS每一条都是由一个选择器和一组声明构成：

选择器选出要对哪种控件进行样式修改，

每个声明都是键值对，键为属性，值为属性值

![QSS语法](https://oss.muzing.top/image/QSS_eg.png)



## 使用方式

为降低耦合，往往把QSS写在一个单独的style.qss文件中，然后在main.py的QApplication或QMainWindow中加载样式



### 编写QSS

新建一个扩展名为`.qss`的文件，如style.qss，编辑内容。（本文后面有完整的样式主题、QSS编辑器推荐）

把写好的.qss添加到qrc中



### 加载QSS

创建一个加载QSS样式表的公共类：

```python
class QSSLoader:
    def __init__(self):
        pass

    @staticmethod
    def read_qss_file(qss_file_name):
        with open(qss_file_name, 'r',  encoding='UTF-8') as file:
            return file.read()
```



在代码中加载qss样式表：

```python
app = QApplication(sys.argv)
window = MainWindow()
 
style_file = './style.qss'
style_sheet = QSSLoader.read_qss_file(style_file)
window.setStyleSheet(style_sheet)

window.show()
sys.exit(app.exec_())
```



## QSS 样式分享

### Qt 官方例子

[Qt Style Sheets Examples](https://doc.qt.io/qt-5/stylesheet-examples.html)

Qt官方给出的一些小例子，不一定好看但有很强的学习参考性



### Qt-Material

[UN-GCPDS/qt-material](https://github.com/UN-GCPDS/qt-material)

> This is another stylesheet for **PySide6**, **PySide2** and **PyQt5**, which looks like Material Design (close enough).

“一个仿Material的样式，适用于PySide6, PySide2以及PyQt5”



![浅色主题演示](https://oss.muzing.top/image/Qt-Material-light.gif)



![深色主题演示](https://oss.muzing.top/image/Qt-Material-dark.gif)



使用这套样式表也非常简单，作者已经打包发布到了pypi，所以我们只需要

```shell
pip install qt-material
```

安装，并在代码中import即可

```python
# 使用例子
import sys
# from PySide6 import QtWidgets
# from PySide2 import QtWidgets
from PyQt5 import QtWidgets
from qt_material import apply_stylesheet

# create the application and the main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# setup stylesheet
apply_stylesheet(app, theme='dark_teal.xml')

# run
window.show()
app.exec_()
```

更多详细内容请查阅[该项目的README](https://github.com/UN-GCPDS/qt-material/blob/master/README.md)



### QDarkStyleSheet

> The most complete dark/light style sheet for Qt applications

“最完整的深色/浅色Qt主题”

- [文档](https://qdarkstylesheet.readthedocs.io/)

- [GitHub](https://github.com/ColinDuquesnoy/QDarkStyleSheet)



![containers_no_tabs_buttons](https://oss.muzing.top/image/qdarkstylesheet-containers_no_tabs_buttons.png)

![containers_no_tabs_buttons1](https://oss.muzing.top/image/qdarkstylesheet-containers_no_tabs_buttons1.png)

![containers_tabs_displays](https://oss.muzing.top/image/qdarkstylesheet-containers_tabs_displays.png)

![widgets_inputs_fields1](https://oss.muzing.top/image/qdarkstylesheet-widgets_inputs_fields1.png)



也可以通过pip直接安装使用

```shell
pip install qdarkstyle
```

```python
# PyQt5 使用例子
import sys
import qdarkstyle
from PyQt5 import QtWidgets

# create the application and the main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# setup stylesheet
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
# or in new API
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

# run
window.show()
app.exec_()
```



### 飞扬青云-QSS

在飞扬青云的 [QWidgetDemo](https://github.com/feiyangqingyun/QWidgetDemo) 项目中的 [styledemo](https://github.com/feiyangqingyun/QWidgetDemo/tree/master/styledemo) 子项目包含了3套很好看的QSS样式

![PS黑色](https://oss.muzing.top/image/feiyangqingyun_styledemo_psblack.png)

![浅蓝色](https://oss.muzing.top/image/feiyangqingyun_styledemo_lightblue.png)

![扁平化白色](https://oss.muzing.top/image/feiyangqingyun_styledemo_flatwhite.png)

[QSS目录链接](https://github.com/feiyangqingyun/QWidgetDemo/tree/master/styledemo/other)



## QSS 编辑器

如果对上面推荐的这几个主题还不满意，你可以设计自己的QSS，下面推荐一些专用编辑器



### QssStylesheetEditor

[GitHub首页](https://github.com/hustlei/QssStylesheetEditor)

[中文README](https://github.com/hustlei/QssStylesheetEditor/blob/master/readme_zh-CN.md)

> QssStylesheetEditor 是一个功能强大的 Qt 样式表(QSS)编辑器，支持实时预览，自动提示，自定义变量, 支持预览自定义ui代码，引用QPalette等功能。



![程序主界面](https://oss.muzing.top/image/QssStylesheetEditor_GUI(v1.7).png)

这个软件有如下特点：

- Qss代码高亮，代码折叠
- Qss代码自动提示，自动补全
- 实时预览 Qss 样式效果，可以预览几乎所有的 qtwidget 控件效果
- 支持预览自定义界面代码
- 支持在 Qss 中自定义变量
- 自定义变量可以在颜色对话框中拾取变量的颜色
- 支持通过颜色对话框改变QPalette，并在Qss中引用
- 支持相对路径引用图片，以及引用资源文件中的图片
- 支持切换不同的系统 theme，如 xp 主题，vista 主题等(不同 theme 下 qss 效果会略有差异)
- 能够在 windows，linux，unix 上运行
- 支持多国语言（目前已有中文，英文，俄文翻译）

还有许多强大而实用的功能，可以在[README](https://github.com/hustlei/QssStylesheetEditor/blob/master/readme_zh-CN.md)中查看



### QSS Editor

> 🎨 Cross-platform application to edit and preview Qt style sheets (QSS).

跨平台的QSS编辑/预览应用

[GitHub主页](https://github.com/HappySeaFox/qsseditor)

[GitHub realeases](https://github.com/HappySeaFox/qsseditor/releases)

[下载地址2](https://sourceforge.net/projects/qsseditor/)

![qsseditor-1](https://oss.muzing.top/image/qsseditor-1.png)

![qsseditor-2.png](https://oss.muzing.top/image/qsseditor-2.png)



### Pycharm、VScode 插件

在Pycharm中可以安装 [Qt Style Sheet Highlighter](https://plugins.jetbrains.com/plugin/13963-qt-style-sheet-highlighter) 插件，提供对QSS的代码高亮功能

![Qt Style Sheet Highlighter](https://oss.muzing.top/image/20210716085119.png)

![Qt Style Sheet Highlighter 演示](https://oss.muzing.top/image/qss-highlighter-screen-plugin-screen.gif)





在VScode里可以安装[Qt for Python](https://marketplace.visualstudio.com/items?itemName=seanwu.vscode-qt-for-python) 插件，该插件不仅支持qss文件的代码高亮，还支持qml、qrc、pro等代码的高亮

![Qt for Python](https://oss.muzing.top/image/20210714180428.png)


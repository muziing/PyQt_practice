# QMainWindow

Qt 主程序窗口框架，用于构建用户窗口界面。

QMainWindow有自己的布局，可以添加 [QToolBar](https://doc.qt.io/qt-5.15/qtoolbar.html) 工具栏、[QDockWidget](https://doc.qt.io/qt-5.15/qdockwidget.html) 浮动控件、 [QMenuBar](https://doc.qt.io/qt-5.15/qmenubar.html) 菜单栏、
[QStatusBar](https://doc.qt.io/qt-5.15/qstatusbar.html) 状态栏，以及中心控件

![QMainWindowLayout](https://oss.muzing.top/image/QMainWindowLayout.png)


## Qt 官方文档

[Qt 5.15官方文档-QMainWindow](https://doc.qt.io/qt-5.15/qmainwindow.html)



## 属性设置方法



### Menu Bar 菜单栏

> setMenuBar(QMenuBar **menuBar*)

把*menuBar*设置为主窗口的菜单栏

注意:QMainWindow获取菜单栏指针的所有权，并在适当的时候删除它。



### Toolbars 工具栏



> setIconSize(QSize &*iconSize*)

设置工具栏图标尺寸。默认的工具栏图标尺寸由 GUI Style确定。注意设置的图标尺寸只能小于原始图片尺寸（只能缩小不能放大显示）



### Dock Widgets 停靠控件

将在[QDockWidget](../45-QDockWidget/00-QDockWidget-浮动停靠控件.md)中详细说明



### StatusBar 状态栏



### 其他

> setTabShape(QTabWidget.TabShape *tabShape*)



## Public Slots 槽函数

| 槽函数                                     | 说明                                          | 备注 |
| ------------------------------------------ | --------------------------------------------- | ---- |
| setAnimated(bool *enabled*)                | 停靠部件和工具栏停靠时是否有动画              |      |
| setDockNestingEnabled(bool *enabled*)      | 设置停靠部件是否可以嵌套                      |      |
| setUnifiedTitleAndToolBarOnMac(bool *set*) | 设置窗口是否使用macOS上统一的标题和工具栏外观 |      |



## Signals 信号

| 信号                                                         | 说明                                                         | 备注                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| iconSizeChanged(QSize &*iconSize*)                           | 当窗口中使用的图标的大小改变时，就会发出这个信号。新的图标大小在iconSize中传递 | 您可以将此信号连接到其他组件，以帮助维护应用程序的外观一致性 |
| tabifiedDockWidgetActivated(QDockWidget **dockWidget*)       | 通过当通过选择选项卡激活tabified dock小部件时，就会发出这个信号；激活的停靠部件作为dockWidget参数传出 |                                                              |
| toolButtonStyleChanged(Qt.ToolButtonStyle *toolButtonStyle*) | 当窗口中工具按钮使用的样式发生更改时，将发出此信号；新的样式作为toolButtonStyle参数传出 | 您可以将此信号连接到其他组件，以帮助维护应用程序的外观一致性 |


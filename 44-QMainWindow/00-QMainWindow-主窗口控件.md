# QMainWindow

Qt 主程序窗口框架，用于构建用户窗口界面。

QMainWindow有自己的布局，可以添加 
- [QToolBar](https://doc.qt.io/qt-5.15/qtoolbar.html) 工具栏
- [QDockWidget](https://doc.qt.io/qt-5.15/qdockwidget.html) 浮动停靠控件
-  [QMenuBar](https://doc.qt.io/qt-5.15/qmenubar.html) 菜单栏
- [QStatusBar](https://doc.qt.io/qt-5.15/qstatusbar.html) 状态栏
- Central Widget 中心控件

![QMainWindowLayout](https://oss.muzing.top/image/QMainWindowLayout.png)



## Qt 官方文档

[Qt 5.15官方文档-QMainWindow](https://doc.qt.io/qt-5.15/qmainwindow.html)



## 属性设置方法



### Menu Bar 菜单栏

[查看代码](./02-QMainWindow-QMenuBar-菜单栏.py)

> QMainWindow.setMenuBar(QMenuBar **menuBar*)

把*menuBar*设置为主窗口的菜单栏

注意:QMainWindow获取菜单栏指针的所有权，并在适当的时候删除它



> QMainWindow.setMenuWidget(QWidget **menuBar*)

注意:QMainWindow获取菜单栏指针的所有权，并在适当的时候删除它

--------

以下内容为 [QMenuBar](https://doc.qt.io/qt-5.15/qmenubar.html) 的属性方法

> QMenuBar.addAction(str &*text*)
>
> QMenuBar.addAction(str &*text*, QObject **receiver*, str *member*)
>
> QMenuBar.addAction(str &*text*, Functor *functor*)

菜单栏添加 Action



> QMenuBar.addMenu(QMenu **menu*)
>
> QMenuBar.addMenu(str &*title*)
>
> QMenuBar.addMenu(QIcon &*icon*, str &*title*)
>
> QMenuBar.insertMenu(QAction * *before*, QMenu **menu*)

菜单栏添加菜单



> QMenuBar.addSeparator()
>
> QMenuBar.insertSeparator(QAction **before*)

菜单栏添加分割线



> setNativeMenuBar(bool *nativeMenuBar*)
>
> isNativeMenuBar() -> bool

对于macOS、Ubuntu等操作系统，通过这个方法可以指定使用操作系统提供的菜单栏，对于不支持的平台则该方法无效



**QMenuBar Signal 信号**

| 信号                         | 说明                                                         | 备注                                                 |
| ---------------------------- | ------------------------------------------------------------ | ---------------------------------------------------- |
| hovered(QAction **action*)   | 当一个菜单栏的action被高亮时发送此信号，*action* 作为参数传出 | 经常被用来更新状态栏信息                             |
| triggered(QAction **action*) | 鼠标单击触发菜单栏中的action时发送此信号，*action* 作为参数传出 | 在需要将多个项目连接到同一个槽的时候，适合使用此信号 |



### Toolbars 工具栏

[查看代码](./03-QMainWindow-QToolBar-工具栏.py)

> setIconSize(QSize &*iconSize*)

设置工具栏图标尺寸。默认的工具栏图标尺寸由 GUI Style确定。注意设置的图标尺寸只能小于原始图片尺寸（只能缩小不能放大显示）



> setToolButtonStyle(Qt.ToolButtonStyle *toolButtonStyle*)

设置工具栏按钮风格。默认值为 Qt.ToolButtonIconOnly。若想跟随系统设置，只需设置为 Qt.ToolButtonFollowStyle



> addToolBar(Qt.ToolBarArea *area*, QToolBar **toolbar*)
>
> addToolBar(QToolBar **toolbar*)
>
> addToolBar(str &*title*)

添加一个工具栏



> addToolBarBreak(Qt.ToolBarArea *area*=Qt.TopToolBarArea)
>
> insertToolBarBreak(QToolBar **before*)

添加/插入分割线



> removeToolBar(QToolBar **toolbar*)

从主窗口布局中移除工具栏并隐藏它，注意*toolbar*并没有被删除



> removeToolBarBreak(QToolBar **before*)

移除 *before* 前面的分割线



> toolBarBreak(QToolBar **toolbar*) -> bool

返回在 *toolbar* 前面是否有工具栏分割线



### Dock Widgets 浮动停靠控件

将在[QDockWidget](../45-QDockWidget/00-QDockWidget-浮动停靠控件.md)中详细说明



### StatusBar 状态栏

[查看代码](./04-QMainWindow-QStatusBar-状态栏.py)

> setStatusBar(QStatusBar **statusbar*)

将*statusbar*设置为主窗口的状态栏



> statusBar() -> QStatusBar

返回主窗口的状态栏

-------------

以下为 [QStatusBar](https://doc.qt.io/qt-5.15/qstatusbar.html) 的方法属性

>setSizeGripEnabled(*bool*)
>
>isSizeGripEnabled() -> bool

状态栏右下角的 SizeGrip 是否启用，默认启用



> currentMessage()
>
> clearMessage()
>
> showMessage(str &*message*, int *timeout* = 0)



### Central Widget 中央控件

> setCentralWidget(QWidget **widget*)

将给定的 *widget* 设置为主窗口的中央控件

注意:QMainWindow获取 *widget* 指针的所有权，并在适当的时候删除它



> takeCentralWidget()

从主窗口中移除中央控件

被移除的控件所有权转移到此函数的调用方



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


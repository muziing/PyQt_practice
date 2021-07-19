# QDockWidget

> The QDockWidget class provides a widget that can be docked inside a QMainWindow or floated as a top-level window on the desktop.

提供一种可以停靠在QMainWindow内或作为独立窗口浮在桌面的控件

![MainWindow-docks](https://oss.muzing.top/image/Qt-mainwindow-docks.png)

## Qt官方文档

[Qt 5.15官方文档-QDockWidget](https://doc.qt.io/qt-5.15/qdockwidget.html)

## 常用方法


| QDockWidget.DockWidgetFeatures | 值   | 描述                                                         |
| ------------------------------ | ---- | ------------------------------------------------------------ |
| DockWidgetClosable             |      | 可以关闭dock控件。在某些系统（如MacOS 10.5）上，dock控件在浮动时总有一个关闭按钮 |
| DockWidgetMovable              |      | 用户可以控制dock控件在码头间移动                             |
| DockWidgetFloatable            |      | dock控件可以与主窗口分离，并作为独立窗口浮动                 |
| DockWidgetVerticalTitleBar     |      | dock控件在其左侧显示一个垂直标题栏。这可以用来增加QMainWindow中的垂直空间 |
| AllDockWidgetFeatures          |      | （已弃用）dock控件可以关闭、浮动、移动。请勿使用此属性。     |
| NoDockWidgetFeatures           |      | dock控件不能被关闭、移动、浮动                               |



## Signals 信号

| 信号                                                       | 说明                                                         | 备注                                                         |
| ---------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| allowedAreasChanged(Qt.DockWidgetAreas *allowedAreas*)     | 当allowedAreas属性改变时发送此信号，新的allowedAreas作为参数传出 |                                                              |
| dockLocationChanged(Qt.DockWidgetArea *area*)              | 当停靠小部件移动到另一个停靠区域，或移动到当前停靠区域中的不同位置时，将发送此信号 | 用户移动或代码控制均会触发                                   |
| featuresChanged(QDockWidget.DockWidgetFeatures *features*) | 当features属性改变时，就会发出这个信号，新的features作为参数传出 |                                                              |
| topLevelChanged(bool *topLevel*)                           | 当浮动属性改变时发送此信号，如果dock控件现在是浮动的，则*topLevel*参数为True，否则为False |                                                              |
| visibilityChanged(bool *visible*)                          | 当dock控件变为可见(或不可见)时，将发出此信号             | 当控件被隐藏或显示时，以及当它停靠在选项卡停靠区域并且它的选项卡被选中或取消选中时，都会触发 |

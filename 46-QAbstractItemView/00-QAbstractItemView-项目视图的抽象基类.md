# QAbstractItemView

继承自[QAbstractScrollArea](../12-QAbstractScrollArea/00-QAbstractScrollArea-滚动区域的低级抽象.md)

提供项目视图（item view）的基本方法

QAbstractItemView是所有的使用QAbstractItemModel模型的视图的基类，是一个不能被实例化的抽象类。它通过信号槽机制为与模型的交互操作提供了一个标准化的接口，确保子类视图能够随着模型的变化而及时更新。该类对键盘和鼠标的导航、视窗的滚动、项的编辑以及选择提供了标准的支持。

## Qt 官方文档

[Qt 5.15-官方文档-QAbstractItemView](https://doc.qt.io/qt-5.15/qabstractitemview.html)

## model/View 模型视图

在Qt中使用**model/View**结构来管理数据与视图的关系，**model**负责数据的存取，数据的交互通过**delegate**来实现

分享一篇我找到的博客：[PyQt(Python+Qt)入门学习：Model/View架构详解](https://blog.csdn.net/LaoYuanPython/article/details/104064757) （利益无关）

## 常用方法

设置方法

| 方法                                                         | 描述                             | 说明                                  |
| ------------------------------------------------------------ | -------------------------------- | ------------------------------------- |
| setModel(QAbstractItemModel, **model*)                       | 为视图设置模型以供展示           | 设置新的model之后，旧的不会被自动删除 |
| setTabKeyNavigation(bool *enable*)                           | 是否支持tab键和(shift+tab)的导航 |                                       |
| setSelectionBehavior(QAbstractItemView.SelectionBehavior *behavior*) | 选择模式                         | 见下方SelectionBehavior表格           |
| setVerticalScrollMode(QAbstractItemView.ScrollMode *mode*)   | 垂直滚动模式                     | 见下方ScrollMode表格                  |
| setDragDropMode(QAbstractItemView.DragDropMode *behavior*)   | 设置拖放模式                     | 见下方DragDropMode表格                |
|                                                              |                                  |                                       |
|                                                              |                                  |                                       |
|                                                              |                                  |                                       |
| setTextElideMode(Qt.TextElideMode *mode*)                    | 省略号在文本中出现的位置         | 默认值为右侧                          |
|                                                              |                                  |                                       |
|                                                              |                                  |                                       |

### SelectionBehavior 选择模式

| QAbstractItemView.SelectionBehavior | 值   | 描述         |
| ----------------------------------- | ---- | ------------ |
| QAbstractItemView.SelectItems       | 0    | 选中单个项目 |
| QAbstractItemView.SelectRows        | 1    | 选中行       |
| QAbstractItemView.SelectColumns     | 2    | 选中列       |



### ScrollMode 滚动模式

| QAbstractItemView.ScrollMode | 描述                   |
| ---------------------------- | ---------------------- |
| ScrollPerItem                | 一次滚动一个项目的内容 |
| ScrollPerPixel               | 一次滚动一个像素的内容 |

### DragDropMode 拖拽模式

| QAbstractItemView.DragDropMode | 值   | 描述                                         |
| ------------------------------ | ---- | -------------------------------------------- |
| NoDragDrop                     | 0    | 不支持拖拽放置                               |
| DragOnly                       | 1    | 该视图支持拖拽自己的项目                     |
| DropOnly                       | 2    | 接受丢弃                                     |
| DragDrop                       | 3    | 支持拖放                                     |
| InternalMove                   | 4    | 该视图只接受来自其自身的移动（不是复制）操作 |



## 常用 Model

### [QStringListModel](https://doc.qt.io/qt-5.15/qstringlistmodel.html)

### [QStandardItemModel](https://doc.qt.io/qt-5.15/qstandarditemmodel.html)

### [QFileSystemModel](https://doc.qt.io/qt-5.15/qfilesystemmodel.html)




# QAbstractItemView

继承自[QAbstractScrollArea](../12-QAbstractScrollArea/00-QAbstractScrollArea-滚动区域的低级抽象.md)

提供项目视图（item view）的基本方法

QAbstractItemView是所有的使用QAbstractItemModel模型的视图的基类，是一个不能被实例化的抽象类。它通过信号槽机制为与模型的交互操作提供了一个标准化的接口，确保子类视图能够随着模型的变化而及时更新。该类对键盘和鼠标的导航、视窗的滚动、项的编辑以及选择提供了标准的支持。

## Qt 官方文档

[Qt 5.15-官方文档-QAbstractItemView](https://doc.qt.io/qt-5.15/qabstractitemview.html)

## model/View 模型视图

在Qt中使用**model/View**结构来管理数据与视图的关系，**model**负责数据的存取，数据的交互通过**delegate**来实现

分享一篇我找到的博客：[PyQt(Python+Qt)入门学习：Model/View架构详解](https://blog.csdn.net/LaoYuanPython/article/details/104064757) （利益无关）

![Model/View架构模型](https://oss.muzing.top/image/2020011610050834.png)

- Model 模型与数据源通信，为体系结构中的其他组件提供数据接口
- View 视图从模型Model中根据一定条件（如行号、列号等）获取模型索引，模型索引是一个指向数据项的引用。通过模型Model的模型索引，视图View可以从数据源检索数据项。
- Delegate 代理在标准视图中展现数据项，编辑项时，代理Delegate直接使用模型索引与模型Model通信。

## 属性设置方法

### 滚动控制类属性

| 方法                                                         | 描述                                                         | 说明                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------- |
| setAutoScroll(bool *enable*)                                 | 设置是否开启自动滚动：如果用户在视口边缘的 16 像素内拖动，QAbstractItemView 会自动滚动视图的内容、果当前项发生变化，则视图将自动滚动以确保当前项完全可见 | 默认为True           |
| setAutoScrollMargin(int *margin*)                            | 设置自动滚动触发的范围，单位是像素                           | 默认值为16           |
| setVerticalScrollMode(QAbstractItemView.ScrollMode *mode*)   | 垂直滚动模式                                                 | 见下方ScrollMode表格 |
| setHorizontalScrollMode(QAbstractItemView.ScrollMode *mode*) | 水平滚动模式                                                 | 见下方ScrollMode表格 |

#### *ScrollMode 滚动模式*

| QAbstractItemView.ScrollMode | 描述                   |
| ---------------------------- | ---------------------- |
| ScrollPerItem                | 一次滚动一个项目的内容 |
| ScrollPerPixel               | 一次滚动一个像素的内容 |



--------

### 拖拽类属性

| 方法                                                       | 描述                                                         | 说明                   |
| ---------------------------------------------------------- | ------------------------------------------------------------ | ---------------------- |
| setDragEnabled(bool *enable*)                              | 此属性保存视图是否支持拖放它自己的项目                       |                        |
| setDragDropMode(QAbstractItemView.DragDropMode *behavior*) | 设置拖放模式                                                 | 见下方DragDropMode表格 |
| setDefaultDropAction(Qt.DropAction *dropAction*)           |                                                              |                        |
| setDragDropOverwriteMode(bool *overwrite*)                 |                                                              |                        |
| setShowDropIndicator(bool *enable*)                        | 用于控制在拖拽过程中显示当前拖拽到的位置，当释放时则在当前拖拽位置覆盖或插入 |                        |

#### *DragDropMode 拖拽模式*

| QAbstractItemView.DragDropMode | 值   | 描述                                         |
| ------------------------------ | ---- | -------------------------------------------- |
| NoDragDrop                     | 0    | 不支持拖拽放置                               |
| DragOnly                       | 1    | 该视图支持拖拽自己的项目                     |
| DropOnly                       | 2    | 接受丢弃                                     |
| DragDrop                       | 3    | 支持拖放                                     |
| InternalMove                   | 4    | 该视图只接受来自其自身的移动（不是复制）操作 |

-----

### 选择类属性

| 方法                                                         | 说明     | 备注                        |
| ------------------------------------------------------------ | -------- | --------------------------- |
| selectionMode                                                |          |                             |
| setSelectionBehavior(QAbstractItemView.SelectionBehavior *behavior*) | 选择模式 | 见下方SelectionBehavior表格 |


#### *SelectionBehavior 选择模式*

| QAbstractItemView.SelectionBehavior | 值   | 描述         |
| ----------------------------------- | ---- | ------------ |
| QAbstractItemView.SelectItems       | 0    | 选中单个项目 |
| QAbstractItemView.SelectRows        | 1    | 选中行       |
| QAbstractItemView.SelectColumns     | 2    | 选中列       |



-----------

### 编辑及数据呈现控制属性

| 方法                                      | 说明                             | 备注         |
| ----------------------------------------- | -------------------------------- | ------------ |
| editTriggers                              |                                  |              |
| setTabKeyNavigation(bool *enable*)        | 是否支持tab键和(shift+tab)的导航 |              |
| setTextElideMode(Qt.TextElideMode *mode*) | 省略号在文本中出现的位置         | 默认值为右侧 |
| setIconSize(QSize &*size*)                | 设置图标尺寸                     |              |




## Public Slots 槽函数

| 槽函数                                | 说明                                         | 备注                                                         |
| ------------------------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| clearSelection()                      | 取消选择所有选定项                           | 当前索引不改变                                               |
| edit(QModelIndex &*index*)            | 开始编辑与给定索引对应的项(如果它是可编辑的) | 注意此函数不会改变当前索引，用户可能会发现键盘导航异常。请在调用此函数前调用setCurrentIndex() |
| reset()                               | 重置视图内部状态                             | 已经做出的修改将不会被保存。如想在重置时commit修改，请重新实现此方法：先commit修改，然后调用超类 |
| scrollToBottom()                      | 滚动到视图底部                               |                                                              |
| scrollToTop()                         | 滚动到视图顶部                               |                                                              |
| selectAll()                           | 选择视图内的全部项目                         |                                                              |
| setCurrentIndex(QModelIndex &*index*) | 将当前项设置为*index*处的项目                | 除非当前选择模式为NoSelection，否则项目也会同时被选中        |
| setRootIndex(QModelIndex &*index*)    | 设置给定的*index*为根项目                    |                                                              |
| update(QModelIndex &*index*)          | 更新给定*index*所占用的区域                  |                                                              |



## Signals 信号

| 信号                                  | 说明                                                     | 备注                           |
| ------------------------------------- | -------------------------------------------------------- | ------------------------------ |
| activated(QModelIndex &*index*)       |                                                          |                                |
| clicked(QModelIndex &*index*)         | 当鼠标左键单击时发送此信号，点击的项目的索引作为参数传出 | 只有索引有效时才发送           |
| doubleClicked(QModelIndex &*index*)   | 鼠标双击时发送此信号，点击的项目的索引作为参数传出       | 只有索引有效时才发送           |
| entered(QModelIndex &*index*)         | 当鼠标光标进入项目时发送此信号，项目索引作为参数传出     | 需要开启鼠标跟踪才能使用       |
| iconSizeChanged(QModelIndex &*index*) | 项目图标尺寸改变时传出此信号                             |                                |
| pressed(QModelIndex &*index*)         | 鼠标按键按下时发送此信号，项目索引作为参数传出           | 索引有效时才发送               |
| viewportEntered()                     | 当鼠标光标进入时发送此信号                               | 需要开启鼠标跟踪才能使用此功能 |



## 常用 Model

### [QStringListModel](https://doc.qt.io/qt-5.15/qstringlistmodel.html)

用于存储str字符串项的简单列表

### [QStandardItemModel](https://doc.qt.io/qt-5.15/qstandarditemmodel.html)

管理更复杂的项树结构，每个项都可以包含任意数据

### [QFileSystemModel](https://doc.qt.io/qt-5.15/qfilesystemmodel.html)

提供有关本地文件系统中的文件和目录的信息


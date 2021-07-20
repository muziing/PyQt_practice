# QTableView

继承自[QAbstractItemView](../46-QAbstractItemView/00-QAbstractItemView-项目视图的抽象基类.md)

实现了一个表格视图，用以显示数据模型中的项目。

![QTableview](https://oss.muzing.top/image/Qt-windows-tableview.png)

QTabView类是 [Model/View 类](https://doc.qt.io/qt-5.15/model-view-programming.html#model-view-classes) 之一，也是 Qt的 [model/view 框架](https://doc.qt.io/qt-5.15/model-view-programming.html) 的一部分

关于Model/View，可以参考我的博客：[PyQt中的 Model/View 结构 - muzing的杂货铺](https://muzing.top/posts/5ff61cbd/)

### 导航

可以通过鼠标点击单元格或使用键盘方向键来导航表格中的单元格。因为QTabView默认启用[tabKeyNavigation](https://doc.qt.io/qt-5.15/qabstractitemview.html#tabKeyNavigation-prop) ，所以也可以使用Tab和BackTab(Shift + Tab) 来从一个单元格移动到另一个。



### 视觉外观

表头控件为 [QHeaderView](../54-QHeaderView/00-QHeaderView-表头视图.md)

该表有一个垂直表头，可以使用verticalHeader()方法获得；一个水平表头，可以通过horizontalHeader() 方法获得。可以使用rowHeight() 来获得表中每一行的行高；类似地，可以使用columnWidth()来获得列的列宽。由于这两个表头控件都是普通控件，您可以使用它们的hide() 方法隐藏它们中的任何一个。

行和列可以通过hideRow() 、hideColumn() 、showRow()和showColumn() 来隐藏和显示。它们可以通过selectRow() 和selectColumn()进行选择。根据showGrid属性，该表将显示一个网格。

表视图中显示的项与其他项视图中的项一样，使用标准**代理**呈现和编辑。但是，对于某些任务，有时能够在表中插入控件是有用的。控件是通过setIndexWidget()方法为特定的索引设置的，然后通过indexWidget()检索。

![QTableView-resized](https://oss.muzing.top/image/Qt-qtableview-resized.png)

默认情况下，表中的单元格不会展开以填充可用空间。您可以通过拉伸最后一个标题部分使单元格填充可用空间。使用horizontalHeader() 或 verticalHeader() 访问相关的表头，并设置表头的stretchLastSection属性。要根据每个列或行的空间需求分配可用空间，请调用视图的 resizeColumnsToContents() 或 resizeRowsToContents() 方法。

### 坐标系统

对于某些特殊形式的表，能够在行和列索引和控件坐标之间进行转换是很有用的。下文有对应实现两种坐标系之间转换的方法函数详解。



## Qt 官方文档

[Qt 5.15 官方文档-QTableView](https://doc.qt.io/qt-5.15/qtableview.html)



## 单元格与表头设置方法

| 方法                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| setVerticalHeader(QHeaderView **header*)                     | 将*header*设置为将要用于垂直表头的控件                       |
| setHorizontalHeader(QHeaderView **header*)                   | 将*header*设置为将要用于水平表头的控件                       |
| setRowHeight(int *row*, int *height*)                        | 将*row*行的行高设置为*height*                                |
| setColumnWidth(int *column*, int *width*)                    | 将*column*列的列宽设置为*width*                              |
| setSpan(int *row*, int *column*, int *rowSpanCount*, int *columnSpanCount*) | 将表元素(*row*, *column*)的跨度设置为(*rowSpanCount*, *columnSpanCount*)指定的行数和列数 |
| clearSpans()                                                 | 移除所有跨度                                                 |

## 单元格与表头获取方法

| 方法                                | 返回值类型  | 说明                                    | 备注      |
| ----------------------------------- | ----------- | --------------------------------------- | --------- |
| columnSpan(int *row*, int *column*) | int         | 返回表元素在(*row*, *column*)处的列跨度 | 默认值为1 |
| rowSpan(int *row*, int *column*)    | int         | 返回表元素在(*row*, *column*)处的行跨度 | 默认值为1 |
| columnWidth(int *column*)           | int         | 返回给定列的宽度                        |           |
| rowHeight(int *row*)                | int         | 返回给定行的高度                        |           |
| verticalHeader()                    | QHeaderView | 返回垂直表头控件                        |           |
| horizontalHeader()                  | QHeaderView | 返回水平表头控件                        |           |


## 属性设置方法

| 方法                                  | 说明                           | 备注                                                         |
| ------------------------------------- | ------------------------------ | ------------------------------------------------------------ |
| setCornerButtonEnabled(bool *enable*) | 控制左上角的全选按钮是否启用   | 默认为True；点击左上角按钮将选中表格视图中的所有单元格       |
| setWordWrap(bool *on*)                | 设置项目文本的单词自动换行策略 | 如果开启了自动换行，单元格将不会为了适应全部长度的文本而扩大，而是根据textElideMode策略在文本中添加省略号 |
| setSortingEnabled(bool *enable*)      | 设置是否开启排序               | 默认为False；此属性设置为True则立即触发对sortByColumn()的调用 |
| setShowGrid(bool *show*)              | 设置是否显示网格               | 默认为True                                                   |
| setGridStyle(Qt.PenStyle *style*)     | 设置绘制网格的画笔风格         |                                                              |

## 坐标系转换

| 方法                                        | 说明                    | 备注                                 |
| ------------------------------------------- | ----------------------- | ------------------------------------ |
| columnAt(int *x*) -> int                    | 返回给定的x坐标所在的列 | 如果给定的坐标无效(没有列)，则返回-1 |
| rowAt(int *y*) -> int                       | 返回给定的y坐标所在的行 | 如果给定的坐标无效(没有行)，则返回-1 |
| columnViewportPosition(int *column*) -> int | 返回给定列对应的x坐标   |                                      |
| rowViewportPosition(int *row*) -> int       | 返回给定行对应的y坐标   |                                      |



## Public Slots 槽函数

| 槽函数                                           | 说明                                                     | 备注                                                   |
| ------------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------ |
| hideColumn(int *column*)                         | 隐藏指定列                                               |                                                        |
| hideRow(int *row*)                               | 隐藏指定行                                               |                                                        |
| showColumn(int *column*)                         | 显示指定列                                               |                                                        |
| showRow(int *row*)                               | 显示指定行                                               |                                                        |
| resizeColumnToContents(int *column*)             | 根据用于呈现列中每个项目的代理的大小提示调整给定列的大小 | 只有可见列的大小将被调整                               |
| resizeColumnsToContents()                        | 根据用于呈现列中每个项目的代理的大小提示调整所有列的大小 |                                                        |
| resizeRowToContents(int *row*)                   | 根据用于呈现行中每个项目的代理的大小提示调整给定行的大小 |                                                        |
| resizeRowsToContents()                           | 根据用于呈现行中每个项目的代理的大小提示调整所有行的大小 |                                                        |
| selectColumn(int *column*)                       | 选定指定列                                               | 只有当前的SelectionMode和SelectionBehavior允许时才选中 |
| selectRow(int *row*)                             | 选定指定行                                               | 只有当前的SelectionMode和SelectionBehavior允许时才选中 |
| setShowGrid(bool *show*)                         | 设置是否绘制网格                                         |                                                        |
| sortByColumn(int *column*, Qt.SortOrder *order*) | 根据给定的*order*排序列                                  | 并非所有模型都支持，有些情况下可能会崩溃               |


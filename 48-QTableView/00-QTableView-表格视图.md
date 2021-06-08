# QTableView

继承自[QAbstractItemView](../46-QAbstractItemView/00-QAbstractItemView-项目视图的抽象基类.md)

实现了一个表格视图，用以显示数据模型中的项目。

## Qt 官方文档

[Qt 5.15 官方文档-QTableView](https://doc.qt.io/qt-5.15/qtableview.html)



## 常用设置方法

| 方法                                  | 简介                           | 说明                                                         |
| ------------------------------------- | ------------------------------ | ------------------------------------------------------------ |
| setCornerButtonEnabled(bool *enable*) | 控制左上角的全选按钮是否启用   | 默认为True；点击左上角按钮将选中表格视图中的所有单元格       |
| setWordWrap(bool *on*)                | 设置项目文本的单词自动换行策略 | 如果开启了自动换行，单元格将不会为了适应全部长度的文本而扩大，而是根据textElideMode策略在文本中添加省略号 |
| setSortingEnabled(bool *enable*)      | 设置是否开启排序               | 默认为False；此属性设置为True则立即触发对sortByColumn()的调用 |
| setShowGrid(bool *show*)              | 设置是否显示网格               | 默认为True                                                   |
| setGridStyle(Qt.PenStyle *style*)     | 设置绘制网格的画笔风格         |                                                              |



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


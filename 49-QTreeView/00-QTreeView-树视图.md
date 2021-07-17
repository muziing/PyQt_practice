# QTreeView

继承自[QAbstractItemView](../46-QAbstractItemView/00-QAbstractItemView-项目视图的抽象基类.md)



## Qt 官方文档

[Qt 5.15 官方文档-QTreeView](https://doc.qt.io/qt-5.15/qtreeview.html)



## Public Slots 槽函数

| 槽函数                                                     | 说明                                                         | 备注                                                         |
| ---------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| collapse(QModelIndex &*index*)                             | 折叠*index*指定的项目                                        |                                                              |
| collapseAll()                                              | 折叠所有已经展开的项目                                       |                                                              |
| expand(QModelIndex &*index*)                               | 展开*index*指定的项目                                        |                                                              |
| expandAll()                                                | 展开所有可展开的项目                                         |                                                              |
| expandRecursively(QModelIndex &*index*, int *depth* = -1) | 将给定索引处的项及其所有子项展开为给定深度。深度是相对于给定的索引 | -1表示展开所有深度的子项；0表示只扩展给定的索引；当模型中包含的项目非常多时，执行此方法将花费较长时间 |
| expandToDepth(int *depth*)                                 | 把所有项目展开到给定深度                                     |                                                              |
| hideColumn(int *column*)                                   | 隐藏给定的列                                                 | 只能在模型初始化（已知模型列数）之后调用                     |
| resizeColumnToContents(int *column*)                       | 根据列的内容调整列的大小                                     |                                                              |
| showColumn(int *column*)                                   | 显示给定的列                                                 |                                                              |
| sortByColumn(int *column*, Qt.SortOrder *order*)           | 根据给定的列和*order*为模型排序                              | Column可以为-1，在这种情况下，将不显示排序指示符，模型将返回其自然的、未排序的顺序。注意，并不是所有的模型都支持这一点，在这种情况下甚至可能崩溃。 |



## Signals 信号

| 信号                            | 说明                                | 备注 |
| ------------------------------- | ----------------------------------- | ---- |
| collapsed(QModelIndex &*index*) | 当*index*指定的项被折叠时发送此信号 |      |
| expanded(QModelIndex &*index*)  | 当展开*index*位置的项时发送此信号   |      |


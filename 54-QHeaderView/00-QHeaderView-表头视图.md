# QHeaderView

继承自 [QAbstractItemView](../46-QAbstractItemView/00-QAbstractItemView-项目视图的抽象基类.md)

为项目视图提供标题行或标题列

## Qt 官方文档

[Qt 5.15-官方文档-QHeaderView](https://doc.qt.io/qt-5.15/qheaderview.html)



| QHeaderView.ResizeMode | 值   | 描述                                                         |
| ---------------------- | ---- | ------------------------------------------------------------ |
| Interactive            | 0    | 用户可以调整section的大小。也可以使用resizeSection()以代码方式调整section的大小。section大小默认为defaultSectionSize |
| Fixed                  | 2    | 用户不能调整section的大小。section只能使用resizeSection()代码方式调整大小。section大小默认为defaultSectionSize |
| Stretch                | 1    | 将自动调整section的大小以填充可用空间。该大小不能由用户或编程方式更改 |
| ResizeToContents       | 3    | 根据整个列或行的内容自动调整section的大小到其最佳大小。该大小不能由用户或编程方式更改 |



## Signals 信号

| 信号                                                         | 说明                                 | 备注 |
| ------------------------------------------------------------ | ------------------------------------ | ---- |
| geometriesChanged()                                          | 当表头的几何形状发生改变时发送此信号 |      |
| sectionClicked(int *logicalIndex*)                           |                                      |      |
| sectionCountChanged(int *oldCount*, int *newCount*)          |                                      |      |
| sectionDoubleClicked(int *logicalIndex*)                     |                                      |      |
| sectionEntered(int *logicalIndex*)                           |                                      |      |
| sectionHandleDoubleClicked(int *logicalIndex*)               |                                      |      |
| sectionMoved(int *logicalIndex*, int *oldVisualIndex*, int *newVisualIndex*) |                                      |      |
| sectionPressed(int *logicalIndex*)                           |                                      |      |
| sectionResized(int *logicalIndex*, int *oldSize*, int *newSize*) |                                      |      |
| sortIndicatorChanged(int *logicalIndex*, Qt.SortOrder *order*) |                                      |      |


# QHeaderView

继承自 [QAbstractItemView](../46-QAbstractItemView/00-QAbstractItemView-项目视图的抽象基类.md)

为项目视图提供标题行或标题列



QHeaderView 类是 [Model/View 类](https://doc.qt.io/qt-5.15/model-view-programming.html#model-view-classes) 之一，也是 Qt的 [model/view 框架](https://doc.qt.io/qt-5.15/model-view-programming.html) 的一部分。

> 关于Model/View，可以参考我的博客：[PyQt中的 Model/View 结构 - muzing的杂货铺](https://muzing.top/posts/5ff61cbd/)

表头使用 QAbstractItemModel::headerData() 函数从模型中获取每个部分的数据。您可以使用 QAbstractItemModel::setHeaderData() 设置数据。

每个标题都有一个orientation() 和一些由count() 函数给出的节。节是指标题的一部分 - 行或列，具体取决于方向。

可以使用 moveSection() 和 resizeSection() 移动和调整节的大小；它们也可以使用 hideSection() 和 showSection() 隐藏和显示。

标题的每个部分都由部分 ID 描述，由其 section() 指定，并且可以位于标题中的特定 visualIndex() 处。一个节可以有一个使用 setSortIndicator() 设置的排序指示器；这指示关联的项目视图中的项目是否将按照部分给定的顺序进行排序。

对于水平标题，该部分相当于模型中的一列；对于垂直标题，该部分相当于模型中的一行。



## Qt 官方文档

[Qt 5.15-官方文档-QHeaderView](https://doc.qt.io/qt-5.15/qheaderview.html)



## 常用方法

| QHeaderView.ResizeMode | 值   | 描述                                                         |
| ---------------------- | ---- | ------------------------------------------------------------ |
| Interactive            | 0    | 用户可以调整节的大小。也可以使用resizeSection()以代码方式调整节的大小。section大小默认为defaultSectionSize |
| Fixed                  | 2    | 用户不能调整节的大小。节只能使用resizeSection()代码方式调整大小。节大小默认为defaultSectionSize |
| Stretch                | 1    | 将自动调整节的大小以填充可用空间。该大小不能由用户或编程方式更改 |
| ResizeToContents       | 3    | 根据整个列或行的内容自动调整节的大小到其最佳大小。该大小不能由用户或编程方式更改 |



## Signals 信号

| 信号                                                         | 说明                                                         | 备注                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------- |
| geometriesChanged()                                          | 当表头的几何形状发生改变时发送此信号                         |                            |
| sectionClicked(int *logicalIndex*)                           | 单击某个节时发送此信号，该节的逻辑索引作为参数传出           | sectionPressed信号也将发送 |
| sectionCountChanged(int *oldCount*, int *newCount*)          | 当节的数量发生变化（添加或删除节）时发送此信号，原先的节数量和新的节数量作为参数传出 |                            |
| sectionDoubleClicked(int *logicalIndex*)                     | 当一个节被双击时发送此信号，该节的逻辑索引作为参数传出       |                            |
| sectionEntered(int *logicalIndex*)                           | 当光标移动到节并按下鼠标左键时将发送此信号，该节的逻辑索引作为参数传出 |                            |
| sectionHandleDoubleClicked(int *logicalIndex*)               | 双击某个节时发送此信号，该节的逻辑索引作为参数传出           |                            |
| sectionMoved(int *logicalIndex*, int *oldVisualIndex*, int *newVisualIndex*) | 当一个节被移动时发送此信号。参数中传出该节的逻辑索引、旧的视觉索引、新的视觉索引 |                            |
| sectionPressed(int *logicalIndex*)                           | 当一个节被按下时发送此信号，该节的逻辑索引作为参数传出       |                            |
| sectionResized(int *logicalIndex*, int *oldSize*, int *newSize*) | 当一个节被调整大小时发送此信号。参数中传出该节的逻辑索引、旧尺寸、新尺寸 |                            |
| sortIndicatorChanged(int *logicalIndex*, Qt.SortOrder *order*) | 当包含排序指示符或指示的顺序的部分发生更改时，会发出此信号。 节的逻辑索引由 *logicalIndex* 指定，排序顺序由 *order* 指定 |                            |


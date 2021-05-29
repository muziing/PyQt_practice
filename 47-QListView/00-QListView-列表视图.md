# QListView

继承自[QAbstractItemView](../46-QAbstractItemView/00-QAbstractItemView-项目视图的抽象基类.md)

QListView 列表视图表示存储在模型 model 中的项，可以是一个简单的非层次列表，也可以是一组图标。

这个视图不提供水平或垂直的表头；如果需要显示带有水平表头的列表项目，请使用[QTreeView](../49-QTreeView/00-QTreeView-树视图.md)

列表视图中的项目可以使用两种视图模式之一显示：在 **ListMode** 中，项目以简单列表的形式显示； 在 **IconMode** 中，列表视图采用图标视图的形式，其中项目与文件管理器中的文件等图标一起显示。 默认情况下，列表视图处于 ListMode。 要更改视图模式，请使用 setViewMode() 函数，而要确定当前的视图模式，请使用 viewMode()。



## Qt 官方文档

[Qt 5.15-官方文档-QListView](https://doc.qt.io/qt-5.15/qlistview.html)



## 常用方法



| 方法                                       | 说明                                   | 备注 |
| ------------------------------------------ | -------------------------------------- | ---- |
| setFlow(QListView.Flow *flow*)             | 设置显示项目的方向，从左到右or从上到下 |      |
| setLayoutMode(QListView.LayoutMode *mode*) | 设置布局模式                           |      |
|                                            |                                        |      |
|                                            |                                        |      |
|                                            |                                        |      |
|                                            |                                        |      |
|                                            |                                        |      |
|                                            |                                        |      |



### Flow 列表方向

| QListView.Flow        | 值   | 描述                     |
| --------------------- | ---- | ------------------------ |
| QListView.LeftToRight | 0    | 项目在视图中从左至右排列 |
| QListView.TopToButtom | 1    | 项目在视图中从上至下排列 |


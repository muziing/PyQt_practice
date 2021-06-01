# QListView

继承自[QAbstractItemView](../46-QAbstractItemView/00-QAbstractItemView-项目视图的抽象基类.md)

QListView 列表视图表示存储在模型 model 中的项，可以是一个简单的非层次列表，也可以是一组图标。

这个视图不提供水平或垂直的表头；如果需要显示带有水平表头的列表项目，请使用[QTreeView](../49-QTreeView/00-QTreeView-树视图.md)

列表视图中的项目可以使用两种视图模式之一显示：在 **ListMode** 中，项目以简单列表的形式显示； 在 **IconMode** 中，列表视图采用图标视图的形式，其中项目与文件管理器中的文件等图标一起显示。 默认情况下，列表视图处于 ListMode。 要更改视图模式，请使用 setViewMode() 函数，而要确定当前的视图模式，请使用 viewMode()。



## Qt 官方文档

[Qt 5.15-官方文档-QListView](https://doc.qt.io/qt-5.15/qlistview.html)



## 常用方法

设置方法

| 方法                                       | 说明                                             | 备注                                                         |
| ------------------------------------------ | ------------------------------------------------ | ------------------------------------------------------------ |
| setFlow(QListView.Flow *flow*)             | 设置显示项目的方向，从左到右or从上到下           | 见下方Flow表格                                               |
| setLayoutMode(QListView.LayoutMode *mode*) | 设置布局模式                                     | 见下方LayoutMode表格                                         |
| setViewMode(QListView.ViewMode *mode*)     | 设置视图模式                                     | 见下方ViewMode表格                                           |
| setBatchSize(int *batchSize*)              | 设置每批中的项目数量                             | 默认值100；仅在LayoutMode为Batched时才有效                   |
| setWrapping(bool *enable*)                 | 是否启动自动换行                                 |                                                              |
| setItemAlignment(Qt.Alignment *alignment*) | 设置每一项在单元格内的对齐方式                   | 只有在ListMode为TopToBottom且wrapping打开时才有效            |
| setResizeMode(QListView.ResizeMode *mode*) | 设置Resize模式，即视图大小改变时项目是否重新布局 | 默认为Fixed；见下方ResizeMode表格                            |
| setMovement(QListView.Movement *movement*) | 设置项目可以自由移动/捕获到网格/不能移动         | 见下方Movement表格                                           |
| setGridSize(QSize &*size*)                 | 设置布局网格的尺寸                               | 默认为空尺寸，即不在网格中布局；将此属性设置为非空大小会打开网格布局；（当网格布局生效时，间距spacing属性将被忽略） |
| setSpacing(int *space*)                    | 设置项目在布局中的间距                           | 默认值为0；修改此值会导致重新布局                            |
| setWordWrap                                | 设置单词自动换行功能                             | 默认为False；即使启用换行，单元格也不会扩展为文本腾出空间。 根据视图的 textElideMode，它将为无法显示的文本打印省略号 |



### Flow 列表方向

| QListView.Flow        | 值   | 描述                     |
| --------------------- | ---- | ------------------------ |
| QListView.LeftToRight | 0    | 项目在视图中从左至右排列 |
| QListView.TopToBottom | 1    | 项目在视图中从上至下排列 |



### LayoutMode 布局模式

| QListView.LayoutMode | 值   | 描述                                        |
| -------------------- | ---- | ------------------------------------------- |
| QListView.SinglePass | 0    | 一次性列出所有项目                          |
| QListView.Batched    | 1    | 分批列出，每批列出的项目个数由batchSize设置 |



### ViewMode 视图模式

相当于一次性设置了flow, size, movement三个属性

| QListView.ViewMode | 值   | 描述                                             |
| ------------------ | ---- | ------------------------------------------------ |
| QListView.ListMode | 0    | flow: TopToButtom, size: Small, movement: Static |
| QListView.IconMode | 1    | flow: LeftToRight, size: Large, movement: Free   |



### ResizeMode 大小调整模式

| QListView.ResizeMode | 值   | 描述                               |
| -------------------- | ---- | ---------------------------------- |
| QListView.Fixed      | 0    | 项目只会在视图第一次显示时进行布局 |
| QListView.Adjust     | 1    | 每次视图大小改变时，项目都重新布局 |



### Movement 移动

| QListView.Movement | 值   | 描述                                          |
| ------------------ | ---- | --------------------------------------------- |
| QListView.Static   | 0    | 用户不能移动项目                              |
| QListView.Free     | 1    | 用户可以自由移动项目                          |
| QListView.Snap     | 2    | 项目在移动时对齐到指定的网格；见setGridSize() |



## Signals 信号

| 信号                                     | 说明                           | 备注 |
| ---------------------------------------- | ------------------------------ | ---- |
| indexesMoved(QModelIndexList &*indexes*) | 当视图中的索引移动时发出此信号 |      |




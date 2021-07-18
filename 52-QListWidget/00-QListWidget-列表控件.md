# QListView

继承自 [QListView](../47-QListView/00-QListView-列表视图.md)

基于Item项目的列表控件 （QListView则是基于Model模型的）

## Qt 官方文档

[Qt 5.15-官方文档-QListWidget](https://doc.qt.io/qt-5.15/qlistwidget.html)



## Public Slots 槽函数

| 槽函数                                                       | 说明                                                         | 备注                           |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------ |
| clear()                                                      | 移除视图中所有的项目和选择                                   | **警告**：所有项目将被永久删除 |
| scrollToItem(QListWidgetItem **item*, QAbstractItemView.ScrollHint *hint* = EnsureVisible) | 必要时滚动视图，以确保项可见，*hint*指定操作后*item*项目位于何处 |                                |



## Signal 信号

| 信号                                                         | 说明                                                         | 备注                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| currentItemChanged(QListWidgetItem **current* , QListWidgetItem * *previous*) | 当当前项目改变时发送此信号，*previous*是之前获得焦点的项，*current*则是新的当前项目 |                                                              |
| currentRowChanged(int *currentRow*)                          | 当前项发生改变时发送此信号。*currentRow*是当前项目的行       | 如果没有当前项目，则*currentRow*为-1                         |
| currentTextChanged(str &*currentText*)                       | 当前项目发生更改时发送此信号。*currentText*为当前项中的文本数据 | 如果没有当前项，则*currentText*无效                          |
| itemActivated(QListWidgetItem **item*)                       | 项目被激活时发送此信号。当用户单击或双击该项目时，该项目被激活，取决于系统配置。 | 用户按下激活键（对于Windows和X11是回车键，在Mac OS X上是Command+O）时也有效 |
| itemChanged(QListWidgetItem **item*)                         | 当项目的数据发生变化时发送此信号                             |                                                              |
| itemClicked(QListWidgetItem **item*)                         | 当鼠标单击控件中的某个项目时，发送此信号，该项目作为参数传出 |                                                              |
| itemDoubleClicked(QListWidgetItem **item*)                   | 当鼠标双击控件中的某个项目时，发送此信号，该项目作为参数传出 |                                                              |
| itemEntered(QListWidgetItem **item*)                         | 当鼠标光标进入一个项目时，发送此信号，该项目作为参数传出     | 只有当mouseTracking打开，或鼠标按键按下时光标移入一个项目时才有效 |
| itemPressed(QListWidgetItem **item*)                         | 鼠标按键在一个项目上按下时发送此信号，该项目作为参数传出     |                                                              |
| itemSelectionChanged()                                       | 每当选择变化时，发送此信号                                   |                                                              |


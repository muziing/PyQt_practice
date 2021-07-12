# QStackedWidget

继承自[QFrame](../11-QFrame/00-QFrame-框架控件的基类.md)

一组堆叠在一起的控件，每次只有其中一个可见

基于 [QStackedLayout](https://doc.qt.io/qt-5.15/qstackedlayout.html)

## Qt 官方文档

[Qt 5.15 官方文档-QStackedWidget](https://doc.qt.io/qt-5.15/qstackedwidget.html)



## 常用方法

> count() -> int

返回stacked widget控件包含的控件数



> currentIndex() -> int
>
> setCurrentIndex(int *index*)

当前显示页的索引值。如果没有当前页则为-1



> addWidget(QWidget **widget*)
>
> insertWidget(int *index*, QWidget **widget*)
>
> removeWidget(QWidget **widget*)

添加、插入、删除控件



> indexOf(QWidget **widget*) -> int

返回指定控件的索引值



## Public Slots 槽函数

| 槽函数                              | 说明 | 备注 |
| ----------------------------------- | ---- | ---- |
| setCurrentIndex(int *index*)         | 把位于*index*的控件设置为当前控件 |      |
| setCurrentWidget(QWidget **widget*) | 把*widget*控件设置为当前控件 |      |



## Signals 信号

| 信号                        | 说明                                                     | 备注 |
| --------------------------- | -------------------------------------------------------- | ---- |
| currentChanged(int *index*) | 当前控件改变时发送此信号，新的当前控件的索引作为参数传出 |      |
| widgetRemoved(int *index*)  | 删除控件时会发送此信号，被删除的控件的索引作为参数传出   |      |


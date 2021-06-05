# QAbstractScrollArea

继承自[QFrame](../11-QFrame/00-QFrame-框架控件的基类.md)

> The QAbstractScrollArea widget provides a scrolling area with on-demand scroll bars.

QAbstractScrollArea提供了一个带有滚动条的滚动区域。该区域提供了一个称为视口（viewport）的中央小部件，在其中滚动区域的内容（即，内容的可见部分在视口中呈现）。



## Qt官方文档

[Qt 5.15 官方文档-QAbstractScrollArea](https://doc.qt.io/qt-5.15/qabstractscrollarea.html)



## Qt.ScrollBarPolicy 滚动条策略

> setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy)
>
> setVerticalScrollBarPolicy(Qt.ScrollBarPolicy)

| Qt.ScrollBarPolicy    | 值   | 描述                                                   |
| --------------------- | ---- | ------------------------------------------------------ |
| Qt.ScrollBarAsNeeded  | 0    | 按需出现滚动条，只有在内容超出可视区域时才出现；默认值 |
| Qt.ScrollBarAlwaysOff | 1    | 从不显示滚动条                                         |
| Qt.ScrollBarAlwaysOn  | 2    | 总是显示一个滚动条                                     |



## SizeAdjustPolicy 尺寸调整策略

> setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy *policy*)

| QAbstractScrollArea.SizeAdjustPolicy            | 值   | 描述                               |
| ----------------------------------------------- | ---- | ---------------------------------- |
| QAbstractScrollArea.AdjustIgnored               | 0    | 不做任何调整；默认值               |
| QAbstractScrollArea.AdjustToContents            | 2    | 滚动区域将始终调整到适应视口       |
| QAbstractScrollArea.AdjustToContentsOnFirstShow | 1    | 只在第一次显示时调整尺寸至适应视口 |


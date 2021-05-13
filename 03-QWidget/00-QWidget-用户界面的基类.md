# QWidget

> The QWidget class is the base class of all user interface objects. 

所有GUI控件的基类

## Qt官方文档

[Qt 5.15官方文档-QWidget](https://doc.qt.io/qt-5.15/qwidget.html)



## 模态窗口

https://doc.qt.io/qt-5.15/qwidget.html#windowModality-prop

模态窗口可以阻塞用户对其他窗口的输入

更多内容可参考[QDialog](../29-QDialog/00-QDialog-对话框窗口基类.md)

## 槽函数

## 信号

| 信号                                      | 说明                           | 注释                        |
| ----------------------------------------- | ------------------------------ | --------------------------- |
| customContextMenuRequested(QPoint &*pos*) |                                |                             |
| windowIconChanged(QIcon &*icon*)          | 当窗口图标发生改变时发送此信号 | 新的*icon*图标作为参数传出  |
| windowTitleChanged(str &*title*)          | 当窗口标题发生变化时发送此信号 | 新的*title*标题作为参数传出 |


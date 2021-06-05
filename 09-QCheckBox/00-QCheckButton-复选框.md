# QCheckButton

继承自 [QAbstractButton](../04-QAbstractButton/00-QAbstractButton-按钮的抽象基类.md)

> The QCheckBox widget provides a checkbox with a text label. 

带有文本标签的复选框

## Qt官方文档

[Qt 5.15 官方文档-QCheckbutton](https://doc.qt.io/qt-5.15/qcheckbox.html)

## 常用方法

[查看代码](./01-QCheckBox-功能使用.py)

> setTristate(bool *y* = true)
>
> isTristate() -> bool

是否开启三态，即是否允许“部分选中”状态

> setCheckState(Qt.CheckState *state*)

通过代码设置 CheckBox 的选中状态

## Qt.CheckState

[查看代码](./01-QCheckBox-功能使用.py)

部分选中需要 CheckButton 已经开启了 Tristate

| Qt.CheckState       | 值   | 描述     |
| ------------------- | ---- | -------- |
| Qt.Unchecked        | 0    | 未选中   |
| Qt.PartiallyChecked | 1    | 部分选中 |
| Qt.Checked          | 2    | 选中     |



## Signals 信号

[查看代码](./02-QCheckBox-信号.py)

| 信号                      | 描述                                                 | 备注 |
| ------------------------- | ---------------------------------------------------- | ---- |
| stateChanged(int *state*) | 当选中状态发生改变时发送此信号，新的状态作为参数传出 |      |


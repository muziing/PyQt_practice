# QSpinBox

继承自[QAbstractSpinBox](../16-QAbstractSpinBox/00-QAbstractSpinBox-数字设定框的抽象基类.md)



## Qt官方文档

[Qt 5.15 官方文档-QSpinBox](https://doc.qt.io/qt-5.15/qspinbox.html)



## 槽函数

| 槽函数     | 说明               | 备注                                            |
| ---------- | ------------------ | ----------------------------------------------- |
| setValue() | 设置spin box中的值 | 若新设置的值与旧值不同，则触发valueChange()信号 |



## 信号

| 信号                     | 说明                        | 备注                       |
| ------------------------ | --------------------------- | -------------------------- |
| textChanged(str &*text*) | spin box中的text改变时发送  | 传出信号中的text包含前后缀 |
| valueChanged(int *i*)    | spin box中的value改变时发送 | 新的value在i中传出         |


# QComboBox

QComboBox 是下拉列表框控件，提供一个下拉列表供用户选择，也可以直接当作一个QLineEdit用于字符串输入。
QComboBox除了显示可见下拉列表外，每个项（item，或称列表项）还可以关联一个QVariant类型的用户数据，用于存储一些在列表中不可见的数据

## Qt官方文档

[Qt 5.15官方文档-QComboBox](https://doc.qt.io/qt-5.15/qcombobox.html)

## 槽函数

| 槽函数                       | 说明 | 备注 |
| ---------------------------- | ---- | ---- |
| clear()                      |      |      |
| clearEditText()              |      |      |
| setCurrentIndex(int *index*) |      |      |
| setCurrentText(str &*text*)  |      |      |
| setEditText(str &*text*)     |      |      |



## 信号

| 信号                             | 说明 | 备注 |
| -------------------------------- | ---- | ---- |
| activated(int *index*)           |      |      |
| currentIndexChanged(int *index*) |      |      |
| currentTextChanged(str &*text*)  |      |      |
| editTextChanged(str &*text*)     |      |      |
| highlighted(int *index*)         |      |      |
| textActivated(str &*text*)       |      |      |
| textHighlighted(str &*text*)     |      |      |


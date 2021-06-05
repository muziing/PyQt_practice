# QComboBox

QComboBox 是组合下拉框控件，提供一个下拉列表供用户选择，也可以直接当作一个QLineEdit用于字符串输入。
QComboBox除了显示可见下拉列表外，每个项（item，或称列表项）还可以关联一个QVariant类型的用户数据，用于存储一些在列表中不可见的数据

## Qt官方文档

[Qt 5.15官方文档-QComboBox](https://doc.qt.io/qt-5.15/qcombobox.html)



## 常用方法

### 添加与插入项目

> addItem()
>
> addItems()



> setDuplicatesEnabled(bool *enable*)
>
> duplicatesEnabled() -> bool

控制是否允许用户添加多个相同（重复）的项。

注意通过代码添加项目时，始终可以添加多个相同的项



### 获取

> currentIndex() -> int
>
> currentText() -> str
>
> currentData(int *role* = Qt.UserRole) -> QVariant





> count() -> int

此方法返回组合框中的项目个数



### 显示

> setSizeAdjustPolicy()



[查看代码](./05-QComboBox-功能.py)



> setFrame(*bool*)

控制组合框是否有边框

[查看代码](./05-QComboBox-功能.py)



| QComboBox.SizeAdjustPolicy                      | 值                              | 描述                                                         |
| ----------------------------------------------- | ------------------------------- | ------------------------------------------------------------ |
| QComboBox.AdjustToContents                      | 0                               | 始终适应内容                                                 |
| QComboBox.AdjustToContentsOnFirstShow           | 1                               | 只在第一次显示时根据内容调整大小                             |
| QComboBox.AdjustToMinimumContentsLengthWithIcon | AdjustToContentsOnFirstShow + 2 | 将调整至最小内容长度加一个图标的大小；出于性能原因，请在大型模型上使用此策略 |



## Public Slots 槽函数

| 槽函数                       | 说明 | 备注 |
| ---------------------------- | ---- | ---- |
| clear()                      |      |      |
| clearEditText()              |      |      |
| setCurrentIndex(int *index*) |      |      |
| setCurrentText(str &*text*)  |      |      |
| setEditText(str &*text*)     |      |      |



## Signals 信号

[查看代码](./06-QComboBox-信号.py)

| 信号                             | 说明                                                         | 备注                                                         |
| -------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| activated(int *index*)           | 用户在组合框中选择一个项目时就会发送此信号，选中项目的索引作为参数传出 | 即使选择没有更改，也会发送                                   |
| currentIndexChanged(int *index*) | 当前选中的索引发生变化（用户选择或代码调用）时发送此信号，索引作为参数传出 | 如果组合框变空或者 currentIndex 被重置，则 *index* 为pass或-1 |
| currentTextChanged(str &*text*)  | 当前选中的文本发生变化时发送此信号，新的文本作为参数传出     |                                                              |
| editTextChanged(str &*text*)     | 当ComboBox中的LineEdit改变时发送此信号                       |                                                              |
| highlighted(int *index*)         | 当组合框中的项目被用户高亮时发送此信号                       |                                                              |
| textActivated(str &*text*)       | 用户在组合框中选择一个项目时发送此信号                       | 即使选择没有改变，也会发送                                   |
| textHighlighted(str &*text*)     | 用户高亮了组合框弹出列表中的项目时发送此信号                 |                                                              |


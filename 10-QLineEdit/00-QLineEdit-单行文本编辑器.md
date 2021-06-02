# QLineEdit

单行文本编辑器。只能输入一行内容无法换行。

## Qt官方文档

[Qt 5.15 官方文档-QLineEdit ](https://doc.qt.io/qt-5.15/qlineedit.html)



## 属性设置与获取方法

### 外观对齐类

> setAlignment([Qt.Alignment](https://doc.qt.io/qt-5.15/qt.html#AlignmentFlag-enum) *flag*)
>
> alignment() -> Qt.Alignment

Alignment 对齐方式

默认垂直居中靠左对齐



### 字符显示类

> setEchoMode(QLineEdit.EchoMode)
>
> displayText() -> str

EchoMode 显示模式

对于获取用户密码等场景，我们需要让line edit不显示实际输入的字符，而是显示*之类的密码掩码，这时候就需要设置 Echomode。也可以通过 displayText() 方法获取显示的文本

| QLineEdit.EchoMode           | 值   | 描述                                                         |
| ---------------------------- | ---- | ------------------------------------------------------------ |
| QLineEdit.Normal             | 0    | 默认值；显示原始字符                                         |
| QLineEdit.NoEcho             | 1    | 什么都不显示；常用于密码位数都保密的场景，类似Linux登录密码那样 |
| QLineEdit.Password           | 2    | 显示平台定义的密码掩码而不是实际输入的字符                   |
| QLineEdit.PasswordEchoOnEdit | 3    | 编辑时显示字符，否则与Password相同                           |





### 动作类

> setClearButtonEnabled(bool *enable*)

ClearButtonEnabled 清除按钮启用



> setDragEnabled(bool *b*)

默认禁用拖拽；设置是否启用拖拽



### 光标类

> setCursorMoveStyle(Qt.CursorMoveStyle *style*)

提供了两种风格

- Qt.VisualMoveStyle ：与视觉一致；不论文字书写方向如何，按键盘方向左键则向左移动光标
- Qt.LogicMoveStyle ：与逻辑一致；对于从左向右的文本块，按键盘方向左键则增加光标位置，对于从右向左的文本块则相反；默认值



> setCursorPosition(*int*)
>
> cursorPosition() -> int

设置当前光标位置，默认值为0

## Public Slots 槽函数

| 槽函数      | 说明                         | 备注                                                         |
| ----------- | ---------------------------- | ------------------------------------------------------------ |
| clear()     | 清空LineEdit内的文本         |                                                              |
| copy()      | 将选定文本复制到剪贴板       | 选中了文本、echoMode()为Normal时才有效                       |
| cut()       | 将选定文本剪切到剪贴板       | echoMode()为Normal；如果验证器不允许删除当前文本，则仅复制   |
| paste()     | 将剪贴板内容粘贴进LineEdit   | 如果不满足验证器则无效                                       |
| redo()      | 重新执行上一个操作（重做）   |                                                              |
| selectAll() | 选择所有文本并将光标移至末尾 |                                                              |
| setText()   | 设置文本内容                 | 清除原有的选择、撤销重做记录；移动光标至末尾；太长的文本会被在maxLength处截断 |
| undo()      | 撤销                         | 取消当前选择，光标移至当前位置                               |



## Signals 信号

| 信号                                              | 说明                                     | 备注                                                         |
| ------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------ |
| textEdited(str *text*)                            | 文本内容被编辑时发送此信号               | 只有用户的操作才视为编辑，使用代码设置文本内容则不发送此信号 |
| textChanged(str *text*)                           | 文本内容改变时发送此信号                 | 使用代码改变文本也发送此信号                                 |
| selectionChanged()                                | 用户选择变化时发送此信号                 | 光标按下并有移动即触发，不是选中范围改变才触发               |
| cursorPositionChanged(int *oldPos*, int *newPos*) | 当光标移动时发射此信号，传出旧新光标位置 | pos为光标竖线右侧字符的位置数，从0开始                       |
| editingFinished()                                 | 用户结束编辑时发送此信号                 | 当QLineEdit失去焦点时则认为是结束编辑                        |
| inputRejected()                                   | 输入被拒绝时发送此信号                   | 用户输入不符合验证器或长度超过限制时发送此信号               |
| returnPressed()                                   | 按下Enter键发送的信号                    | 当设置了验证器或掩码时，只有验证器掩码通过后才发送此信号     |


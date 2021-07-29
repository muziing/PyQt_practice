# QLineEdit

单行文本编辑器。只能输入一行内容，无法换行。

![QLineEdit](https://oss.muzing.top/image/Qt-windows-lineedit.png)

如需要输入多行文本、富文本，请使用 [QTextEdit](../13-QTextEdit/00-QTextEdit-文本编辑器.md) 控件


## Qt官方文档

[Qt 5.15 官方文档-QLineEdit](https://doc.qt.io/qt-5.15/qlineedit.html)


## 属性设置与获取方法

### 外观对齐类

> setAlignment([Qt.Alignment](https://doc.qt.io/qt-5.15/qt.html#AlignmentFlag-enum) *flag*)
>
> alignment() -> Qt.Alignment

Alignment 对齐方式

[查看代码](./14-QLineEdit-对齐方式.py)

默认垂直居中靠左对齐

### 输入类

> setInputMask(str &*inputmask*)

掩码验证器

[查看代码](./10-QLineEdit-验证器-掩码.py)

关于掩码，请见下面的详细说明



> setmaxLength(*int*)
>
> maxLength() -> int

限制用户输入的最大长度

[查看代码](./08-QLineEdit-长度和只读限制.py)

### 字符显示类

> setPlaceholderText(str *&*)
>
> placeholderText() -> str

PlaceholderText 占位文本，即在用户输入内容之前显示在Line Edit中的文字。比如“请输入用户名”

[查看代码](./05-QLineEdit-占位文本设置、清空按钮.py)


> setEchoMode(QLineEdit.EchoMode)
>
> displayText() -> str

EchoMode 显示模式

[查看代码](./03-QLineEdit-文本输出模式.py)

对于获取用户密码等场景，我们需要让line edit不显示实际输入的字符，而是显示*之类的密码掩码，这时候就需要设置 Echomode。也可以通过 displayText() 方法获取显示的文本

| QLineEdit.EchoMode           | 值   | 描述                                                         |
| ---------------------------- | ---- | ------------------------------------------------------------ |
| QLineEdit.Normal             | 0    | 默认值；显示原始字符                                         |
| QLineEdit.NoEcho             | 1    | 什么都不显示；常用于密码位数都保密的场景，类似Linux登录密码那样 |
| QLineEdit.Password           | 2    | 显示平台定义的密码掩码而不是实际输入的字符                   |
| QLineEdit.PasswordEchoOnEdit | 3    | 编辑时显示字符，否则与Password相同                           |




### 动作类

> setClearButtonEnabled(bool *enable*)

ClearButtonEnabled 清空按钮

[查看代码](./05-QLineEdit-占位文本设置、清空按钮.py)

在编辑器内部最末尾位置添加一个清空按钮，只有在编辑器非空时才显示



> setDragEnabled(bool *b*)

是否启用拖拽

[查看代码](./15-QLineEdit-编辑功能.py)

默认禁用拖拽，即用户不能通过鼠标拖动改变Line Edit中的字符顺序



> setCompleter(QCompleter **c*)

自动补全，见下面的详细说明

[查看代码](./07-QLineEdit-自动补全.py)



### 光标类

> setCursorMoveStyle(Qt.CursorMoveStyle *style*)

提供了两种风格

- Qt.VisualMoveStyle ：与视觉一致；不论文字书写方向如何，按键盘方向左键则向左移动光标
- Qt.LogicMoveStyle ：与逻辑一致；对于从左向右的文本块，按键盘方向左键则增加光标位置，对于从右向左的文本块则相反；默认值



> setCursorPosition(*int*)
>
> cursorPosition() -> int

设置当前光标位置，默认值为0



## QCompleter 自动补全

[查看代码](./07-QLineEdit-自动补全.py)

可以创建一个 [QCompleter](https://doc.qt.io/qt-5.15/qcompleter.html) 填充器对象，来帮我们完成自动补全功能

## InputMask 掩码

详细见 [Qt文档-QLineEdit-InputMask](https://doc.qt.io/qt-5.15/qlineedit.html#inputMask-prop)



| 掩码字符 | 含义                              |
| -------- | --------------------------------- |
| A        | 必须为字母，如A-Z, a-z            |
| a        | 允许字母，非必须                  |
| N        | 必须为字母或数字，如A-Z, a-z, 0-9 |
| n        | 允许字母或数字，非必须            |
| X        | 允许任何字符，且必须              |
| x        | 允许任何字符，非必须              |
| 9        | 必须数字，即0-9                   |
| 0        | 允许数字0-9，非必需               |
| D        | 必须非零数字，即1-9               |
| d        | 允许非零数字1-9，非必需           |
| #        | 允许数字或加减号，非必须          |
| H        | 必须十六进制字符，即A-F, a-f, 0-9 |
| h        | 允许十六进制字符，非必需          |
| B        | 必须是二进制字符，即0-1           |
| b        | 允许二进制字符，非必须            |

| 元字符  | 含义                                                  |
| ------- | ----------------------------------------------------- |
| >       | 后面的字母字符全大写                                  |
| <       | 后面的字母字符全小写                                  |
| !       | 关闭大小写转换                                        |
| ;c      | 中止输入掩码并将 *blank* 字符设置为 c                 |
| [ ] { } | 保留                                                  |
| \       | 使用\对上面列出的特殊字符进行转义，以将它们用作分隔符 |



## Public Slots 槽函数

[查看代码](./15-QLineEdit-编辑功能.py)

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

[查看代码](./17-QLineEdit-信号.py)

| 信号                                              | 说明                                     | 备注                                                         |
| ------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------ |
| textEdited(str *text*)                            | 文本内容被编辑时发送此信号               | 只有用户的操作才视为编辑，使用代码设置文本内容则不发送此信号 |
| textChanged(str *text*)                           | 文本内容改变时发送此信号                 | 使用代码改变文本也发送此信号                                 |
| selectionChanged()                                | 用户选择变化时发送此信号                 | 光标按下并有移动即触发，不是选中范围改变才触发               |
| cursorPositionChanged(int *oldPos*, int *newPos*) | 当光标移动时发射此信号，传出旧新光标位置 | pos为光标竖线右侧字符的位置数，从0开始                       |
| editingFinished()                                 | 用户结束编辑时发送此信号                 | 当QLineEdit失去焦点时则认为是结束编辑                        |
| inputRejected()                                   | 输入被拒绝时发送此信号                   | 用户输入不符合验证器或长度超过限制时发送此信号               |
| returnPressed()                                   | 按下Enter键发送的信号                    | 当设置了验证器或掩码时，只有验证器掩码通过后才发送此信号     |


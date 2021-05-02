# QAbstractButton

按钮的抽象基类，常用按钮都是它的子类。本身不能被实例化，只有子类（例如，QPushButton）才能被实例化。

包含了按钮的基本功能，按钮按下、发射信号等等。



## [Qt官方文档-QAbstractButton](https://doc.qt.io/qt-5.15/qabstractbutton.html)



## 常用属性

| 属性名        | 数据类型     | 注释               |
| ------------- | ------------ | ------------------ |
| checkable     | bool         | 按钮是否可被选中   |
| checked       | bool         | 按钮是否已被选中   |
| down          | bool         | 按钮是否被按下     |
| icon          | QIcon        | 按钮上的图标       |
| text          | str          | 按钮上的文字       |
| shortcut      | QKeySequence | 设置按钮键盘快捷键 |
| autoExclusive | bool         | 自动排他性         |

## 常用方法

| 方法               | 返回值 | 说明                               |
| ------------------ | ------ | ---------------------------------- |
| setCheckable(bool) | None   | 设置按钮是否可被选中，默认为False  |
| setChecked(bool)   | None   | 设置按钮是否已经被选中（保持按下） |
|                    |        |                                    |



## 信号

| 信号                        | 说明                                                 |
| --------------------------- | ---------------------------------------------------- |
| checked(bool *checked=False*) | 按钮被单击（按下并释放）                             |
| pressed()                   | 按钮被按下                                           |
| released()                  | 按钮被释放                                           |
| toggle()                    | 按钮状态切换（仅限checkable button，下同）           |
| toggled(bool *checked*)     | 按钮状态切换，返回一个bool类型的变量表示切换后的状态 |


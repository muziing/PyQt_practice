# QAbstractButton

> The QAbstractButton class is the abstract base class of button widgets, providing functionality common to buttons. 

按钮的抽象基类，常用按钮都是它的子类。本身不能被实例化，只有子类（例如，QPushButton）才能被实例化。

包含了按钮的基本功能，按钮按下、发射信号等等。



## Qt官方文档

[Qt 5.15 官方文档-QAbstractButton](https://doc.qt.io/qt-5.15/qabstractbutton.html)

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

| 方法                         | 说明                                         | 备注                                       |
| ---------------------------- | -------------------------------------------- | -------------------------------------------- |
| setAutoExclusive(bool) | 是否启用自动排他性                 | 排他性详见[QRadioButton](../07-QRadioButton/00-QRadioButton-单选按钮.md) |
| setAutoRepeat(bool) | 设置是否开启自动重复 | 自动重复见文档后面部分 |
| setCheckable(bool)           | 设置按钮是否可被选中，默认为False            |             |
| setChecked(bool)             | 设置按钮是否已经被选中（保持按下）           |            |
| setDown(bool)                | 设置按钮按下 | 设置为True也不会触发pressed()或clicked()信号 |
| setIcon(QIcon &*icon*) | 为按钮设置图标 |                                              |
| setShortcut(QKeySequence &*key*) | 为按钮设置快捷键 |                                              |
| setText(str &*text*) | 为按钮设置文字 |                                              |

## Signals 信号

[查看代码](./07-QAbstractButton-可用信号.py)

| 信号                        | 说明                                                 |
| --------------------------- | ---------------------------------------------------- |
| checked(bool *checked*=False) | 按钮被单击（按下并释放）                             |
| pressed()                   | 按钮被按下                                           |
| released()                  | 按钮被释放                                           |
| toggle()                    | 按钮选中状态切换（仅限checkable button，下同）         |
| toggled(bool *checked*)     | 按钮状态切换，返回一个bool类型的变量表示切换后的状态 |

## Public Slots 槽函数

| 槽函数                         | 说明                                  | 备注                             |
| ------------------------------ | ------------------------------------- | -------------------------------- |
| animateClick(int *msec* = 100) | 执行单击动画                          | 所有与单击有关的信号都会适当发送 |
| click()                        | 执行一次单击                          | 所有与单击有关的信号都会适当发送 |
| toggle()                       | 切换checkable按钮的状态(切换选中状态) |                                  |



## AutoExclusive 自动排他性

[查看代码](./04-)

详见[QRadioButton](../07-QRadioButton/00-QRadioButton-单选按钮.md)

## AutoRepeat 自动重复

### 说明

> This property holds whether autoRepeat is enabled
>
> If autoRepeat is enabled, then the [pressed()](https://doc.qt.io/qt-5.15/qabstractbutton.html#pressed) , [released](https://doc.qt.io/qt-5.15/qabstractbutton.html#released) , and [clicked()](https://doc.qt.io/qt-5.15/qabstractbutton.html#clicked) signals are emitted at regular intervals when the button is down. autoRepeat is off by default. The initial delay and the repetition interval are defined in milliseconds by [autoRepeatDelay](https://doc.qt.io/qt-5.15/qabstractbutton.html#autoRepeatDelay-prop) and [autoRepeatInterval](https://doc.qt.io/qt-5.15/qabstractbutton.html#autoRepeatInterval-prop).
>
> Note: If a button is pressed down by a shortcut key, then auto-repeat is enabled and timed by the system and not by this class. The [pressed()](https://doc.qt.io/qt-5.15/qabstractbutton.html#pressed) , [released](https://doc.qt.io/qt-5.15/qabstractbutton.html#released) , and [clicked()](https://doc.qt.io/qt-5.15/qabstractbutton.html#clicked) signals will be emitted like in the normal case.



当按钮开启了AutoRepeat自动重复后，用户鼠标持续按住该按钮的情况下，按钮会自动重复发送pressed(), released(), clicked()信号

[AutoRepeatDelay](https://doc.qt.io/qt-5.15/qabstractbutton.html#autoRepeatDelay-prop) 表示从用户按下按钮，保持一定时间不释放，才开始自动重复。

[AutoRepeatInterval](https://doc.qt.io/qt-5.15/qabstractbutton.html#autoRepeatInterval-prop) 表示自动重复间隔时长，间隔时长越短则发送clicked()等信号的频率越高。

注意：如果按钮是被shortcut key键盘快捷键触发按下，则自动重复是由系统计时而非这个类

### 代码示例

见本仓库[代码例子](./02-QAbstractButton-功能测试.py)


### 设置方法

| 函数                          | 返回值 | 说明                       |
| ----------------------------- | ------ | -------------------------- |
| setAutoRepeat(bool)           | None   | 为按钮开启/关闭自动重复    |
| autoRepeat()                  | bool   | 按钮是否已经开启了自动重复 |
| setAutoRepeatDelay(int) | None   | 设置自动重复延时，单位是ms |
| autoRepeatDelay() | int | 获取自动重复延时，单位ms |
| setAutoRepeatInterval(int) | None | 设置自动重复间隔时长，单位ms |
| autoRepeatInterval() | int | 获取自动重复间隔时长 |
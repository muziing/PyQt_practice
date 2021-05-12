# QAbstractSpinBox

> The QAbstractSpinBox class provides a spinbox and a line edit to display values. 

数字设定框的抽象基类，包含一个spinbox（上下箭头）和一个line edit

## Qt官方文档

[Qt 5.15 官方文档-QAbstractSpinBox](https://doc.qt.io/qt-5.15/qabstractspinbox.html)



## 常用功能



### keyboardTracking 键盘跟踪

比如用户想要在QAbstractSpinBox中输入600，会在键盘上依次输入6, 0, 0：设置键盘跟踪为打开时（默认打开），则控件会发送value为6、60、600三次信号；反之，当键盘跟踪关闭，只有在用户结束编辑（焦点离开控件或按下Enter键）之后才发送一个value为600的信号。

| 方法                       | 说明                                     |
| -------------------------- | ---------------------------------------- |
| keyboardTracking() -> bool | 返回bool类型，表示当前是否打开了键盘跟踪 |
| setKeyboardTracking(bool)  | 打开或关闭键盘跟踪                       |



## 槽函数

| 槽函数      | 说明               | 备注                 |
| ----------- | ------------------ | -------------------- |
| clear()     | 清除所有行编辑内容 | 前后缀不会被清除     |
| selectAll() | 选择所有文本       | 前后缀不会被选中     |
| stepDown()  | 单步减小           | 类似于调用stepBy(-1) |
| stepUp()    | 单步增加           | 类似于调用stepBy(1)  |



## 信号

| 信号              | 说明                       | 备注                                        |
| ----------------- | -------------------------- | ------------------------------------------- |
| editingFinished() | 当用户编辑完成时发送此信号 | 控件失去焦点或用户按下Enter键，视为编辑完成 |


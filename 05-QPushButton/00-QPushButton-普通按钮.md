# QPushButton

普通按钮控件，常见于界面上的确定、应用、取消、是、否等按键。

> The push button, or command button, is perhaps the most commonly used widget in any graphical user interface. Push (click) a button to command the computer to perform some action, or to answer a question. Typical buttons are OK, Apply, Cancel, Close, Yes, No and Help.

## [Qt官方文档-QPushButton](https://doc.qt.io/qt-5.15/qpushbutton.html)

## 常用属性

| 属性        | 数据类型 | 描述                                                |
| ----------- | -------- | --------------------------------------------------- |
| autoDefault | bool     | 自动默认                                          |
| default     | bool     | 默认键（用户在对话框中按下键盘Enter键后会触发该键） |
| flat        | bool     | 设置外观扁平化                                      |

## 常用方法

## 信号

| 信号                                                         | 说明                                            |
| ------------------------------------------------------------ | ----------------------------------------------- |
| 同[QAbstractButton](../04-QAbstractButton/00-QAbstractButton-按钮的抽象基类.md) | 由继承关系，包含了父类QAbstractButton的所有信号 |
| showMenu                                                     | 显示(弹出)相关的弹出式菜单                      |


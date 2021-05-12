# QToolButton

继承自[QAbstractButton](../04-QAbstractButton/00-QAbstractButton-按钮的抽象基类.md)

命令或选项的快速访问按钮，通常在 [QToolBar](https://doc.qt.io/qt-5.15/qtoolbar.html) （工具栏）中使用

## Qt官方文档-QToolButton

[Qt 5.15 官方文档-QToolButton](https://doc.qt.io/qt-5.15/qtoolbutton.html)

## 常用方法

## 槽函数

| 槽函数                                         | 说明                         | 备注                                                         |
| ---------------------------------------------- | ---------------------------- | ------------------------------------------------------------ |
| setDefaultAction(QAction **action*)            | 设置*action*的默认action动作 | 详见[官方文档](https://doc.qt.io/qt-5.15/qtoolbutton.html#setDefaultAction) |
| showMenu()                                     | 展示（弹出）相关的弹出式菜单 | 直到用户关闭了弹出菜单该槽函数才返回                         |
| setToolButtonStyle(Qt.ToolButtonStyle *style*) | 设置ToolButton样式           | 仅文字/仅图标/文字在图标旁/文字在图标下                      |


## 信号

| 信号                                                         | 说明                                            | 备注                                                         |
| ------------------------------------------------------------ | ----------------------------------------------- | ------------------------------------------------------------ |
| triggered(QAction *action)                                   | 指定action动作被触发时发送此信号                | 该动作还可以与用户界面的其他部分相关联，例如菜单项和键盘快捷键。 通过这种方式共享操作有助于使用户界面更加一致，并且通常无需执行太多工作。 |


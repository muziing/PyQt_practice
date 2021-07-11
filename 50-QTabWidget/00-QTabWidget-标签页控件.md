# QTabWidget

展示一组选项卡（标签页）的控件



## Qt 官方文档

[Qt 5.15 官方文档-QTabWidget](https://doc.qt.io/qt-5.15/qtabwidget.html)

## 常用方法

设置方法

| 方法                                             | 说明                            | 备注 |
| ------------------------------------------------ | ------------------------------- | ---- |
|                                                  |                                 |      |
|                                                  |                                 |      |
| setCurrentIndex(int *index*)                     |                                 |      |
| setTabsClosable(bool *closeable*)                |                                 |      |
| setElideMode(Qt.TextElideMode *mode*)            |                                 |      |
| setMovable(bool *movable*)                       |                                 |      |
| setTabBarAutoHide(bool *enabled*)                |                                 |      |
| setTabPosition(QTabWidget.TabPosition *position*) | 见下方QTabWidget.TabPostion表格 |      |
| setTabShape(QTabWidget.TabShape*s*)              | 见下方QTabWidget.TabShape表格   |      |



| QTabWidget.TabPosition | 值   | 描述             |
| --------------------- | ---- | ---------------- |
| North                 | 0    | 标签在页上方绘制 |
| South                 | 1    | 标签在页下方绘制 |
| West                  | 2    | 标签在页左侧绘制 |
| East                  | 3    | 标签在页右侧绘制 |



| QTabWidget.TabShape | 值   | 描述                 |
| ------------------- | ---- | -------------------- |
| Rounded             | 0    | 标签为圆角（默认值） |
| Triangular          | 1    | 标签为直角           |



## Public Slots 槽函数

| 槽函数                              | 说明                     | 备注                                   |
| ----------------------------------- | ------------------------ | -------------------------------------- |
| setCurrentIndex(int *index*)        | 设置当前索引             | 初始化控件时没有标签页，所以默认值为-1 |
| setCurrentWidget(QWidget **widget*) | 将*widget*设置为当前控件 |                                        |



## Signals 信号

| 信号                             | 说明                                                   | 备注                                                 |
| -------------------------------- | ------------------------------------------------------ | ---------------------------------------------------- |
| currentChanged(int *index*)      | 当当前页面索引改变时发送此信号，新页的索引作为参数传出 | 如果没有新页（比如在QTabWidget中没有控件），则返回-1 |
| tabBarClicked(int *index*)       | 当用户单击*index*上的标签页时发送此信号                | 如果光标下没有标签页则传出-1                         |
| tabBarDoubleClicked(int *index*) | 当用户双击*index*上的标签页时发送此信号                | 如果光标下没有标签页则传出-1                         |
| tabCloseRequested(int *index*)   | 单击标签页上的关闭按钮将发送此信号                     |                                                      |


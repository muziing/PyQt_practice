# QTabWidget

展示一组选项卡（标签页）的控件



## Qt 官方文档

[Qt 5.15 官方文档-QTabWidget](https://doc.qt.io/qt-5.15/qtabwidget.html)

## 使用方法

> The normal way to use QTabWidget is to do the following:
>
> 1. Create a QTabWidget.
> 2. Create a [QWidget](https://doc.qt.io/qt-5.15/qwidget.html) for each of the pages in the tab dialog, but do not specify parent widgets for them.
> 3. Insert child widgets into the page widget, using layouts to position them as normal.
> 4. Call [addTab](https://doc.qt.io/qt-5.15/qtabwidget.html#addTab)() or [insertTab](https://doc.qt.io/qt-5.15/qtabwidget.html#insertTab)() to put the page widgets into the tab widget, giving each tab a suitable label with an optional keyboard shortcut.

1. 创建一个QTabWidget
2. 创建每个标签页的页面控件，但是不要为它们设置父控件
3. 像普通控件那样把子控件插入到页面控件中，使用布局管理器以定位
4. 调用 addTab() 或 insertTab() 方法把页面控件添加到标签页控件中，为每个标签页一个合适的label标签和键盘快捷键

## 常用方法

### 设置方法

| 方法                                              | 说明                            | 备注 |
| ------------------------------------------------- | ------------------------------- | ---- |
| setTabText(int *index*, str &*label*)             | 为指定索引位置的标签设置文本 |      |
| setTabIcon(int *index*, QIcon &*icon*)            | 为指定索引位置的标签设置图标 |      |
| setTabsClosable(bool *closeable*)                 | 设置是否自动为每个标签页添加关闭按钮 | 只是外观上添加关闭按钮，需要连接信号与槽才能真正实现关闭功能 |
| setUsesScrollButtons(bool *useButtons*) | 控制当选项卡栏有多个选项卡无足够空间显示时是否使用按钮滚动选项卡 |  |
| setElideMode(Qt.TextElideMode *mode*)             | 设置在页签中省略文本的方式 |      |
| setIconSize(QSize &*size*) | 设置页签中图标（最大）尺寸；默认为样式相关的 | 如果实际使用的图标尺寸小于此属性，则不会放大 |
| setMovable(bool *movable*)                        | 设置用户是否可以在页签区域内移动标签页 | 默认为False |
| setTabBarAutoHide(bool *enabled*)                 | 设置为True后，当标签页数量少于两个时自动隐藏页签 | 默认为False |
| setTabPosition(QTabWidget.TabPosition *position*) | 见下方QTabWidget.TabPosition表格 |      |
| setTabShape(QTabWidget.TabShape*s*)               | 见下方QTabWidget.TabShape表格   |      |
| setDocumentMode(bool *set*) | 此属性设置为True时，不会呈现选项卡部件框架，即选项卡页面和其后的窗口等页面无框架区分看起来是一个整体。此模式对于页面需要显示文档类型的情况非常有用，因为节省了选项卡部件框架占用的部分空间。 | |



| QTabWidget.TabPosition | 值   | 描述             |
| --------------------- | ---- | ---------------- |
| North                 | 0    | 页签在页上方绘制 |
| South                 | 1    | 页签在页下方绘制 |
| West                  | 2    | 页签在页左侧绘制 |
| East                  | 3    | 页签在页右侧绘制 |



| QTabWidget.TabShape | 值   | 描述                 |
| ------------------- | ---- | -------------------- |
| Rounded             | 0    | 页签为圆角（默认值） |
| Triangular          | 1    | 页签为三角形（梯形）      |

### 获取方法

| 方法                         | 说明                  | 备注               |
| ---------------------------- | --------------------- | ------------------ |
| count() -> int               | 返回标签页的数量      |                    |
| indexOf(QWidget **w*) -> int | 返回*w*页面当前的索引 | 如果未找到则返回-1 |
| currentIndex() -> int        | 返回当前页面的索引             |                    |



### 页操作

| 方法                                                    | 说明                                              | 备注                                                 |
| ------------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------- |
| addTab(QWidget **page*, str &*label*)                   | 添加一个标签页                                    |                                                      |
| addTab(QWidget **page*, QIcon &*icon*, str &*label*)    | 添加一个标签页                                    |                                                      |
| insertTab(int *index*, QWidget **page*, set &*label*)   | 插入一个标签页                                    |                                                      |
| insertTab(QWidget **page*, QIcon &*icon*, str &*label*) | 插入一个标签页                                    |                                                      |
| removeTab(int *index*)                                  | 移除*index*位置的标签页                           |                                                      |
| setTabEnabled(int *index*, bool *enable*)               | 设置标签是否可用                                  | 即使设置了不可用，该标签页依然可见，只是用户无法选中 |
| clear()                                                 | 移除所有标签页，等同于调用removeTab()直到清空为止 | 并没有删除它们                                       |



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


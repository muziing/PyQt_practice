# QCalendarWidget

一个月日历，允许用户选择一个日期



## Qt 官方文档

[Qt 5.15 官方文档-QCalendarWidget](https://doc.qt.io/qt-5.15/qcalendarwidget.html)



## 槽函数

| 槽函数                                   | 说明                               | 备注 |
| ---------------------------------------- | ---------------------------------- | ---- |
| setCurrentPage(int *year*, int *month*)  | 不改变选中的日期，显示给定的年、月 |      |
| setDateRange(QDate &*min*, QDate &*max*) |                                    |      |
| setGridVisible(bool *show*)              |                                    |      |
| setNavigationBarVisible(bool *visible*)  |                                    |      |
| setSelectedDate(QDate &*date*)           |                                    |      |
| showNextMonth()                          |                                    |      |
| showNextYear()                           |                                    |      |
| showPreviousMonth()                      |                                    |      |
| showPreviousYear()                       |                                    |      |
| showSelectedDate()                       |                                    |      |
| showToday()                              |                                    |      |



## 信号

| 信号                                        | 说明                                           | 备注                                                         |
| ------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------ |
| activated(QDate &*date*)                    | 用户按下Enter或者鼠标双击一个日期时发送此信号  |                                                              |
| clicked(QDate &*date*)                      | 鼠标按下时发送此信号，传出用户点击的日期*date* | 只在点击有效日期时才发送                                     |
| currentPageChanged(int *year*, int *month*) | 当当前显示的月份发生改变时发送此信号           | 新的年、月作为参数传出                                       |
| selectionChanged()                          | 当前选择的日期改变时发送此信号                 | 通过代码调用setSelectedDate()方法或用户通过鼠标键盘选择均会触发 |


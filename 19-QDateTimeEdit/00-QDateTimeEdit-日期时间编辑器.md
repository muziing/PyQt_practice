# QDateTimeEdit

## Qt官方文档

[Qt 5.15 官方文档-QDateTime](https://doc.qt.io/qt-5.15/qdatetime.html)

[Qt 5.15 官方文档-QDate](https://doc.qt.io/qt-5.15/qdate.html)

[Qt 5.15 官方文档-QTime](https://doc.qt.io/qt-5.15/qtime.html)

[Qt 5.15 官方文档-QDateTimeEdit](https://doc.qt.io/qt-5.15/qdatetimeedit.html)



## QDateTime

### 创建

```python
dt = QDateTime(QDateTime)
```

### 显示格式
[QDateTime.toString](https://doc.qt.io/qt-5.15/qdatetime.html#toString)

以 2001年5月21日14:13:09.120为例：

| Format        | Result        |
| ------------- | ------------- |
| dd.MM.yyyy    | 21.05.2001    |
| ddd MMMM d yy | Tue May 21 01 |
| hh:mm:ss.zzz  | 14:13:09.120  |
| hh:mm:ss.z    | 14:13:09.12   |
| h:m :s ap | 2:13 :9 pm    |

更详细的日期时间格式化字符可以参考：

[QDate.toString](https://doc.qt.io/qt-5.15/qdate.html#toString-1)

[QTime.toString](https://doc.qt.io/qt-5.15/qtime.html#toString)



## QDateTimeEdit

继承自[QAbstractSpinBox](../16-QAbstractSpinBox/00-QAbstractSpinBox-数字设定框的抽象基类.md)

### DisplayFormat 显示格式
参考 QDateTime
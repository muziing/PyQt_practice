# QProgressBar

水平或垂直进度条控件

向用户展示程序仍在运行没有卡死，改善用户体验

## Qt 官方文档

[Qt 5.15官方文档-QProgressBar](https://doc.qt.io/qt-5.15/qprogressbar.html)



## 槽函数

| 槽函数                                 | 说明                     | 备注                                                         |
| -------------------------------------- | ------------------------ | ------------------------------------------------------------ |
| reset()                                | 重置进度条               | 进度条将倒回并展示没有进度                                   |
| setRange(int *minimum*, int *maximum*) | 分别设置进度的最小最大值 | 如果当前value值不在新设置的范围内，则会通过reset()方法重置；如果最大最小值均设为0则显示为“忙碌” |
| setValue(int *value*)                  | 设置当前值               | 若试图设置的value值落在范围之外则无效                        |



## 信号

| 信号                      | 说明                                                  |
| ------------------------- | ----------------------------------------------------- |
| valueChanged(int *value*) | 当进度条中的值改变时发送此信号，新的value作为参数传出 |


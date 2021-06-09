# QSlider

继承自[QAbstractSlider](../24-QAbstractSlider/00-QAbstractSlider-滑块控件抽象基类.md)

## Qt 官方文档

[Qt 5.15 官方文档-QSlider](https://doc.qt.io/qt-5.15/qslider.html)

## 刻度线控制

[查看代码](./01-QSlider-刻度控制.py)

| QSlider.TickPosition   | 值   | 描述                             |
| ---------------------- | ---- | -------------------------------- |
| QSlider.NoTicks        | 0    | 不绘制任何刻度线                 |
| QSlider.TicksAbove     | 1    | 在水平）滑块控件上方绘制刻度线   |
| QSlider.TicksBelow     | 2    | 在水平）滑块控件（下方绘制刻度线 |
| QSlider.TicksBothSIdes | 3    | 在凹槽两侧绘制刻度线             |
| QSlider.TicksLeft      | 1    | 在（垂直）滑块控件左侧绘制刻度线 |
| QSlider.TicksRight     | 2    | 在（垂直）滑块控件右侧绘制刻度线 |

## Signals 信号

[查看代码](../24-QAbstractSlider/03-QAbstractSlider-是否按下、信号.py)

| 信号             | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| valueChanged()   | 当滑块的值改变时发射此信号，tracking()决定是否在用户交互过程中发送此信号 |
| sliderPressed()  | 当用户开始拖动滑块时发射此信号                               |
| sliderMoved()    | 当用户拖动滑块时发送此信号                                   |
| sliderReleased() | 当用户释放滑块时发送此信号                                   |


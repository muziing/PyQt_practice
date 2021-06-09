# QAbstractSlider

滑块控件的抽象基类。

滑块控件即用户通过鼠标拖拽、键盘方向键控制输入（一般为int整数）的控件

## Qt 官方文档

[Qt 5.15官方文档-QAbstractSlider](https://doc.qt.io/qt-5.15/qabstractslider.html)



## SliderAction



| QAbstractSlider.SliderAction        | 值   |
| ----------------------------------- | ---- |
| QAbstractSlider.SliderNoAction      | 0    |
| QAbstractSlider.SliderSingleStepAdd | 1    |
| QAbstractSlider.SliderSingleStepSub | 2    |
| QAbstractSlider.SliderPageStepAdd   | 3    |
| QAbstractSlider.SliderPageStepSub   | 4    |
| QAbstractSlider.SliderToMinimum     | 5    |
| QAbstractSlider.SliderToMaximum     | 6    |
| QAbstractSlider.SliderMove          | 7    |



## SliderChange

| QAbstractSlider.SliderChange            | 值   |
| --------------------------------------- | ---- |
| QAbstractSlider.SliderRangeChange       | 0    |
| QAbstractSlider.SliderOrientationChange | 1    |
| QAbstractSlider.SliderStepsChange       | 2    |
| QAbstractSlider.SliderValueChange       | 3    |



## Public Slots 槽函数

| 槽函数                           | 说明 | 备注 |
| -------------------------------- | ---- | ---- |
| setOrientation(*Qt.Orientation*) |      |      |
| setRange(int *min*, int *max*)   |      |      |
| setValue(*int*)                  |      |      |



## Signals 信号

[查看代码](./03-QAbstractSlider-是否按下、信号.py)

| 信号                               | 说明 | 描述 |
| ---------------------------------- | ---- | ---- |
| actionTriggered(int *action*)      |      |      |
| rangeChanged(int *min*, int *max*) |      |      |
| sliderMoved(int *value*)           |      |      |
| sliderPressed()                    |      |      |
| sliderReleased()                   |      |      |
| valueChanged(int *value*)          |      |      |


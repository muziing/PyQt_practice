# QFontComboBox

一个让用户选择字体的combobox

继承自 [QComboBox](../22-QComboBox/00-QComboBox-组合下拉框.md)



## Qt 官方文档

[Qt 5.15 官方文档-QFontComboBox](https://doc.qt.io/qt-5.15/qfontcombobox.html)



## Public Slots 槽函数

| 槽函数                     | 说明         | 备注 |
| -------------------------- | ------------ | ---- |
| setCurrentFont(QFont &*f*) | 设置当前字体 |      |



## Signal 信号

| 信号                              | 说明                                             | 备注 |
| --------------------------------- | ------------------------------------------------ | ---- |
| currentFontChanged(QFont &*font*) | 当前字体发生变化时发送此信号，新字体作为参数传出 |      |



## 常用方法

> currentFont() -> QFont
>
> setCurrentFont(QFont &*font*)

当前选择的字体



> fontFilters() -> QFontComboBox.FontFilters
>
> setFontFilters(QFontComboBox.FontFilters *filters*)

combobox的筛选器

| QFontComboBox.FontFilters | 值   | 描述             |
| ------------------------- | ---- | ---------------- |
| AllFonts                  |      | 显示全部字体     |
| ScalableFonts             |      | 显示可缩放字体   |
| NonScalableFonts          |      | 显示不可缩放字体 |
| MonospacedFonts           |      | 显示等宽字体     |
| ProportionalFonts         |      | 显示比例字体     |



> writingSystem() -> QFontDatabase.WritingSystem
>
> setWritingSystem(*QFontDatabase.WritingSystem*)

设置combobox的writing system，比如 Latin、Greek等
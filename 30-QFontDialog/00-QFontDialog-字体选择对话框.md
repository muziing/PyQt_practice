# QFontDialog

继承自[QDialog](../29-QDialog/00-QDialog-对话框窗口基类.md)



## Qt 官方文档

[Qt 5.15 官方文档-QFontDialog](https://doc.qt.io/qt-5.15/qfontdialog.html)



## Signals 信号

| 信号                              | 说明                                             | 备注                                       |
| --------------------------------- | ------------------------------------------------ | ------------------------------------------ |
| currentFontChanged(QFont &*font*) | 当前字体改变时发送此信号，新的字体作为参数传出   | 最终选择的字体可能与当前字体不同           |
| fontSelected(QFont &*font*)       | 字体被选择时发送此信号，被选择的字体作为参数传出 | 当用户在字体对话框中更改当前字体时不会发送 |



## Static Public Members 静态方法

> getFont(bool * *ok*, QFont &*initial*, QWidget * *parent* = nullptr, str &*title* = str(), QFontDialog.FontDialogOptions *options* = FontDialogOptions()) -> QFont



> getFont(bool * *ok*, QWidget **parent* = nullptr) -> QFont



## 常用方法



> options() -> QFontDialog.FontDialogOptions
>
> setOptions(QFontDialog.FontDialogOptions *options*)

此属性包含影响对话框外观和感觉的各种选项

默认情况下所有选项都禁用

应在显示对话框前设置属性。并非所有属性都适用，取决于平台。

| QFontDialog.FontDialogOption | 值   | 描述                                                      |
| ---------------------------- | ---- | --------------------------------------------------------- |
| NoButtons                    | 1    | 不要显示 **OK** 和 **Cancel** 按钮                        |
| DontUseNativeDialog          | 2    | 在Mac上使用Qt的标准字体对话框，而不是苹果的原生字体面板。 |
| ScalableFonts                | 4    | 显示可缩放字体                                            |
| NonScalableFonts             | 8    | 显示不可缩放字体                                          |
| MonospacedFonts              | 16   | 显示等宽字体                                              |
| ProportionalFonts            | 32   | 显示比例字体                                              |


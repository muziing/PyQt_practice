# QTextEdit

用于显示和编辑纯文本、富文本的控件

## Qt官方文档
[Qt 5.15官方文档-QTextEdit](https://doc.qt.io/qt-5.15/qtextedit.html)



| QTextEdit.AutoFormatting | 值   | 描述                                                         |
| ------------------------ | ---- | ------------------------------------------------------------ |
| AutoNone                 |      | 不做任何自动格式化                                           |
| AutoBulletList           |      | 自动创建项目符号列表(例如，当用户在最左边的列中输入星号('*')，或在现有列表项中按Enter键 |
| AutoAll                  |      | 应用所有自动格式。目前只支持自动项目符号列表                 |



| QTextEdit.LineWrapMode | 值   |
| ---------------------- | ---- |
| NoWrap                 | 0    |
| WidgetWidth            | 1    |
| FixedPixelWidth        | 2    |
| FixedColumnWidth       | 3    |



## Public Slots 槽函数

| 槽函数                                                       | 说明 | 备注 |
| ------------------------------------------------------------ | ---- | ---- |
| append(str &*text*)                                          |      |      |
| clear()                                                      |      |      |
| copy()                                                       |      |      |
| cut()                                                        |      |      |
| paste()                                                      |      |      |
| undo()                                                       |      |      |
| redo()                                                       |      |      |
| selectAll()                                                  |      |      |
| insertHtml(str &*text*)                                      |      |      |
| insertPlainText(str &*text*)                                 |      |      |
| scrollToAnchor(str &*name*)                                  |      |      |
| setAlignment([Qt.Alignment](https://doc.qt.io/qt-5.15/qt.html#AlignmentFlag-enum) *a*) |      |      |
| setCurrentFont(QFont &*f*)                                   |      |      |
| setFontFamily(str &*fontFamily*)                             |      |      |
| setFontItalic(bool *italic*)                                 |      |      |
| setFontPointSize([qreal](https://doc.qt.io/qt-5.15/qtglobal.html#qreal-typedef) *s*) |      |      |
| setFontUnderline(bool *underline*)                           |      |      |
| setFontWeight(int *weight*)                                  |      |      |
| setPlainText(str &*text*)                                    |      |      |
| setText(str &*text*)                                         |      |      |
| setTextBackgroundColor(const [QColor](https://doc.qt.io/qt-5.15/qcolor.html) &*c*) |      |      |
| setTextColor(const [QColor](https://doc.qt.io/qt-5.15/qcolor.html) &*c*) |      |      |
| zoomIn(int *range* = 1)                                      |      |      |
| zoomOut(int *range* = 1)                                     |      |      |



## Signals 信号

| 信号                                                         | 说明 | 备注 |
| ------------------------------------------------------------ | ---- | ---- |
| copyAvailable(bool *yes*)                                    |      |      |
| currentCharFormatChanged([QTextCharFormat](https://doc.qt.io/qt-5.15/qtextcharformat.html) &*f*) |      |      |
| cursorPositionChanged()                                      |      |      |
| redoAvailable(bool *available*)                              |      |      |
| undoAvailable(bool *available*)                              |      |      |
| selectionChanged()                                           |      |      |
| textChanged()                                                |      |      |


# QPlainTextEdit

继承自[QAbstractScrollArea](../12-QAbstractScrollArea/00-QAbstractScrollArea-滚动区域的低级抽象.md)

编辑和显示纯文本的控件

适用于段落和字符：
段落是一个格式化的字符串，为了适应控件的宽度，会自动换行
默认情况下，在读取纯文本时，一个换行符表示一个段落
文档由零个或多个段落组成。段落由硬线断开分隔
段落中的每个字符都有自己的属性，例如字体和颜色

内容的编辑：
文本的选择由QTextCursor类处理，该类提供创建选择检索文本内容删除选择的功能
QPlainTextEdit包含一个QTextDocument对象，可以使用document()方法检索该对象

与QTextEdit功能相似，但针对纯文本处理进行了优化。差异：
QPlainTextEdit是一个简略版的类，使用QTextEdit和QTextDocument作为背后实现的技术支撑。
性能优于QTextEdit，主要是因为在文本文档中使用QPlainTextDocumentLayout简化文本布局
纯文本文档布局不支持表格或嵌入框架，并使用逐行滚动的方式替换像素精确高度计算

## Qt官方文档

[Qt 5.15官方文档-QPlainTextEdit](https://doc.qt.io/qt-5.15/qplaintextedit.html)


## 编辑时可用的快捷键

[Qt官方文档-编辑快捷键](https://doc.qt.io/qt-5.15/qplaintextedit.html#editing-key-bindings)



## 常用方法



| 方法                                       | 描述                                 | 备注                                     |
| ------------------------------------------ | ------------------------------------ | ---------------------------------------- |
| setPlaceholderText(str &*placeholderText*) | 设置占位文本                         |                                          |
| toPlainText() -> str                       | 将文本编辑器中的文本以纯文本形式返回 |                                          |
| setPlainText(str &*text*)                  | 将文本编辑器的内容设置为*text*       | 之前的所有内容将不被保留                 |
| setTabChangesFocus(bool *b*)               | 设置Tab键功能为切换焦点              | 默认关闭，即，按下键盘Tab键是输入一个Tab |
| setUndoRedoEnabled(bool *enable*)          | 设置是否开启撤销/重做功能            | 默认为True，开启                         |
| setReadOnly(bool *ro*)                     | 设置只读                             | 默认False                                |


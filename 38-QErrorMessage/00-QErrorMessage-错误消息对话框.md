# QErrorMessage

继承自 [QDialog](../29-QDialog/00-QDialog-对话框窗口基类.md)

一个显示错误消息的对话框

> The static qtHandler() function installs a message handler using qInstallMessageHandler() and creates a QErrorMessage that displays qDebug(), qWarning() and qFatal() messages. This is most useful in environments where no console is available to display warnings and error messages.
>
> 静态 qtHandler() 函数使用 qInstallMessageHandler() 安装消息处理程序并创建显示 qDebug()、qWarning() 和 qFatal() 消息的 QErrorMessage。 这在没有控制台可用于显示警告和错误消息的环境中最有用。

## Qt 官方文档

[Qt 5.15 官方文档-QErrorMessage](https://doc.qt.io/qt-5.15/qerrormessage.html)



## Public Slots 槽函数

| 槽函数                                  | 说明     | 备注                                                         |
| --------------------------------------- | -------- | ------------------------------------------------------------ |
| showMessage(str &*message*)             | 显示消息 | 通常立即显示，但如果有挂起的消息则将排队以待稍后显示；如果用户要求不再显示该消息，则此函数不执行任何操作 |
| showMessage(str &*message*, str &*type*) | 显示消息 | 重载；如果用户要求不再显示该类型*type*的消息，则此函数不执行任何操作 |


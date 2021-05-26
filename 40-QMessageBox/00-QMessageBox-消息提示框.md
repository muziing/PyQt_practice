# QMessageBox

继承自[QDialog](../29-QDialog/00-QDialog-对话框窗口基类.md)

弹出一个模态对话框，用于为用户提供信息；或向用户提问并接收回答

## Qt 官方文档
[Qt 5.15-官方文档-QMessageBox](https://doc.qt.io/qt-5.15/qmessagebox.html)

## 标准图标

在消息提示框中显示一个标准图标

```python
message_box.setIcon(QMessage.Information)
```

| 图标                 | 值   | 说明     |
| -------------------- | ---- | -------- |
| QMessage.NoIcon      | 0    | 没有图标 |
| QMessage.Information | 1    | 提供信息 |
| QMessage.Warning     | 2    | 警告     |
| QMessage.Critical    | 3    | 严重错误 |
| QMessage.Question    | 4    | 提问     |

## 标准按钮

| 按钮                         | 描述         | 按钮规则        |
| --------------------------- | ------------ | --------------- |
| QMessageBox.Ok              | 确认         | AcceptRole      |
| QMessageBox.Open            | 打开         | AcceptRole      |
| QMessageBox.Save            | 保存         | AcceptRole      |
| QMessageBox.Cancel          | 取消         | RejectRole      |
| QMessageBox.Close           | 关闭         | RejectRole      |
| QMessageBox.Discard         | 丢弃，不保存 | DestructiveRole |
| QMessageBox.Apply           | 应用         | ApplyRole       |
| QMessageBox.Reset           | 重置         | ResetRole       |
| QMessageBox.RestoreDefaults | 恢复默认值   | ResetRole       |
| QMessageBox.Help            | 帮助         | HelpRole        |
| QMessageBox.SaveAll         | 保存全部     | AcceptRole      |
| QMessageBox.Yes             | 是           | YesRole         |
| QMessageBox.YesToAll        | 全选是       | YesRole         |
| QMessageBox.No              | 否           | NoRole          |
| QMessageBox.NoToAll         | 全选否       | NoRole          |
| QMessageBox.Abort           | 中止         | RejectRole      |
| QMessageBox.Retry           | 重试         | AcceptRole      |
| QMessageBox.Ignore          | 忽略         | AcceptRole      |



## 标准按钮规则

|            规则              | 值   | 描述                                                 |
| --------------------------- | ---- | ---------------------------------------------------- |
| QMessageBox.InvalidRole     | -1   | 该按钮无效                                           |
| QMessageBox.AcceptRole      | 0    | 单击该按钮将使对话框被接受（例如，确定）             |
| QMessageBox.RejectRole      | 1    | 单击该按钮会导致拒绝对话框（例如取消）               |
| QMessageBox.DestructiveRole | 2    | 单击该按钮会导致破坏性更改（例如关闭文件不保存修改） |
| QMessageBox.ActionRole      | 3    | 单击该按钮将导致更改对话框中的元素                   |
| QMessageBox.HelpRole        | 4    | 可以单击该按钮以请求帮助                             |
| QMessageBox.YesRole         | 5    | 按钮是一个“是”按钮                                   |
| QMessageBox.NoRole          | 6    | 按钮是一个“否”按钮                                   |
| QMessageBox.ResetRole       | 7    | 该按钮将对话框的字段重置为默认值                     |
| QMessageBox.ApplyRole       | 8    | 该按钮将应用当前更改                                 |


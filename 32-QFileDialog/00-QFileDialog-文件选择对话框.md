# QFileDialog

继承自[QDialog](../29-QDialog/00-QDialog-对话框窗口基类.md)



## Qt 官方文档

[Qt 5.15 官方文档-QFileDialog](https://doc.qt.io/qt-5.15/qfiledialog.html)



| QFileDialog.AcceptMode | 值   |
| ---------------------- | ---- |
| AcceptOpen             | 0    |
| AcceptSave             | 1    |



| QFileDialog.DialogLabel | 值   |
| ----------------------- | ---- |
| LookIn                  | 0    |
| FileName                | 1    |
| FileType                | 2    |
| Accept                  | 3    |
| Reject                  | 4    |



| QFileDialog.FileMode | 值   | 描述                                                         |
| -------------------- | ---- | ------------------------------------------------------------ |
| AnyFile              | 0    | 文件名，不论文件是否存在                                     |
| ExistingFile         | 1    | 已经存在的单个文件名                                         |
| Directory            | 2    | 目录的名称。同时显示文件和目录。（对于Windows，使用 native 文件对话框时不支持在目录选择器中显示文件） |
| ExistingFiles        | 3    | 0个到多个已存在的文件名                                      |



| QFileDialog.Options         | 值   | 描述                                                         | 备注                                         |
| --------------------------- | ---- | ------------------------------------------------------------ | -------------------------------------------- |
| ShowDirsOnly                |      | 只在对话框中显示目录（默认文件和目录都显示），只在目录文件模式下有效 |                                              |
| DontResolveSymlinks         |      | 不要在文件对话框中解析符号链接（默认解析符号链接）           |                                              |
| DontConfirmOverwrite        |      | 如果选择了已经存在的文件，不需要确认（默认请求确认）         | 在macOS上使用native 文件对话框时不支持此属性 |
| DontUseNativeDialog         |      | 不要使用native文件对话框（默认使用native文件对话框）         | 必须在显示或改变对话框前设置此属性           |
| ReadOnly                    |      |                                                              |                                              |
| HideNameFilterDetails       |      |                                                              |                                              |
| DontUseSheet                |      |                                                              |                                              |
| DontUseCustomDirectoryIcons |      |                                                              |                                              |





| QFileDialog.ViewMode | 值   | 描述                                     |
| -------------------- | ---- | ---------------------------------------- |
| Detail               | 0    | 显示目录中每个项目的图标、名称和详细信息 |
| List                 | 1    | 仅显示目录中每个项目的图标和名称         |


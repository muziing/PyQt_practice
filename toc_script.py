import os

"""用于生成整个PyQt_practice项目的toc目录，markdown格式"""

abs_addr = os.getcwd()  # 获取当前工作目录（PyQt_practice项目）的绝对路径
with open('./toc.md', 'wt', encoding='UTF-8') as f:
    lines = list()
    dir_list = list()
    listed_dir = os.listdir('./')  # 列出当前目录下所有项目
    listed_dir.sort()  # 按照名称排序
    for i in listed_dir:
        if i[0].isdigit() and i[1].isdigit():  # 根据本项目的命名规律，所有文件名前两位为数字的才是需要进行目录的文件夹
            dir_list.append(i)
    for n in dir_list:
        lines.append(f'### {n}\n')
        os.chdir(f'{abs_addr}/{n}')  # 进入子文件夹
        file_names = os.listdir('./')
        file_names.sort()
        for m in file_names:
            if m.endswith('.py'):  # 根据本项目命名规律，所有.py文件才是需要目录的
                lines.append(f'[{m}](./{n}/{m})\n\n')
    f.writelines(lines)

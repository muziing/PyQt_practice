import os

"""用于生成整个PyQt_practice项目的toc目录，markdown格式"""

abs_addr = os.getcwd()
with open('./toc.md', 'wt', encoding='UTF-8') as f:
    lines = list()
    dir_list = list()
    listed_dir = os.listdir('./')
    listed_dir.sort()
    for i in listed_dir:
        if i[0].isdigit() and i[1].isdigit():
            dir_list.append(i)
    for n in dir_list:
        lines.append(f'### {n}\n')
        os.chdir(f'{abs_addr}/{n}')
        file_names = os.listdir('./')
        file_names.sort()
        for m in file_names:
            if m.endswith('.py'):
                lines.append(f'[{m}](./{n}/{m})\n\n')
    f.writelines(lines)

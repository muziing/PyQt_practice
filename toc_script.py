import os


def make_toc():
    """用于生成整个PyQt_practice项目的toc目录，markdown格式"""
    abs_addr = os.getcwd()  # 获取当前工作目录（PyQt_practice项目）的绝对路径
    with open('./toc.md', 'wt', encoding='UTF-8') as f:
        lines = list()
        valid_dir_list = list()
        listed_dir = os.listdir('./')  # 列出当前目录下所有项目
        listed_dir.sort()  # 按照名称排序
        for dir_name in listed_dir:
            if dir_name[0].isdigit() and dir_name[1].isdigit():  # 本项目的命名规律，文件名前两位为数字的才是需要进行目录的文件夹
                valid_dir_list.append(dir_name)
        for valid_dir_name in valid_dir_list:
            lines.append(f'### {valid_dir_name}\n')
            os.chdir(f'{abs_addr}/{valid_dir_name}')  # 进入子文件夹
            file_names = os.listdir('./')
            file_names.sort()
            for file_name in file_names:
                if file_name.endswith('.py') or file_name.endswith('.md'):  # 根据本项目命名规律，所有.py文件才是需要目录的
                    lines.append(f'[{file_name}](./{valid_dir_name}/{file_name})\n\n')
        f.writelines(lines)


if __name__ == '__main__':
    make_toc()

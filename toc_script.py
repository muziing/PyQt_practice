import os
from pprint import pprint

# TODO 改写成oop；改用 pathlib 替代 os.path


def tree(working_dir="./") -> dict:
    """
    列出工作目录下所有符合要求的目录和文件
    """
    tree_result = dict()
    valid_dir_list = list()
    file_name_list = list()

    abs_addr = os.getcwd()  # 获取当前工作目录的绝对路径
    listed_dir = os.listdir(working_dir)  # 列出工作目录下所有项目
    listed_dir.sort()  # 按照名称排序

    # 验证有效性
    for dir_name in listed_dir:
        if dir_name[0:2].isdigit():  # 本项目的命名规律，文件名前两位为数字的才是需要进行目录的文件夹
            valid_dir_list.append(dir_name)
    for valid_dir_name in valid_dir_list:
        os.chdir(f'{abs_addr}/{valid_dir_name}')  # 进入子文件夹
        file_names = os.listdir('./')
        file_names.sort()
        for file_name in file_names:
            if file_name.endswith('.py') or file_name.endswith('.md'):  # 根据本项目命名规律，所有.py或.md文件才是需要目录的
                file_name_list.append(file_name)
        tree_result.update({valid_dir_name: file_name_list})
        file_name_list = list()  # 重新置空
    os.chdir(abs_addr)  # 切回初始工作目录

    return tree_result


def cloc_script(working_dir='./') -> str:
    """
    使用cloc统计项目代码行数
    """
    ignored_dir = str()
    with open('.gitignore', 'r', encoding='UTF-8') as f:
        for dir_name in f.readlines():
            dir_name = dir_name.replace('/', '')
            dir_name = dir_name.replace('\n', ',')
            ignored_dir += dir_name

    # 调用cloc，并排除gitignore中的目录，需要提前将cloc添加到系统环境变量
    cmd = f'cloc --exclude-dir {ignored_dir} {working_dir}'

    with os.popen(cmd) as p:
        cmd_result = p.read()

    # TODO 增强鲁棒性，增加对cloc调用失败的异常处理
    # 根据cloc返回结果，连续两个换行符后面的内容是需要的信息
    return cmd_result.split('\n\n', 1)[1]


def write_toc(tree_dict: dict, toc_file='./toc.md'):
    """
    把目录和文件名写入toc.md文件
    """
    write_lines = list()
    file_counter = 0

    for dir_name in tree_dict.keys():
        write_lines.append(f'### [{dir_name}](./{dir_name})\n')
        for file_name in tree_dict[dir_name]:
            write_lines.append(f'[{file_name}](./{dir_name}/{file_name})\n\n')
            file_counter += 1
    write_lines += f"共{len(tree_dict.keys())}个目录，{file_counter}个文件."
    with open(toc_file, 'wt', encoding='UTF-8') as f:
        f.writelines(write_lines)
    print(f"TOC生成成功，共{len(tree_dict.keys())}个目录，{file_counter}个文件.")
    # TODO 将cloc代码行数统计结果也写入toc文档尾部


if __name__ == '__main__':
    # pprint(tree())
    # print(cloc_script())
    write_toc(tree())

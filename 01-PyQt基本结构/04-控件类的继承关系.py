from PyQt5.Qt import *


def get_sub_classes(class_):
    """递归的显示某一对象的所有子对象"""
    for subclass in class_.__subclasses__():
        print(subclass)
        if len(class_.__subclasses__()) > 0:
            get_sub_classes(subclass)


get_sub_classes(QAbstractButton)

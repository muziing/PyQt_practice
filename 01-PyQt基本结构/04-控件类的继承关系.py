from PyQt5.Qt import *


def get_sub_classes(class_):
    for subclass in class_.__subclasses__():
        print(subclass)
        if len(class_.__subclasses__()) > 0:
            get_sub_classes(subclass)


get_sub_classes(QAbstractButton)

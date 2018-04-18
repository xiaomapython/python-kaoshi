# -*- coding=utf8 -*-

__Author__ = 'majuchuan'


# 闭包
def fun1(x):
    def s():
        return 7
    return s


@fun1
def fun2():
    pass


print(fun2())

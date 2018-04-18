# -*- coding=utf8 -*-

__Author__ = 'majuchuan'


# path = input("请输入文件路径(相对路径或者绝对路径):")
with open('test.txt', 'r') as f:
    line = int(input("你想打印的行数："))
    for i in range(line):
        i = i+1
        print("第%s行" % i, f.readline().split('\n')[0])

    print("一共有%s行" % (len(f.readlines())+line))



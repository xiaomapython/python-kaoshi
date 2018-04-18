# -*- coding=utf8 -*-

__Author__ = 'majuchuan'


import random

num = random.randint(1, 100)
print(num)
n = 0
print("请输入1-100的正数数")
while n < 10:
    guess_num = int(input("输入你要猜的数字："))
    if guess_num == num:
        print("恭喜你，猜对了", end=" ")
        break
    elif guess_num > num:
        print("你所猜的数字偏大了", end=" ")
    else:
        print("你所猜的数字偏小了", end=" ")
    n += 1
    print("你还有%s次机会" % (10-n))
else:
    print("对不起，你的10次机会用完了")


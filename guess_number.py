# 猜数字游戏，1到100之间的随机数字

import random
r = random.randint(1,100)
count = 0
while True:
    count = count + 1
    num = int(input('请输入数字：'))
    if num == r:
        print('恭喜你，你猜对了')
        break
    elif num > r:
        print('比', num, '小，再猜')
    elif num < r:
        print('比', num, '大，接着猜')
    print('这是第', count, '次')
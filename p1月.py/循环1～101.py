import random
n = random.randint(1,102)
cc = 0
while cc<100:
    a = int(input('请输入数字: '))

    if n>a:
        print('猜小了')
    elif n<a:
        print('猜大了')
    else:
        print('耶，猜对了 买水去')
        break


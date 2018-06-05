import random
m = random.randint(1,100)
i = 0
while True:
    p = int(input('请输入1～100数字'))
    i += 1
    if p > m:
        print('猜大了, ')
    elif p < m:
        print('猜小了 ')
    else:
        print('耶，猜对了 ，买冰淇淋')
        break

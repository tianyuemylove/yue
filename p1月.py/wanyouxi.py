import random
x = random.randint(1,100)
for b in range(1,15555555555555555555555555555555555555555555555555555555):
    a =int(input("猜1～100的数字"))
    if a > x :
        print ("猜大了")
    elif a < x :
        print ("猜小了")
    else:
        print ("恭喜你猜对了")
        break


import random
a = random.randint(1,100)
for x in range (1,10,1):
    b = int(input("请输入数字"))
    if b < a:
        print ("猜小了")
    elif b == a:
        print ("你是个幸运的女孩")
        break
    else:
        print ("猜大了")

        

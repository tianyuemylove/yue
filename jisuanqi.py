e = input('欢迎使用小唯计算器')
def jia (a,b):
    c = a + b
    print(c)
def jian (a,b):
    c = a - b
    return (c)
def cheng (a,b):
    c = a * b
    print (c)
def chu (a,b):
    c = a/b
    print (c)
jia(1,2)

while True :
    a = int (input("请输入数字："))
    d = input("请输入  + - * /")
    b = int (input("请输入数字："))
    if d == '+':
        hc = jia(a,b)
        print (hc)
    elif d == '-':
        cc = jian (a,b)
        print (cc)
    elif d == '*':
        yc = cheng(a,b)
        print (yc)
    elif d == '/':
        pc = chu(a,b)
        print (pc)
    elif a=='q'or b=='q'or d=='q':
        break
    0
        print('你输写错误')
        	

   

print("欢迎使用小唯 计算器")
def jia (a,b):
    c = a+b
    return c
def jian (a,b):
    c = a-b
    return c
def cheng (a,b):
    c = a*b
    return c
def chu (a,b):
    c = a/b
    return c
a = int(input("请输入数字>>"))
while True:
    d = input ("请输入 +  -  *  /  ")
    if d == 'q':
        print (d)
        break
    b = int(input("请输入数字>>"))
    if d == '+':
        cc = jia(a,b)
        print (cc)
    elif d == '-':
        co = jian(a,b)
        print (co)
    elif d == '*':
        ce = cheng(a,b)
        print(ce)
    elif d == '/':
        cg = chu(a,b)
        print(cg)
    else:
        print("输入错误")
    
           





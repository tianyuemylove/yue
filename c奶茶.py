listt = [] # 定义了一个空列表
def naicha(): 
    print('*' *30)
    print('欢迎来到一点点奶茶店 ⓛⓞⓥⓔ ')
    print('1.添加奶茶菜单')
    print('2.查询全部奶茶菜单')
    print('3.点餐')
    print('4.查询一个指定菜单')
    print('5.删除一个奶茶')
    print('6.结帐')
    print('7.退出系统')
    print('*'* 30)
def menu(): # 奶茶菜单
    print('奶茶种类๑۩۩.. ..۩۩ ')
    print('巧克力奶茶'  '￥12')
    print('西柚奶茶'  '￥9')
    print('红豆奶茶'  '￥9')
    print('珍珠奶茶'  '￥9' )
    print('香芋奶茶'   '￥9')
def add(): #新建菜单    增加 
    name = input('请输入奶茶名称 ღ ஜ :')
    price =float(input('请输入奶茶价格 ღ ஜ :'))
    class1 = input('请输入奶茶的类型 ღ ஜ :')
    kouwei = input('请输入奶茶口味 ღ ஜ :')
    # dic = {} # 把输入的内容保存到字典里, 只是一个奶茶 
    dic = {'姓名':name,'价格':price,'类型':class1,'口味':kouwei}
    listt.append(dic) # 把这一个奶茶添加到 列表菜单中
   
def all(): #查看全部奶茶菜单    查看
   # if len(listt)
    # a = 1
    for i in listt:
     
        print('您选择的奶茶名字是 ღ ஜ :%s \n您选择的奶茶价格是 ღ ஜ :%s,' % (i['姓名'],i['价格']))
     #       a -=1
        
        print('*'* 30)
c_list =[]
def diancan(n):     # 点奶茶
    dic =listt[n-1]
    c_list.append(dic)  # 最后结帐使用
    return dic  # 返回给调用这 一个字典 保存了完整信息
def zhiding(): # 查询一个指定奶茶 (名字 价格 口味 类型 等)
    v = int(input('请输入你要查询奶茶的编号 ஓ '))
    v = v-1
    print(listt[v])
def shanchu(): # 删除一个奶茶
    # r 是你要删除奶茶的名字
    r = int(input('请输入你要删除奶茶的编号：'))
    r = r-1
    listt.pop(r)
    print(listt)
dic = {}
#def genggai():  # 更改奶茶
 #   new = input('请输入你要更改的内容 name price class1 kouwei >> ') 
'''
    if new == 'name':
        w = input('请您输入奶茶新的名字:')
        dic['name']=w
        print(listt)
    elif new == 'price':
      w = int(input('请您输入奶茶新的价格 :'))
        dic['price']=w
        print(listt)
    elif new == 'class1':
        w = input('请您输入奶茶新的类型 :')
        dic['class1'] = w
        print(listt)
    elif new == 'kouwei':
        w = input('请您输入奶茶新的口味 :')
        dic['kouwei']=w
        print(listt)
    else:
        print('您输入错误请重新输入')
''' 
    
def jiezhang():
    # 结帐计算金额
    s = 0
    if len(c_list) >0:
        for i in c_list:
            s += int(i['价格'])
    return s
    
while True:
    naicha()
    menu()
    x = int(input('请输入您需要的操作 ஓ :'))
    if x == 1:
        add()
    elif x == 2:
        all()
        print(listt)
    elif x == 3:
        c = int(input('请输入您要点奶茶的编号 ஓ :'))
        d =diancan(c) # 返回的是 一个奶茶完整信息， 
        for q in listt:
            print ('您选择的奶茶名字是 ღ  ：%s \n您选择的奶茶价格是 ღ  ： %s \n 您选择的奶茶口味是：%s \n 您选择的奶茶类型是：%s ' % (d['姓名'] , d['价格'],d['口味'],d['类型']))
    elif x == 4:
        zhiding()
    elif x == 5:
        shanchu()
   # elif x ==6:
    #    genggai()

    elif x == 6:
        p = int(input('奶茶的单价是ഇ :>> '))
        s = int(input('奶茶的数量是ഇ :>> '))
        m = p * s # 钱
        
        print ('您本次应当支付的金额是 ★  %d:' % m)
        print ('欢迎下次光临一点点奶茶店 ⓛⓞⓥⓔ !')
        jiezhang()
    elif x== 0:
        print('退出成功')
    elif x == 7:
        break
    else:
        print('您输入错误，请重新输入')




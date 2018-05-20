list_name = []
dic = {}
list_name.append(dic)
def aa():
    print('*'* 40)
    print('1.新建名片')
    print('2.显示名片')
    print('3.查看名片')
    print('4.删除名片')
    print('5.退出系统')
    print('6.修改名片')
    print('*' * 40)
aa()
def cc():
    user = input('请输入姓名:')
    age = int(input('请输入年龄:'))
    phone = int(input('请输入电话:'))
    com = input('请输入公司:')
    sex = input('请输入性别:')
    dic = {'name':user,'age':age,'phone':phone,'com':com,'sex':sex}
    list_name.append(dic)
    print(list_name)
def vv():
    print ("显示全部名片")
    print (list_name)
def yy():
    t = int(input("查看哪个名片"))
    t = t-1
    print (list_name[t])
def kk():
    ss = int(input("删h除名片"))
    ss =ss-1
    list_name.pop(ss)
    print(list_name)
def oo():
    dd = input('修改名片:name,com,age,phone,sex:')
    if dd == 'name':
        r = input("请输入新的名字:")
        dic["name"] = r
        print(list_name)
    elif dd == 'com':
        r = input("请输入新的公司:")
        dic['com']=r
        print(list__name)
    elif dd =='age':
        r = input("请输入新的年龄:")
        dic['age']=r
        print(list_name)
    elif dd == 'phone':
        r = input("请输入新的电话:")
        dic['phone'] = r
        print(list_name)
    elif dd == 'sex':
        r = input("请输入新的性别:")
        dic['sex']=r
        print(list_name)
    else:
        print('您输出错误，请重新输入 ')
  
def hh():
    zz = int(input('退出系统'))
    print(list_name)
while True:
    x = int(input('请您输入要操作的序号 1.新建名片 2. 显示名片 3.查看名片 4. 删除名片 5. 退出系统 6.修改名片'))

    if x == 0:
        break
    if x == 1:
        cc()
    elif x == 2:
        vv()
    elif x == 3:
        yy()
    elif x == 4:
        kk()
    elif x == 5:
        break
    elif x == 6:
        oo()
       

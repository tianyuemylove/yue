list1 = []
dic = {}
# cc 是菜单
def cc(): # cc
    print('*' * 30)
    print('欢迎使用名片管理系统 v1.0')
    print('1.新建名片')
    print('2.查看名片')
    print('3.删除名片')
    print('4.修改名片')
    print('5.查看全部名片')
    print('6.退出系统')
    print('*' * 30)
cc()
# vv 是 新建名片
def vv():
    name = input('请输入名字：')
    age = input('请输入年龄：')
    com = input('请输入公司：')
    phone =int(input('请输入手机号：'))
    sex = input('请输入性别：')
    dic = {'name':name,'age':age,'com':com,'phone':phone,'sex':sex}
    list1.append(dic)
    print(list1)
#tt 是 查看全部名片
def tt():
    print(list1)
# pp 是查看名片
def pp():
    z= int(input('请输入你要查询的xu号'))
    z =z-1
    print (list1[z])
# oo是删除名片
def oo():
    ss = int(input('请输入你要删除的名片'))
    ss = ss-1
    list1.pop(ss)
    print(list1)
# xx 是修改名片
def xx():
    dd = input('请输入你要修改的内容 name age com phone sex ')
    r = input('请输入新的名字：')
    if dd == 'name':
        dic['name'] =r
        print(list1)
    r=int(input('请输入新的年龄：'))
    elif dd == 'age':
	dic['age']= r
        print(list1)
    r = inpur('请输入新的公司')
    elif dd =='com':
	dic['com']=r
	print(list1)
    elif dd == 'phone':
	r = int(input('请输入新的电话'))
	dic['phone']=r
	print(list1)
    elif dd == 'sex':
	r = input('请输入新的性别')
	dic['sex']=r
	print(list1)
	else:
	print('您输入错误请重新输入')

while True:
    k = int(input('请输入你要操作的序号：1.新建名片 2.查看名片 3.删除名片 4.修改名片 5 查看全部名片 6 退出系统'))
    if k == 1:
        vv()
    elif k == 2:
        pp()
    elif k== 3:
        oo()
    elif k ==4:
        xx()
    elif k == 5:
        tt()
    elif k == 6:
        break



















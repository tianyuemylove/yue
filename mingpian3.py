listt = []
def cc():
    print('*'* 40)
    print('欢迎使用名片管理系统 v1.0')
    print('1.新建名片')
    print('2.显示名片')
    print('3.查询名片')
    print('4.删除名片')
    print('5.退出系统')
    print('*'* 40)
cc()
''' def vv():
    print('请输入姓名>>')
    print('请输入公司>>')
    print('请输入年龄>>')
    print('请输入电话>>')
    print('请输入性别>>')
    print ('请输入邮箱>>')
vv()'''
def ss():
    name = input('请输入姓名:')
    com = input('请输入公司:')
    age = int(input('请输入年龄:'))
    phone = int(input('请输入电话:'))
    sex = input('请输入性别:')
    email= input('请输入邮箱:')
    dic ={'mane':'name','company':'com','age':'age','phone':'phone','sex':'sex','email':'email'}
    listt.append(dic)
    print(listt)

ss()


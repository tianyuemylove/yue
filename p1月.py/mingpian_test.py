list_card = []
def cc():
    print ("*"* 20)
    print ("1.新建名片")
    print ("2.请输入姓名")
    print ("3.请输入公司")
    print ("4.请输入电话")
    print ("5.请输入邮箱")
    print ("6.请输入年龄")
    print ("7.请输入性别")
    print ("*"* 20)
cc()
def tuichu():
    print ("成功退出系统")
tuichu()
def xx():
    print("*"* 20)
    print("请您开始创建名片")
    name =input("请输入姓名:")
    company = input("请输入公司:")
    phone =int(input("请输入电话"))
    email = input("请输入邮箱:")
    age =int(input("请输入年龄"))
    sex = input("请输入性别:")
    dic = {"name":name,"com":company,"phone":phone,"email":email,"age":age,"sex":sex}
    list_card.append(dic)
    print(list_card)
    print ("名片保存成功，姓名是：%s" % dic['name'])
xx()




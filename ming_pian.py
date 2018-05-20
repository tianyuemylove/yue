def a():
    print("*"* 50)
    print ("1.新建名片")
    print ("2.查看名片")
    print ("3修改名片")
    print ("4.删除名片")
    print ("5.退出名片")
    print("*"* 50)
a()
name_list = []
def lll():
    b = input("请输入名字>>")
    c = int(input("请输入年龄>>"))
    d = int(input("请输入电话>>"))
    v = input("请输入性别>>")
    m = input ("请输入公司>>")
    dic = {"name":b,"age":c,"phone":d,"sex":v,"com":m}
    name_list.append(dic)
    print (name_list)
mm = input("请输入系统所规定的菜单:")
for 

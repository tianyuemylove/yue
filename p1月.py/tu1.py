
#tu1 =(1,2,3)
#for c in tu1:
 #   print(c)
#x =0
#while x <=2:
 #   print(tu1[x])
  #  x =x+1
tu1 = ((1,2,3),(4,5,6),(7,8,9))
'''for q in tu1:
   # print(q)
    for cc in q:
     print(cc)
s = 0
while s <= 2:
    print(tu1[s])
    s = s+1
    x = 0
    while x<=2:
        print(tu1[x])
        x =x+1'''
listt = []
dic1 = {'name':'冰淇淋','com':'百度','age':19}
dic2 = {'name':'苹果','com':'腾讯','age':19}
dic3 ={'name':'西瓜','com':'哈哈','age':19}
dic4 = {'name':'菠萝蜜','com':'nana','age':19}
listt.append(dic1)
listt.append(dic2)
listt.append(dic3)
listt.append(dic4)
print (listt)
bbb = 0
while bbb <=3:
    cc = input('请输入你要要查询的名字 >>')
    for i in listt:
        if cc == i['name']:
            print('*'* 30)
            print ('姓名:%s' % i['name'])
            print ('公司:%s' % i['com'])
            print ('年龄:%s' % i['age'])
    if cc =='q':
      	    break

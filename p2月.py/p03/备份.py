def cc_cp(name):

    i = open('name','w')
    i.write('I love you 哟呦呦 ！\n')
    i.close()
    f = open('name','rb+')
    p = name.rfind('.')
    n = name[:p]
    k = name[p:]
    f.close()
    t = open(n +'副本'+ k,'wb+')
    while True:
        c = f.read(1024)
        if len(c)== 0 :
            break
        t.write(c)


v = input('请输入您需要备份的文件名字')
cc_cp(v)


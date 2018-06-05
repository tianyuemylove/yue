l1 = open('i.txt','w')
l1.write('君自故乡来,\n')
l1.write('应知故乡事。\n')
l1.write('来日一窗前，\n')
l1.write('寒梅著花末。\n')
l1.close()
l1 = open('i.txt','r')
bb = l1.read(5)
seek(5,0)
print(bb)

cc = l1.readlines()
l1.tell()
print('游标的 位置是 ', l1.tell())
l1.close()
l2 = open('i.txt','a')
for x in cc:
    v = x[:len(x)-1]
    print(v + '$_$\n')
l2.close()


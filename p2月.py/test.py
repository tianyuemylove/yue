l = open('i.txt','w')
l.write('君自故乡来，\n')
l.write('应知故乡事。\n')
l.write('来日一窗前，\n')
l.write('寒梅著花末。\n')
l.close()
l1 = open('i.txt','r')
cc = l1.readlines()
l1.close()
l2 = open('i.txt','a')
for x in cc:
    v = x[:len(x)-1]
    l2.write(v + '*_*')
l2.close()

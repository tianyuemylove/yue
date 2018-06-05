# for i in range(1,10):
#    for c in range(1,i+1):
#        print('%d * %d =%d' % (i,c,i*c),end = '\t')
#    print('\n')



i = 0
c = 0
while i<9:
    i =i+1
    while c<9:
        c=c+1
        c =i+1
        print('%d * %d = %d' % (i,c,i*c),end = '\t')
    print('\n')



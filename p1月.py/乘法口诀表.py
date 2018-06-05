for i in range(9,0,-1):
    for c in range(9,i-1,-1):
        x =i*c
        print('%d *%d = %d' % (i,c,x), end='\t')
    print('\n')

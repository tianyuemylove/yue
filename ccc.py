list_test = ['lijia',19,'nv']
c =10
b =20
def cc():
    global c
    c = c + 1
    print (c)
    list_test[1] = 299
    list_test.append('cccccccccccccc')
    print (list_test)
    

def xx():
    global b
    b = b+1
    print(b)
cc()
xx() 

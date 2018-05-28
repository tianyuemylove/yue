cc = 0
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if (x!=y) and (y!=z) and (z!=x) :
                print(x,y,z) 
                cc =cc+1
print(cc) 
                

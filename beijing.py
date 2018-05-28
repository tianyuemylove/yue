listt =[{"北京":{"面积":"1000平","人口":"200w"},"上海":{"面积":"600平","人口":"150w"}}]   
for i in listt:
    for x,y in i.items():
        for a,b in y.items():
            print(x,a,b)
            
            
        

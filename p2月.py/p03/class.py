class tutu:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print('%s正在吃胡萝卜' % self.name)
    def drink(self):
        print('兔兔正在喝饮料')
    def run(self):
        print('兔兔在跑步')
    def jieshao(self):
        print('我的名字是%s  我的年龄是%d ' % (self.name,self.age))
aiai = tutu('王一凡','19','180','10')
aiai.eat()

#aiai.age = 700
#aiai.name = '爱爱'
#aiai.jieshao()

#huahua = tutu()
#huahua.age = 9000
#huahua.name = '花花'
#huahua.jieshao()

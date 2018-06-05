class tutu:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def all(self):
        print('我的名字是%s兔兔，我的年龄是%d,我的颜色是%s' % (self.name,self.age,self.color))
    def eat(self):
        print('%s兔兔正在吃胡萝卜' % self.name)
    def drink(self):
        print('%s兔兔正在喝可乐' % self.name)
    def run(self):
        print('%s兔兔正在跑步减肥' % self.name)
    def __str__(self):
        s = '大西瓜'+ self.name
        return s
aiai = tutu('王一凡',7,'红色')
print('爱爱的内存地址是:%d' % id(aiai))
print(aiai)
aiai.eat()
aiai.drink()
aiai.run()
aiai.all()

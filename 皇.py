class Huang:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
    def eat(self):
        print('%s兔兔正在吃胡萝卜'% self.name)
    def sing(self):
        print('%s兔兔正在唱歌' % self.name)
    def run(self):
        print('%s兔兔正在跑步减肥，加油！' % self.name)
        print('%s是智障' % self.name)
    def __str__(self):
        s ='名字:'+self.name +'\n'+'年龄:'+self.age+'身高:'+self.height
        return s
def tutu(item):
    item.eat()
    item.sing()
    item.run()

aiai = Huang('王一凡','3','0.3米')
print(aiai)
wanwan = Huang('爱爱','7','0.5米')
print(wanwan)
tutu(aiai)
tutu(wanwan)

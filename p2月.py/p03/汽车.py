class Car:
    def __init__(self,name,lunzi,color):
        self.lunzi = lunzi
        self.color = color
        self.name = name
    def run(self):
        print('%s激动的跳起来啦 %d个轮子正在飞快的转动起来 鲜艳的%s'% (self.name,self.lunzi,self.color))
    def jiao(self):
        print('%s开心的唱起来啦' % self.name)
    def wei(self):
        print('%s受伤了 追尾啦' % self.name)
    def __str__(self):
        s = '大西瓜'+self.name
        return s
baoma = Car('王一凡',8,'红色')
baoma.run()
baoma.jiao()
baoma.wei()
aodi = Car('奥迪',5,'红称黄绿青蓝紫')
print('车的名字是: %s' % baoma)
aodi.run()
aodi.jiao()
aodi.wei()


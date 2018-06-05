class Youxi:
    def __init__(self,name,xingwei,color):
        self.name = name
        self.xingwei = xingwei
        self.color = color
    def classs(self):
        print('类名: %s' % self.name)
    def xinwei(self):
        print('行为: %s' % self.xingwei)
kui = Youxi('向日葵','放阳光','黄色')
kui.classs()
kui.xinwei()
# *************************************************
class yx:
    def __init__(self,name,xingwei,shuxing):
        self.name = name
        self.xingwei = xingwei
        self.shuxing = shuxing
    def lei(self):
        print('类名: %s' % self.name)
    def xing(self):
        print('行为: %s' % self.xingwei)
    def shu(self):
        print('属性: %s' % self.shuxing)
    def __str__(self):
        s = '拉拉:'+self.name+'嘿嘿:'+self.xingwei+'哎呦:'+self.shuxing
        return s
wandou = yx('豌豆','发炮，摇头','颜色，发型，血量')
wandou.lei()
wandou.xing()
wandou.shu()
print(wandou)
#**************************************************
jianguo = yx('坚果','阻挡','血量，类型')
jianguo.lei()
jianguo.xing()
jianguo.shu()
#**************************************************
jiangshi = yx('僵尸','走，跑跳，吃，死','颜色，血量，类型，速度')
jiangshi.lei()
jiangshi.xing()
jiangshi.shu()

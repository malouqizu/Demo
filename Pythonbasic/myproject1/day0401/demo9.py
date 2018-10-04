class AA:
    def __init__(self,n):
        self.name = n

    def funa(self):
        print("名字：",self.name)

    def info(self):
        print("我是类AA")
        print("============================")

class BB(AA):
    def __init__(self,n,a):
        AA.__init__(self,n)
        self.age=a

    def funb(self):
        print("年龄：",self.age)

    def info(self):
        print("我是类BB，我继承自类AA")
        print("===========================")

class CC(BB):
    def __init__(self,n,a,ad):
        BB.__init__(self,n,a)
        self.address=ad

    def func(self):
        print("地址：",self.address)

    def info(self):
        print("我是类CC，我继承自类BB")
        print("=========================")

a=AA("张三")
a.funa()
a.info()

b=BB("李四",18)
b.funa()
b.funb()
b.info()

c=CC("王五",18,"北京")
c.funa()
c.funb()
c.func()
c.info()
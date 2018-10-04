class AA:
    def __init__(self,n):
        self.name = n

    def funa(self):
        print("名字：",self.name)

    def info(self):
        print("我是类AA")

class BB(AA):
    def __init__(self,n,a):
        AA.__init__(self,n)
        self.age=a

    def funb(self):
        print("年龄：",self.age)

    def info(self):
        print("我是类BB，我继承自类AA")

a=AA("张三")
a.funa()
a.info()

b=BB("张三",18)
b.funa()
b.funb()
b.info()


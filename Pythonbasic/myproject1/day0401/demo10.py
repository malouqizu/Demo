class A:
    def __init__(self,n):
        self.name=n

    def funa(self):
        print("姓名：",self.name)

    def info(self):
        print("我是类A")
        print("=======================")

class B:
    def __init__(self,a):
        self.age=a

    def funb(self):
        print("年龄：",self.age)

    def info(self):
        print("我是类B")
        print("=======================")

class C(A,B):
    def __init__(self,n,a,ad):
        A.__init__(self,n)
        B.__init__(self,a)
        self.address=ad

    def func(self):
        print("地址：",self.address)

    def info(self):
        print("我是类C")
        print("=======================")

a=A("张三")
a.funa()
a.info()

b=B("李四")
b.funb()
b.info()

c=C("王五",15,"北京")
c.funa()
c.funb()
c.func()
c.info()
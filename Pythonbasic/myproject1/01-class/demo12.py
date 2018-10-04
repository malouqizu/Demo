#定义一个父类AAA
class AAA:
    #定义父类构造函数
    def __init__(self,n):
        self.name=n

    def funa(self):
        print("类AAA中的函数")
        print("姓名:",self.name)

#定义一个父类BBB
class BBB:
    #定义父类构造函数
    def __init__(self,a):
        self.age=a

    def funb(self):
        print("类BBB中的函数")
        print("年龄:",self.age)

#定义一个子类CCC,同时继承AAA和BBB
class CCC(AAA,BBB):
    #定义子类的构造函数
    def __init__(self,n,a,w):
        #调用父类的构造函数
        AAA.__init__(self,n)
        BBB.__init__(self,a)
        #定义自己的变量
        self.work=w

    def func(self):
        print("子类CCC中的函数")
        print("工作:",self.work)

#实例化子类CCC
c=CCC("张敏",23,"教师")

#调用子类所有的函数
c.funa()
c.funb()
c.func()
#数据封装
class MyClass(object):
    def __init__(self,x,y,z):
        self.var1=x
        self._var2=y
        self.__var3=z

obj=MyClass(3,4,5)
print(obj.var1)
print(obj._var2)
obj.var1=10
obj._var2=15
print(obj.var1)
print(obj._var2)


class A():
    def __init__(self,p):
        self.__p=p

    def getP(self):
        return self.__p

    def setP(self,p):
        self.__p=p

a1=A(2)
print(a1.getP())
a1.setP(3)
print(a1.getP())

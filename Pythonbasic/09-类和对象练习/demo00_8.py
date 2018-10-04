#数据隐藏
class MyClass:
    __a=0
    def sum(self,increment):
        self.__a=self.__a+increment
        print(self.__a)

b=MyClass()
b.sum(2)
b.sum(5)

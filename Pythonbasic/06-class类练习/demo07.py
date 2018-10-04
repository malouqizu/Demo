#定义一个类B
class B:
    #定义构造函数,包含一个默认值参数
    def __init__(self,a,b=10):
        self.length=a
        self.width=b

    #定义一个普通的函数
    def show(self):
        print("执行计算相乘的结果:")
        self.res=self.length*self.width
        return self.res

#实例化类B
b1=B(20,15)
#调用show函数
#x=b1.show()
print("计算结果:",b1.show())

b2=B(10.56)
y=b2.show()
print("计算结果:%.2f"%y)
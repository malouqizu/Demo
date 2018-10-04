#定义类A
class A:
    #定义一个构造函数，只有self参数
    def __init__(self):
        print("这是构造函数！")

    #定义一个普通的函数
    def show(self):
        self.x=10
        self.y=20
        self.z=self.x+self.y
        return self.z

#实例化类A
p=A()
#调用show方法
res=p.show()
print("计算结果:",res)

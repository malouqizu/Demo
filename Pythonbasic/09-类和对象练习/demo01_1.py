#编写一个程序，定义一个类，类名为Rectangle，它有两个参数：
#length和breadth。这个类还有用来计算矩形周长的方法。
class Rectangle():
    def __init__(self,a,b):
        self.length=a
        self.breadth=b

    def fun(self):
        c=self.length*2+self.breadth*2
        print("矩形的周长：",c)

r=Rectangle(3,4)
r.fun()

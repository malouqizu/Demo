#定义一个Calc类
class Calc:
    #定义构造函数
    def __init__(self,x,y):
        print("这是一个构造函数：")
        self.length=x
        self.width=y

    #定义一个普通函数，计算长方形周长和面积
    def calca(self):
        print("这是一个计算函数：")
        self.area=self.length *self.width
        self.zhouchang=2*(self.length+self.width)
        print("计算结果：\n面积：",self.area,"周长：",self.zhouchang)

#对Calc类进行实例化，  同时提供构造函数参数
c1=Calc(20,10)
#调用calca函数
c1.calca()
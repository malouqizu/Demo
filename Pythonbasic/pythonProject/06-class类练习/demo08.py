#定义一个类Calculator
class Calculator:
    def calc(self,x,y):
        self.num1=x
        self.num2=y
        self.res=self.num1+self.num2
        print("计算结果:",self.res)

#对类进行实例化
c1=Calculator()
#调用类中的方法，两个整数相加
c1.calc(10,20)
#两个浮点型数据相加
c1.calc(20.45,45.67)
#两个字符串相加
c1.calc("你好，","Python!")
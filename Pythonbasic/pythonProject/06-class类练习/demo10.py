#定义一个父类AA
class AA:
    #定义一个函数input1,输入长方形的长和宽
    def input1(self):
        self.chang=input("请输入长：")
        self.kuan=input("请输入宽：")
        self.chang=float(self.chang)
        self.kuan=float(self.kuan)

    #定义一个函数jisuana,计算长方形的面积
    def jisuana(self):
        self.area=self.chang*self.kuan
        print("长方形面积:%.2f"%self.area)

#定义一个类BB,继承父类AA
class BB(AA):
    #定义函数input2，输入圆的半径
    def input2(self):
        self.banjing=input("请输入圆的半径:")
        self.banjing=float(self.banjing)

    #定义函数jisuanb，计算圆的面积
    def jisuanb(self):
        self.PI=3.14
        self.areab=self.PI*(self.banjing**2)
        print("圆的面积:%.2f"%self.areab)

#定义子类CC,继承父类BB
class CC(BB):
    def c(self):
        print("CC类继承了BB类,BB类继承了AA类！")

'''
#对父类AA进行实例化
a=AA()
#调用函数
a.input1()
a.jisuana()
#对子类BB进行实例化

b=BB()
#调用BB中定义的函数
b.input2()
b.jisuanb()
#调用从类AA中继承的函数
b.input1()
b.jisuana()
'''
#实例化类CC
x=CC()
#调用CC中定义的函数c
x.c()
#调用直接父类BB中的函数
x.input2()
x.jisuanb()

#调用间接父类AA的函数
x.input1()
x.jisuana()


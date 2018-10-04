#定义模块m2,对应的源文件m2.py
#定义计算类Calc
class Calc:
    #定义乘法函数mul
    def mul(self,x,y):
        z=x*y
        return z

    #定义除法函数div
    def div(self,x,y):
        if y!=0:
            z=x/y
            return z
        else:
            print("除数为零！")
            return 0

print("m2模块名称:",__name__)
#测试代码
if __name__=="__main__":
    t1=Calc()
    a=t1.mul(10,20)
    print("相乘结果:",a)

    b=t1.div(100.56,23.45)
    print("相除结果:",b)

    c=t1.div(10,0)
    print("相除结果:",c)
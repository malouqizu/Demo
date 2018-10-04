#导入模块m1中的加法函数add和减法函数sub
from m1 import add,sub
#导入模块m1中的变量PI和city
from m1 import PI,city
#导入模块m2中的Calc类
from m2 import Calc

num1=input("请输入第一个数:")
num2=input("请输入第二个数:")
num1=float(num1)
num2=float(num2)

#调用模块m1中的函数
add(num1,num2)
sub(num1,num2)
#调用模块m1中的变量
print("圆周率:",PI)
print("城市:",city)

#对类Calc进行实例化
c=Calc()
x=c.mul(num1,num2)
print("相乘结果:",x)
print("相除结果:",c.div(num1,num2))


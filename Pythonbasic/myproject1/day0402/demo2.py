from m1 import add,sub
from m1 import PI,city
from m2 import Calc

num1=input("请输入第一个数：")
num2=input("请输入第二个数：")
num1=float(num1)
num2=float(num2)
add(num1,num2)
sub(num1,num2)

c=Calc()
x=c.mul(num1,num2)
print("两数相乘结果：",x)
y=c.div(num1,num2)
print("两数相除结果：",y)

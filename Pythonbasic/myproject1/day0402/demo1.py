import m1
import m2

num1=input("请输入第一个数：")
num2=input("请输入第二个数：")
num1=float(num1)
num2=float(num2)

m1.add(num1,num2)
m1.sub(num1,num2)
print("圆周率：",m1.PI)
print("city：",m1.city)

calc=m2.Calc()
c=calc.mul(num1,num2)
d=calc.div(num1,num2)
print("两数相乘结果：",c)
print("两数相除结果：",d)

#导入m1和m2
import m1
import m2 as abc

num1=input("请输入第1个数:")
num2=input("请输入第2个数:")
num1=float(num1)
num2=float(num2)

#调用模块m1中的模块成员
m1.add(num1,num2)
m1.sub(num1,num2)

yuanzhoulv=m1.PI
print("圆周率:",yuanzhoulv)
print("城市:",m1.city)

#对模块m2中的类Calc实例化
c=abc.Calc()
x=c.mul(num1,num2)
print("相乘结果:",x)
print("相除结果:",c.div(num1,num2))



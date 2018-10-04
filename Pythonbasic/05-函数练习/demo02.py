#用户输入两个整数，使用函数实现两数的乘法

#1、定义函数
def mul(x,y):
    z=x*y
    return z

#2、使用函数
num1=input("请输入第1个整数：")
num1=int(num1)
num2=input("请输入第2个整数：")
num2=int(num2)
res=mul(num1,num2)
print("两数乘积：",res)

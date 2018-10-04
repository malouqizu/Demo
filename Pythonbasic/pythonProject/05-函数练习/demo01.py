#函数练习
#函数定义

#1、无参数、无返回值
def hello():
    print("hello，python！")
    print("你好，软件测试")

#2、无参数，有返回值
def str_add():
    a="abc"
    b="def"
    c=a+b
    return c

#3、有参数、无返回值
def my_add(x,y):
    z=x+y
    print(z)

#4、有参数、有返回值
def calc1(a,b,c):
    m=a*b*c
    return m

'''
#函数调用
#1、调用hello函数
hello()
print("hello函数调用完毕！")

#2、调用str_add函数
x=str_add()  # x="abcdef"
print("计算结果：",x)

print("计算结果：",str_add())

#3、调用my_add函数
a=100
b=200
print("第一次调用：")
my_add(a,b)
print("第二次调用：")
my_add(12.34,45.67)

hello()
'''

#调用calc1函数
x=100
y=200
z=300
res=calc1(x,y,z)    #res=m
print("三个数相乘结果：",res)

res=calc1(12.34,45.67,34.56)
print("三个数相乘结果：",res)


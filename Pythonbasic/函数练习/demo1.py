#函数练习
#函数定义

#1、无参数，无返回值
def hello():
    print("hello,python!")
    print("你好，软件测试！")
    
#2、无参数，有返回值
def str_add():
    a="abc"
    b="def"
    return a+b

#3、有参数，无返回值
def my_add(x,y):
    z=x+y
    print(z)

#4、有参数，有返回值
def calc1(a,b,c):
    m=a*b*c
    return m

'''
#函数调用
#1、调用hello函数
hello()
print("hello函数调用结束！\n")

#2、调用str_add函数
str1=str_add()
print("str_add函数调用结束！")
print(str1)
print("计算结果：",str_add())
print('\n')


#3、调用my_add函数
sum1=my_add(1,2)
print("my_add函数调用结束！")
print(sum1)
print('\n')

#4、调用cacl1函数
cal=calc1(1,2,3)
print("calc1函数调用结束！")
print(cal)
print('\n')
'''

a=100
b=200
print("第一次调用：")
my_add(a,b)
print("第二次调用：")
my_add(12.34,78.90)

hello()





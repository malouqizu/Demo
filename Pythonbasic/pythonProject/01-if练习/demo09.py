#单语句实现if-else功能
#输入两个整数，比较大小，输出较大的数

a=input("请输入第1个整数：")
b=input("请输入第2个整数：")
a=int(a)
b=int(b)

#如果a>b成立，取得if前面表达式a的值，然后赋值给x
#否则，取得else后面表达式b的值，然后赋值给x
x=(a if a>b else b)

print("较大的数是%d"%x)

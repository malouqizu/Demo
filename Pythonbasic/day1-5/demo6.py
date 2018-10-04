#单语句实现if-else功能
#输入两个数，比较大小，输出较大的数
a=input("请输入第一个整数：")
a=int(a)
b=input("请输入第二个整数：")
b=int(b)
#如果a>b成立，取的if前面表达式a的值，然后赋值给x
#否则，取的else后面表达式b的值，然后赋值给x
x=a if a>b else b
print("较大的数是：%d"%x)

#输入两个整数，使用if-else实现判断大小，把较大值输出

x=input("输入第一个整数：")
y=input("输入第二个整数：")
x=int(x)
y=int(y)

if x>y:
    maxi=x
else:
    maxi=y

print("较大数是：%d"%maxi)

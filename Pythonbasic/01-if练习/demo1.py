#输入两个整数，输出较大值

x=input("请输入第1个整数：")
y=input("请输入第2个整数：")
x=int(x)
y=int(y)

maxi=x
if maxi<y:
    maxi=y
print("较大的数是：%d"%maxi)

#给定一个整数，编写程序生成一个字典，这个字典包括（i,i*i），其中i是一个1到n之间（包含1和n）的整数。这个程序会打印出整个字典
n=input("请输入一个整数：")
n=int(n)
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)


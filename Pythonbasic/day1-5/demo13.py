#break的练习
#输入四个整数求和，但和一旦超过100，就停止输入

i=1
sum1=0
while i<15:
    print("请输入第%d个数"%i)
    num1=input()
    num1=int(num1)
    i=i+1
    sum1=sum1+num1
    if sum1>100:
        break
print("和为：%d" %sum1)

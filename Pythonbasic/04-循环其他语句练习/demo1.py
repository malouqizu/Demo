#break练习
#输入四个整数求和，如果超过100，就停止输入

#循环变量赋初值
i=1
#存放求和结果
sum1=0

while i<=4:   #循环条件
    print("请输入第%d个数："%i)
    num1=input()
    num1=int(num1)
    #循环变量增值
    i+=1
    #计算累加和
    sum1=sum1+num1
    if sum1>100:
        break

print("和为：%d"%sum1)

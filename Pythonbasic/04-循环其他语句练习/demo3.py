#continue和while
#输入三个数据，如果输入的正数，进行相加，如果输入的是负数，不进行相加

i=1
sum1=0
while i<=3:
    print("请输入第%d个数："%i)
    num1=input()
    num1=int(num1)
    i=i+1
    if num1<0:
        continue
    sum1=sum1+num1

print("和为：%d"%sum1)

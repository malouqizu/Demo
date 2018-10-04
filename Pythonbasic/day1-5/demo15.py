#continue与while循环
#输入三个数据，如果输入的是正数进行累加
#如果输入的是一个负数不进行相加

i=0
sum1=0
while i<3:
    i=i+1;
    print("第%d个数据:" %i)
    num=input()
    num=int(num)
    if num<0:
        continue
    sum1=sum1+num

print("所有正整数之和为%d"%sum1)

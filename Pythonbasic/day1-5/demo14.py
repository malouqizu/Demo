#break与for循环
#使用range产生1~9的数据
#对这些数据进行累加求和
#这些数据一旦超过30就结束整个循环

sum1=0
for i in range(1,10,1):
    sum1=sum1+i
    print(i,sum1)
    if sum1>30:
        break
print(sum1)

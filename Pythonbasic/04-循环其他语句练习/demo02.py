#break与for循环
#使用range产生1-9的数据
#对这些数据进行累加求和
#一旦累加和超过30，就终止循环

#存放累加和
sum1=0
for i in range(1,10,1):
    # 求元素1-9的累加和
    sum1+=i
    print(i,sum1)
    if sum1>30:
        break

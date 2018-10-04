#continue与for循环
#计算1~10之间的偶数和

sum1=0
for i in range(1,11,1):
    if i%2==0:
        sum1=sum1+i
    else:
        continue
    print(i,sum1)
    
print(sum1)

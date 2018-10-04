#使用for循环实现1~5的平方
#定义一个列表，存放1~5

num=[1,2,3,4,5]

for i in num:   #使用变量i遍历列表num
    square=num[i-1] * num[i-1]  #依次计算1~5平方
    print(i,"的平方是：",square)

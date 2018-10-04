#while...else和列表实现1~9的平方
'''
list1=[1,2,3,4,5,6,7,8,9]
total=len(list1)
i=0
print("计算1~9的平方：")
while i<total:
    square=list1[i]*list1[i]
    print(i+1,"的平方是：",square)
    i=i+1
else:
    print("循环正常结束：")
'''
list1=[1,2,3,4,5,6,7,8,9]
total=len(list1)
i=0
print("计算1~9的平方：")
while i<total:
    square=list1[i]*list1[i]
    print(i+1,"的平方是：",square)
    i=i+1
    if square>50:
        break
else:
    print("循环正常结束：")

print("while循环结束，开始执行下面的语句！")

#使用while-else和列表实现1~9的平方

list1=[1,2,3,4,5,6,7,8,9]
total=len(list1)
i=0
print("计算1-9的平方：")
while i<total:
    square=list1[i] * list1[i]
    print(i+1,"的平方是：",square)
    i+=1
else:
    print("循环正常结束！")


'''
#while-else有break练习
i=0
while i<5:
    print("第%d次循环"%i)
    if i==3:
        break
    i+=1
else:
    print("循环正常结束！")
print("开始执行循环后语句...")
'''

#for-else练习
for i in range(1,5,1):
    print(i)
    if i==4:
        break
else:
    print("循环正常结束！")

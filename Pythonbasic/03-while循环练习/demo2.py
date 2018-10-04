#求1~9的平方

#使用列表存储1`9
list1=[1,2,3,4,5,6,7,8,9]

#测试列表的长度（元素的个数）
total=len(list1)

#循环变量初值
i=0
print("计算1-9的平方：")

#循环条件：i小于列表长度就循环
while i<total:
    # 依次计算1-9平方，存在square
    square=list1[i] * list1[i]
    # 输出显示
    print("%d   *   %d  =   %d"%(list1[i],list1[i],square))
    # 循环变量增值
    i+=1
    
    

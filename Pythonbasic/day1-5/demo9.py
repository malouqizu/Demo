#求1~9的平方

list1=[1,2,3,4,5,6,7,8,9]
total=len(list1)
i=0
print("计算1~9的平方")
while i<total:
    square=list1[i]*list1[i]
    print("%d * %d = %d" %(list1[i],list1[i],square))
    i=i+1

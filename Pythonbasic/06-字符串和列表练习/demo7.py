#编写Python程序，演示各种列表函数和列表操作
lst1=['java','cloud',1995,2010]
lst2=[3,6,9,12,15]
lst3=["p ","q ","r ","s "]
print("Various list operations:")
print(lst1[0])
print("list split operations:")
print(lst2[1:5])
print(lst2[1:18])
print(lst2[:3])
print(lst2[1:])
print(lst2[::-1])
print(lst2[3:1])
lst1=['java','cloud',1995,2010]
lst2=[3,6,9,12,15]
print("Modify elements of the list:")
lst1[2]=2001
print(lst1)
print("Delete element from list:")
del lst1[2]
print(lst1)
print(len(lst1))
print(max(lst2))
print(min(lst2))
print(sum(lst2))
print(sum(lst2)/len(lst2))
print(lst2.count(3))
lst3=["p","q","r","s"]
print(len(lst3))
print(max(lst3))
print(min(lst3))
print(lst3.count("p"))
tup=(1,2,3)
print(list(tup))
lst1.extend(lst2)
print(lst1)
print(lst1.index('java'))
lst3.insert(4,"w")
print(lst3)
lst1=['java','cloud',1995,2010]
print(lst1.pop())
print(lst1)
lst1.remove('cloud')
print(lst1)
lst1.reverse()
print(lst1)
lst2=[3,6,9,12,15,1]
lst2.sort()
print(lst2)



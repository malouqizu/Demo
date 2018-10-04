#考虑元组（12,7,38,56,78）,编写一个程序，打印出另一个元组，该元组的值是给定元组中的偶数
tup1=(12,7,38,56,78)
list1=list()
for i in tup1:
    print(i)
    if i%2 == 0:
        list1.append(i)

print(list1)
tup1=tuple(list1)
print(tup1)
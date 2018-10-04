#编写一个程序，检查一个字符串是否是回文。

str1=input("请出入一个字符串：")
list1=[]
for item in str1:
    list1.append(item)

list1.reverse()
str2="".join(list1)
print(str2)

if str1==str2:
    print("出入的字符串",str1,"是回文！")
else:
    print("出入的字符串",str1,"不是回文！")





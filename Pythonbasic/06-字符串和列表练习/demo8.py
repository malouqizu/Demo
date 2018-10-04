#验证课后习题做的是否准确
string="computer"
print(string[6])

string="keyboard"
print(string[6:4])

str1="hello world!"
str2="Welcome to Programming"
print(str1[4])
print(str1*5)
print(str2*3)
print(str1[6:])
print(str2[14:])
print(str1[5:10])
print(str2 + "Python")

print("%o is the octal equivalent of %d" %(6,6))
print("the fourth letter of %s is %c" %('programming','i'))
print("The sum = %d" %(-5))
print("%X is the hexadecimal equivalent of %d" %(14,14))
print("%x is the hexadecimal equivalent of %d" %(13,13))

str="This is my first python program. My first python program is simple."
print(str.replace('first','second'))
print(str.replace('first','second',2))

s="I am learning Python and it is simple to learn."
print("Maximum character is:",max(s))
print("Minimum character is:",min(s))

str="This is my first python program. My first python program is simple."
print(str.count('o',0,28))
print(str.count('o',0,60))

str="Welcome to Programming in python"
print(str.find('gramm',0,31))
print(str.find('thing'))
print(str.startswith('in',8,25))
print(str.startswith('in',23,31))
print(str.endswith('in',8,25))
print(str.endswith('in',0,31))

lst1=[1,4,23,56,90]
lst1.insert(4,32)
print(lst1)

list1=['hey',234,1.32,'book',100]
print("item at position 3=",list1[3])
list1[3]=432
print("item at position 3=",list1[3])
print("item at position 1 and 2 is ",list1[1],list1[2])
list1[1]='hi'
list1[2]=340
print("item at position 1 and 2 is ",list1[1],list1[2])

ls=['hey',234,1.32,'book',100]
print(ls)
del ls[4]
print(ls)
print(ls*3)
print(ls+ls)
ls.append(387)
print(ls)

tup=('hey',234,1.32,'book',100)
print(tup)
print(list(tup))

ls=['hey',234,1.32,'book',100,234,234]
print(ls.count(234))
ls.remove('hey')
print(ls)

print(ls.index(100))
#print(ls.index('john'))

print(ls)
ls.reverse()
print(ls)
'''
list2=input("Enter a list (space separated):")
list2=list(map(int,list2.split()))
print("Maximum element in a list: ",max(list2))
'''
list1=['大象','狮子','老虎','狐狸']
print(list1[0])
print(list1[-1])

list2=[1,3,2,5,9,20,15]
print(min(list2))

values=input("input some comma separated numbers:")
list3=values.split(",")
print(list3)

list4=['hey',234,1.32,'hook',100]
print(list4)
list4.pop(-1)
print(list4)

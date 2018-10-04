'''
for x in range(5):
    print(x)

print('\n')
'''
'''
for y in range(10,20,2):
    print(y)

print('\n')
'''
'''
for z in range(10,20):
    print(z)
'''
'''
list1=["河南","北京","深圳","上海"]
for x,y in enumerate(list1):
    print("%d %s" %(x,y))

for a,b in enumerate("abcdefg"):
    print("%d %c" %(a,b))

t1=("hello","how")
for a,b in enumerate(t1):
    print(a,b)

for m,n in enumerate("软件工程师"):
    print(m,n)
'''
'''
for a in sorted("abndceh"):
    print(a)
    
for b in sorted("软件工程师"):
    print(b)

num=[2,4,1,7,89,50]
for c in sorted(num):
    print(c)
'''
'''
for x in reversed('abcfedg'):
    print(x)
'''
list1=[1,2,3]
list2=['a','b','c']
list3=['河南','北京','上海']
for a,b,c in zip(list1,list2,list3):
    print(a,b,c)







    









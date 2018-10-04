#编写一个Python程序，演示字典的功能和操作
'''
dicti={'Lang':'Python','Chap':6,"Topic":'program'}
print(dicti)
print(dicti['Lang'])
print(dicti['Chap'])
print(dicti['Topic'])
for m,n in dicti.items():
    print(m,n)

print("")
for m in dicti:
    print(m,dicti[m])

print("")
for key in dicti.keys():
    print(key,dicti[key])

print("")
for value in dicti.values():
    print(value)

dicti['Chap']=8
print(dicti)
dicti['Topic']='Dicionary topic'
print(dicti)

del dicti['Lang']
print(dicti)

dicti.clear()
print(dicti)

del dicti

dicti1={'Lang':'Python','Chap':11}
dicti2={'Lang':'c','Chap':15}
dicti3={'Lang':'java','Chap':35}
dicti4={'Lang':'perl','Chap':25}
print(dicti1['Chap'])
print(dicti2['Lang'])

tup4=('john',100,345,1.67,'book')
print(tup4[2:4])
print(tup4[3:])

tup5=(1,5,8,9)
print(tup5[1:-1])

tup1=(3,5,7,9)
tup2=(3,5,9,7)
if tup1 < tup2:
    print("tup1 < tup2")

print(tup1<tup2)
print(tup1>tup2)
print(tup1==tup2)
print(tup1<=tup2)
print(tup1>=tup2)
print(tup1!=tup2)

str1='hello python'
print(tuple(str1))
'''

tup3=(4,6,8,10)
#tup3.append((12,14,20,24))
print(tup3*2)

tup5=('computer',456,'book')
print(list(tup5))



#编写一个程序，说明元组中的函数和元组操作
tpl1=(1,2,3,5,7,11)
tpl2=('aaa','pqr','uvw','zzz')
tpl3=tpl1+tpl2
print(tpl2.count(1))
print(tpl3.count(3))
print(tpl3.count(30))
lst=tuple(tpl3)
print(lst)
del tpl3

#模块demo12,对应的源文件demo12.py
#文件路径:day0402->mypackage->package1-package12
#导入包中模块module11a和module11b
import day0402.mypackage.package1.package11.module11a
import day0402.mypackage.package1.package11.module11b

#一行可以导入多个模块
#import day0402.mypackage.package1.package11.module11a,day0402.mypackage.package1.package11.module11b
#导入时给模块起个别名
import day0402.mypackage.package1.package11.module11a as mya
import day0402.mypackage.package1.package11.module11b as myb


#访问module11a中的模块成员
day0402.mypackage.package1.package11.module11a.m11afun1()
x=day0402.mypackage.package1.package11.module11a.PI
print(x)
p1=day0402.mypackage.package1.package11.module11a.M11a()
p1.m11afun2()
#访问module11b中的模块成员
a=day0402.mypackage.package1.package11.module11b.m11bfun1("Python")
print(a)
print(day0402.mypackage.package1.package11.module11b.city)
p2=day0402.mypackage.package1.package11.module11b.M11b()
b=p2.m11bfun2("Java!")
print(b)

'''
#使用模块别名进行访问
#访问module11a中的模块成员
mya.m11afun1()
x=mya.PI
print(x)
p1=mya.M11a()
p1.m11afun2()
#访问module11b中的模块成员
a=myb.m11bfun1("Python")
print(a)
print(myb.city)
p2=myb.M11b()
b=p2.m11bfun2("Java!")
print(b)
'''

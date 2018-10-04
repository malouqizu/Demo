#模块demo21,对应的文件demo21.py
#文件路径:day0402->mypackage->package2->package21
#导入模块module11a中的模块成员
#from day0402.mypackage.package1.package11.module11a import m11afun1
#from day0402.mypackage.package1.package11.module11a import PI
#from day0402.mypackage.package1.package11.module11a import M11a

#导入模块module11b中的模块成员
#from day0402.mypackage.package1.package11.module11b import m11bfun1
#from day0402.mypackage.package1.package11.module11b import city
#from day0402.mypackage.package1.package11.module11b import M11b

#在一行导入多个模块成员
#from day0402.mypackage.package1.package11.module11a import m11afun1,PI,M11a
#from day0402.mypackage.package1.package11.module11b import m11bfun1,city,M11b

#导入模块所有成员，可以使用星号*
#from day0402.mypackage.package1.package11.module11a import *
#from day0402.mypackage.package1.package11.module11b import *

#使用from import方式导入模块
from day0402.mypackage.package1.package11 import module11a
from day0402.mypackage.package1.package11 import module11b

#访问模块module11a中的成员
module11a.m11afun1()
print(module11a.PI)
my2=module11a.M11a()
my2.m11afun2()

#访问模块module11b中的成员
a=module11b.m11bfun1("中国!")
print(a)
print(module11b.city)
b=module11b.M11b()
c=b.m11bfun2("China!")
print(c)


'''
#访问module11a中的模块成员
m11afun1()
print(PI)
my1=M11a()
my1.m11afun2()
#访问module11b中的模块成员
x=m11bfun1("软件测试！")
print(x)
print(city)
my2=M11b()
y=my2.m11bfun2("测试！")
print(y)
'''


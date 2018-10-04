#模块demo12，对应文件demo12.py
#文件路径：day0402->mypackage->package1->package12
#导入包中模块module11a和module11b
'''
import day0402.mypackage.package1.package11.module11a
import day0402.mypackage.package1.package11.module11b

#访问模块module11a中的成员
day0402.mypackage.package1.package11.module11a.m11afun1()

pi=day0402.mypackage.package1.package11.module11a.PI
print("圆周率：",pi)

m=day0402.mypackage.package1.package11.module11a.M11a()
m.m11afun2()

#访问模块module11b中的成员
day0402.mypackage.package1.package11.module11b.m11bfunc1()

city=day0402.mypackage.package1.package11.module11b.city
print("city:",city)

n=day0402.mypackage.package1.package11.module11b.M11b()
n.m11bfunc2()

'''

import day0402.mypackage.package1.package11.module11a as mya
import day0402.mypackage.package1.package11.module11b as myb

mya.m11afun1()
pi=mya.PI
print("圆周率：",pi)
m=mya.M11a()
m.m11afun2()

myb.m11bfunc1()
city=myb.city
print("city:",city)
n=myb.M11b()
n.m11bfunc2()
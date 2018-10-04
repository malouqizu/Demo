#模块demo2，对应的文件为demo22.py
#文件路径：day0402->mypackage->package1->package12
#导入包中模块module11a和module11b

from day0402.mypackage.package1.package11 import module11a
from day0402.mypackage.package1.package11 import module11b

module11a.m11afun1()
pi=module11a.PI
print("圆周率：",pi)
m=module11a.M11a()
m.m11afun2()

module11b.m11bfunc1()
city=module11b.city
print("city:",city)
n=module11b.M11b()
n.m11bfunc2()
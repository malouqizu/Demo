#模块demo21，对应的文件为demo21.py
#文件路径：day0402->mypackage->package1->package12
#导入模块module11a和module11b中的成员
from day0402.mypackage.package1.package11.module11a import m11afun1
from day0402.mypackage.package1.package11.module11a import PI
from day0402.mypackage.package1.package11.module11a import M11a

from day0402.mypackage.package1.package11.module11b import m11bfunc1
from day0402.mypackage.package1.package11.module11b import city
from day0402.mypackage.package1.package11.module11b import M11b

m11afun1()
print("圆周率：",PI)
m=M11a()
m.m11afun2()

m11bfunc1()
print("city:",city)
n=M11b()
n.m11bfunc2()
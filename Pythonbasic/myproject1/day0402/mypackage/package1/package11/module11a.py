#模块module11a，对应文件module11a.py
#文件路径：day0402->mypackage->package1->package11
#定义函数
def m11afun1():
    print("我是module11a中的函数")

#定义变量
PI=3.14156

#定义类
class M11a:
    def m11afun2(self):
        print("我是module11a中类M11a中的函数")

#测试代码
if __name__ == "__main__":
    m11fun1()
    print("PI=",PI)
    m=M11a()
    m.m11fun2()
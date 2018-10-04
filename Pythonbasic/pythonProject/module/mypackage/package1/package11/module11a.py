#模块module11a,对应文件module11a.py
#文件路径：module->mypackage->package1->package11
#定义函数
def m11afun1():
    print("这是module11a中的函数")

#定义变量
PI=3.1415

#定义一个类
class M11a:
    def m11afun2(self):
        print("这是module11a中类M11a中的函数")

#测试代码
if __name__=="__main__":
    m11afun1()
    c=M11a()
    c.m11afun2()
    print("变量:",PI)
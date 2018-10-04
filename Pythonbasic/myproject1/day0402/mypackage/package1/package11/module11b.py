#模块module11b，对应的文件module11b.py
#文件路径：day0402->mypackage->package1->package11
#定义函数
def m11bfunc1():
    print("我是模块module11b中的函数")

#定义变量
city=["北京","天津","上海","重庆","深圳"]

#定义类
class M11b:
    def m11bfunc2(self):
        print("我是模块module11b中的函数")

print("我是模块：",__name__)
#测试代码
if __name__ == "__main__":
    m11bfunc1()
    print("city:",city)
    m=M11b()
    m.m11bfunc2()
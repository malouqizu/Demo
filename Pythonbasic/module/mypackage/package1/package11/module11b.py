#模块module11b，对应文件module11b.py
#文件路径:module->mypackage->package1->package11
#定义函数
def m11bfun1(str1):
    str1="你好,"+str1
    print("这是module11b中的函数")
    return str1

#定义元组
city=("北京","上海","天津")

#定义类
class M11b:
    def m11bfun2(self,str2):
        self.str2="hello,"+str2
        print("这是module11b中类M11b中的函数")
        return self.str2

#测试代码
if __name__=="__main__":
    x=m11bfun1("Python")
    print(x)
    print(city)

    y=M11b()
    a=y.m11bfun2("java")
    print(a)

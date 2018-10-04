class AA():
    def __init__(self,n,a,*p):
        print("我是类AA的构造函数")
        self.name=n
        self.age=a
        self.other=p
        m=len(self.other)
        t1=tuple()
        if m==0:
            print("其他信息：无")
        else:
            for i in self.other:
                print(i)

    def pri(self):
        print("姓名：",self.name)
        print("年龄：",self.age)

    def info(self):
        print("我是类AA")

a=AA("张三",20,"北京","女","18611122639")
a.pri()
a.info()

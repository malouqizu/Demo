class AA():
    def __init__(self,n,a=19):
        print("我是类AA的构造函数")
        self.name=n
        self.age=a

    def pri(self):
        print("姓名：",self.name)
        print("年龄：",self.age)

    def info(self):
        print("我是类AA")

a=AA("李四")
a.pri()
a.info()
#定义一个父类Person
class Person:
    #定义父类的构造函数
    def __init__(self,n,a):
        self.name=n
        self.age=a
    #定义普通函数show1
    def show1(self):
        print("姓名:",self.name)
        print("年龄:",self.age)

    def info(self):
        print("父类的方法")
        print("我是父类Person")
        print("=============================")

#定义子类StudentA,继承父类Person
class StudentA(Person):
    #定义子类的构造函数
    def __init__(self,n,a,num,g):
        #调用父类的构造函数
        Person.__init__(self, n, a)
        #定义学号和年级
        self.stu_num=num
        self.grade=g

    #定义普通的函数，显示学号和年级
    def show2(self):
        print("学号：",self.stu_num)
        print("年级:",self.grade)

    #覆盖父类中的info函数
    def info(self):
        print("子类StudentA中的函数")
        print("我是子类StudentA")
        print("==============================")

#定义子类WorkerA，继承父类Person
class WorkerA(Person):
    #定义子类的构造函数
    def __init__(self,n,a,num,lev):
        #调用父类的构造函数
        Person.__init__(self,n,a)
        self.wk_id=num
        self.level=lev

    #定义普通函数show3
    def show3(self):
        print("工号：",self.wk_id)
        print("级别:",self.level)

    #覆盖父类的函数info
    def info(self):
        print("子类WorkerA中的函数")
        print("我是子类WorkerA")
        print("=========================")

#实例化父类Person,并调用其中的函数
zhangsan=Person("张三",45)
zhangsan.show1()
zhangsan.info()

#实例化子类StudnetA,并调用所有的函数
lisi=StudentA("李四",20,"A0010","三年级")
#调用父类继承的函数show1
lisi.show1()
#调用自己定义的函数
lisi.show2()
#调用覆盖父类的函数info
lisi.info()

#实例化子类WorkerA,并调用所有的函数
wangwu=WorkerA("王五",47,"AA1111","高级技师")
#调用父类的函数
wangwu.show1()
#调用自己的函数
wangwu.show3()
#调用覆盖父类的函数info
wangwu.info()
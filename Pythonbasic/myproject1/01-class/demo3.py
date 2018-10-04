#定义一个Person类，包含函数和成员变量/数据成员
class Person2:
    def lecture(self,xingming):
       self.name=xingming
       print("我叫",self.name,"我在演讲！")
    def study(self,nianling):
        self.age=nianling
        print("我今年",self.age,"岁，我在学习！")
    def drive(self,zhiye):
        self.profession=zhiye
        print("我是一名",self.profession,"我在开车！")
    def work(self,zhicheng):
        self.level=zhicheng
        print("我是",self.level,"职称，我在工作！")

#实例化Person2
#调用类中的函数
Jack=Person2()
Jack.lecture("杰克")
Jack.study(20)
Jack.drive("警察")
Jack.work("中级")
#访问类中的变量
print(Jack.name,Jack.age,Jack.profession,Jack.level)

Person2()

#定义一个Person类
class Person2:
    def lecture(self,n):
        self.name=n
        print("我是",self.name,"我在演讲！")
    def study(self,a):
        self.age=a
        print("我",self.age,"岁，我在学习！")
    def drive(self,zhiye):
        self.profession=zhiye
        print("我是一名",self.profession,"我在开车！")
    def work(self,zhicheng):
        self.level=zhicheng
        print("我的技术等级是",self.level,"我在工作！")

#实例化Person2
jack=Person2()
jack.lecture("杰克")
jack.study(15)
jack.drive("侦探")
jack.work("高级")
print(jack.name,jack.age,jack.profession,jack.level)
jack.name="Tom"
jack.age=89
jack.profession="警察"
jack.level="初级"
print(jack.name,jack.age,jack.profession,jack.level)


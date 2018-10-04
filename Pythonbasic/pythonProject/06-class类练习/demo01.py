#定义一个Person1类
class Person1:
    def lecture(self):
        print("我在演讲！")
    def study(self):
        print("我在学习！")
    def drive(self):
        print("我在开车！")
    def work(self):
        print("我在工作！")

#对Person1类进行实例化
Tom=Person1()
#访问类中的函数
Tom.lecture()
Tom.study()
Tom.work()
Tom.drive()
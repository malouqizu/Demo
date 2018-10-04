#定义一个学生类Student
class Student:
    def pri(self):
        print("这是一个学生类！")

    def stuinfo(self,n,a):
        self.name=n
        self.age=a
        print("我叫",self.name,"我今年",self.age,"岁")

#实例化Student类
xiaoming=Student()
#调用Student类中的方法
xiaoming.pri()
xiaoming.stuinfo("小明",12)
print("姓名：",xiaoming.name)
print("年龄：",xiaoming.age)

xiaohong=Student()
xiaohong.pri()
xiaohong.stuinfo("小红",13)
print("姓名：",xiaohong.name,"年龄：",xiaohong.age)

#定义一个Student类
class Student:
    def pri(self):
        print("这是Student类！")

    def stuinfo(self,n,a):
        self.name=n
        self.age=a
        print("姓名：",self.name,"年龄：",self.age)


#实例化Student
xiaoming=Student()
xiaoming.pri()
xiaoming.stuinfo("小明",12)
print(xiaoming.name,xiaoming.age)

xiaohong=Student()
xiaohong.pri()
xiaohong.stuinfo("小红",13)
print(xiaohong.name,xiaohong.age)











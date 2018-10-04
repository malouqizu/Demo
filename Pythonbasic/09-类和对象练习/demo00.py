#定义类结构：定义一个student类
class Student():
    def fill_details(self,name,branch,year):
        self.name=name
        self.branch=branch
        self.year=year

    def pri_detials(self):
        print(self.name)
        print(self.branch)
        print(self.year)

#创建一个对象，并使用对象的方法
s1=Student()
s1.fill_details('lily','english',2000)
s1.pri_detials()

#演示对象使可以改变的特征
s1.fill_details('jack','ECE',2010)
s1.pri_detials()
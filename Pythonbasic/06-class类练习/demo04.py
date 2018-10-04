#定义一个Worker类
class Worker:
    def setname(self,n):
        self.name=n
    def setage(self,a):
        self.age=a
    def setsalary(self,s):
        self.salary=s

    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def getsalary(self):
        return self.salary

    def printinfo(self):
        print("姓名：",self.name)
        print("年龄：",self.age)
        print("薪资:",self.salary)

#对类进行实例化
zhangming=Worker()
#访问类中的函数
zhangming.setname("张明")
zhangming.setage(45)
zhangming.setsalary(8567.89)
zhangming.printinfo()
name=zhangming.getname()
print(name)
age=zhangming.getage()
print(age)
salary=zhangming.getsalary()
print(salary)

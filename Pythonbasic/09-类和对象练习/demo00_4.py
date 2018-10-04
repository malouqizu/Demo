#继承
#定义父类Person
class Person(object):
    def get_name(self,name):
        self.name=name

    def get_details(self):
        return self.name

#定义子类Student
class Student(Person):
    def fill_details(self,name,branch,year):
        Person.get_name(self,name)
        self.branch=branch
        self.year=year

    def get_detials(self):
        print(self.name)
        print(self.branch)
        print(self.year)

#定义子类Teacher
class Teacher(Person):
    def fill_detials(self,name,branch):
        Person.get_name(self,name)
        self.branch=branch

    def get_details(self):
        print(self.name)
        print(self.branch)

person1=Person()
student1=Student()
techer1=Teacher()

person1.get_name('John')
print(person1.get_details())

student1.fill_details('Jinnie','CSE',2005)
student1.get_detials()

techer1.fill_detials('Jack','ECE')
techer1.get_details()

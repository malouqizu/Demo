class Student:
    def __init__(self,name,age,grade="һ�꼶"):
        self.name=name
        self.age=age
        self.grade=grade

    def display(self):
        print("����:",self.name)
        print("����:",self.age)
        print("�꼶:",self.grade)

if __name__=="__main__":
    xiaoming=Student("С��",12,"���꼶")
    xiaoming.display()
    xiaogang=Student("С��",13,"���꼶")
    xiaogang.display()

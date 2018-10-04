#内置的类属性
class Student():
    '''
    这是一个Student类！
    '''
    def fill_details(self,name,branch,year):
        self.name=name
        self.branch=branch
        self.year=year

    def pri_detials(self):
        print(self.name)
        print(self.branch)
        print(self.year)

print(Student.__doc__)
print(Student.__name__)
print(Student.__module__)
print(Student.__bases__)
print(Student.__dict__)
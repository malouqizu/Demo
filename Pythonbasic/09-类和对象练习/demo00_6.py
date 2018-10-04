#方法重写
class Parent():
    def ovr_method(self):
        print("This is in Parent Class!")

class Child(Parent):
    def ovr_method(self):
        print("This is in Child Class!")

p=Parent()
p.ovr_method()
c=Child()
c.ovr_method()

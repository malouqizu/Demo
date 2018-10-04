#定义一个类Animal，该类中有一个方法legs。之后创建两个子类：Tiger和Dog。
#接下来，使用类Dog显式调用方法leg，并使用类Tiger隐式调用方法leg
class Animal():
    def legs(self):
        print("legs Animal() method!")

class Dog(Animal):
    def legs(self):
        print("legs Dog() method!")

class Tiger(Animal):
    pass

a=Animal()
a.legs()
d=Dog()
d.legs()
t=Tiger()
t.legs()
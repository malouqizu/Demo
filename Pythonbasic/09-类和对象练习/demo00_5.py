#多重继承
class A():
    def x(self):
        print("Method of A")

class B():
    def x(self):
        print("Method of B")

class C(B,A):
    pass

a=A()
b=B()
c=C()
a.x()
b.x()
c.x()


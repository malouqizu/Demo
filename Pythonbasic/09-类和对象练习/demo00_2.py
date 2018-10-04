#对象作为返回值
class Triangle():
    def create_triangle(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print("The triangle is created!")

    def pri_sides(self):
        print("side a:",self.a)
        print("side b:",self.b)
        print("side c:",self.c)

t1=Triangle()
t1.create_triangle(10,20,25)
t1.pri_sides()

def size_double(obj):
    t2=Triangle()
    t2.a=obj.a*2
    t2.b=obj.b*2
    t2.c=obj.c*2
    return t2

t3=size_double(t1)
t3.pri_sides()

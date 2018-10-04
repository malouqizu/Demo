#对象作为参数
class Triangle():
    a=10
    b=18
    c=23
    print("我是一个可以改变的对象!")

t1=Triangle()

def perimeter(obj):
    per=t1.a+t1.b+t1.c
    print("Permieter of triangle: ",per)

perimeter(t1)
class Calc():
    def mul(self,x,y):
        z=x*y
        return z

    def div(self,x,y):
        if y!=0:
            z=x/y
            return z
        else:
            print("除数为零")
            return 0

print("我是模块：",__name__)
if __name__ == "__main__":
    c=Calc()
    a=c.mul(10,20)
    print("两数相乘：",a)
    b=c.div(10,20)
    print("两数相除：",b)


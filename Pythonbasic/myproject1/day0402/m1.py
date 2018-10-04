def add(x,y):
    z=x+y
    print("两数相加等于：",z)

def sub(x,y):
    z=x-y
    print("两数相减等于：",z)

PI=3.14156
city=["北京","上海","天津","重庆"]

print("我是模块：",__name__)
if __name__ == "__main__":
    add(10,20)
    sub(10,20)
    print("圆周率：",PI)
    print("city:",city)
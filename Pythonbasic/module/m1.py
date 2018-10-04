#定义模块m1，对应的源文件m1.py
#定义加法函数add
def add(x,y):
    z=x+y
    print("相加结果：",z)

#定义减法函数sub
def sub(x,y):
    z=x-y
    print("相减结果：",z)

#定义变量PI
PI=3.1415
#定义列表变量city
city=["北京","上海","天津","重庆"]

print("m1模块名称：",__name__)
#测试代码
if __name__ =="__main__":
    add(100,200)
    sub(300,200)
    print("圆周率:",PI)
    print("city:",city)
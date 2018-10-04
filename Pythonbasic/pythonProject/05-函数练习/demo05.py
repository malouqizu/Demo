#关键字参数练习
#函数定义
def fun1(x,y,z):
    n=x*y*z
    print("x=%d"%x)
    print("y=%d"%y)
    print("z=%d"%z)
    print("三数乘积：%d"%n)

#函数调用——普通方式
fun1(10,20,30)

#函数调用——关键字参数方式
fun1(z=50,x=30,y=10)

#位置顺序和关键字参数混合使用
fun1(20,z=50,y=40)

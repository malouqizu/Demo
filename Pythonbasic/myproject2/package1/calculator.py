class calcu():
    def add(self,x,y):
        self.x=x
        self.y=y
        self.res1=x+y
        return self.res1

    def sub(self,x,y):
        self.x=x
        self.y=y
        self.res2=x-y
        return self.res2

    def mul(self,x,y):
        self.x=x
        self.y=y
        self.res3=x*y
        return self.res3

    def div(self,x,y):
        self.x=x
        self.y=y
        self.res4=x/y
        return self.res4

if __name__=="__main__":
    c1=calcu()

    print("==========================")
    print("add函数功能测试开始：")
    add_r1=c1.add(10,2)
    if add_r1==30:
        print("add函数整数测试结果正确！")
    else:
        print("add函数整数测试结果错误！")

    add_r2=c1.add(10.11,12.2)
    if add_r2==22.33:
        print("add函数浮点数测试结果正确！")
    else:
        print("add函数浮点数测试结果错误！")

    add_r3=c1.add("你好","Python！")
    if add_r3=="你好Python！":
        print("add函数字符串测试结果正确！")
    else:
        print("add函数字符串测试结果错误！")

    print("add函数功能测试结束！")
    print("==========================")

    print("==========================")
    print("sub函数功能测试开始：")
    sub_r1=c1.sub(10,2)
    if sub_r1==5:
        print("sub函数整数测试结果正确！")
    else:
        print("sub函数整数测试结果错误！")

    sub_r2=c1.sub(10.11,5.1)
    if abs(sub_r2-5)<=0.000001:
        print("sub函数浮点数测试结果正确！")
    else:
        print("sub函数浮点数测试结果错误！")

    print("sub函数功能测试结束！")
    print("==========================")

    print("==========================")
    print("mul函数功能测试开始：")
    mul_r1=c1.mul(10,2)
    if mul_r1==200:
        print("mul函数整数测试结果正确！")
    else:
        print("mul函数整数测试结果错误！")

    mul_r2=c1.mul(11.11,22.2)
    if mul_r2==246.8642:
        print("mul函数浮点数测试结果正确！")
    else:
        print("mul函数浮点数测试结果错误！")

    print("mul函数功能测试结束！")
    print("==========================")

    print("==========================")
    print("div函数功能测试开始：")
    div_r1=c1.div(10,4)
    if div_r1==2:
        print("div函数整数测试结果正确！")
    else:
        print("div函数整数测试结果错误！")

    div_r2=c1.div(10.22,2.01)
    if div_r2==5.11:
        print("div函数浮点数测试结果正确！")
    else:
        print("div函数浮点数测试结果错误！")

    print("div函数功能测试结束！")
    print("==========================")



















#选择语句的嵌套使用
"""
判断输入三条边的数值是否可以构建一个三角形
"""
a=input("请输入第一条边数值：")
a=int(a)
b=input("请输入第二条边数值：")
b=int(b)
c=input("请输入第三条边数值：")
c=int(c)

if a>0 and b>0 and c>0 and a+b>c and a+c>b and c+b>a:
    print("可以组成一个三角形！")
    if a!=b and a!=c and b!=c:
        print("普通三角形！")
    elif (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
        print("等腰三角形！")
    else:
        print("等边三角形！")
else:
    print("不能组成一个三角形！")

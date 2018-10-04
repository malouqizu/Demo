#使用函数，计算圆的面积和长方形面积
#1、定义函数，计算圆的面积
def yuan(r):
    area1=r*r*3.14
    return area1

#2、定义函数，计算长方形面积
def changfangxing(x,y):
    area2=x*y
    return area2
'''
#3、测试函数
a=yuan(10)
print("圆的面积：",a)

b=changfangxing(10,20)
print("长方形面积：",b)
'''
#4、给出提示，让用户选择是计算圆的面积还是计算长方形的面积
#如果计算圆的面积，让用户输入圆的半径
#如果计算长方形的面积，让用户输入长和宽
#（1）给出用户提示菜单
print("计算面积：")
print("a.计算圆的面积")
print("b.计算长方形的面积")

con='y' #定义一个变量，初值为‘y’
while con=='y' or con=='Y':     #判断con是否为‘y’或‘Y’，如果是，进入循环体

    #（2）获得用户的输入
    answer=input("请选择：")
    #（3）对用户输入的选择进行判断，使用if-elif-else
    if answer=='a' or answer=='A':
        print("计算圆的面积")
        m=input("请输入圆的半径：")
        m=float(m)  #把半径转换为浮点数据
        n=yuan(m)   #调用计算圆面积的函数yuan
        print("半径为%.2f圆形面积是：%.2f"%(m,n))

    elif answer=='b' or answer=='B':
        print("计算长方形面积")
        i=input("请输入长方形的长：")
        k=input("请输入长方形的宽：")
        i=float(i)
        k=float(k)
        p=changfangxing(i,k)    #调用计算长方形面积的函数changfangxing
        print("长为%.2f,宽为%.2f的长方形面积为：%.2f"%(i,k,p))
        
    else:
        print("选择错误！")

    con=input("是否继续？(Y/N)")     #提示用户是否继续？如果选择y，则继续循环
else:
    print("程序正常结束！")
    















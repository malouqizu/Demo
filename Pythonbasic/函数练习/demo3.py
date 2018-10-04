#函数定义
#使用函数计算圆的面积和长方形面积

#1、定义函数，计算圆的面积
def yuan(r):
    area1=r*r*3.14
    return area1

#2、定义函数，计算长方形的面积
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
#4、给出提示，让用户选择是计算圆的面积还是计算
#长方形面积，如果计算圆的面积，让用户输入圆的
#的半径，如果用户选择的是计算长方形的面积，让
#用户输入长和宽

#（1）给出用户提示菜单
print("计算面积：")
print("a.计算圆的面积")
print("b.计算长方形的面积")

con='y'#定义一个变量，初值为'Y'
while con=='y' or con=='Y': #判断con是否为'Y',如果是将进入循环体
    
    #（2）获得用户的输入
    answer=input("请选择：")

    #（3）对用户的选择进行判断，使用if-elif-else
    if answer=='a' or answer=='A':
        print("计算圆的面积")
        r=input("请输入圆的半径：")
        r=float(r)
        are=yuan(r)
        print("半径为%.2f圆的面积：%.2f"%(r,are))
        
    elif answer=='b' or answer=='B':
        print("计算长方形的面积")
        x=input("请输入长方形的长：")
        x=float(x)
        y=input("请出入长方形的宽：")
        y=float(y)
        are=changfangxing(x,y)
        print("长为%.2f宽为%.2f的长方形面积：%.2f" %(x,y,are))
        
    else:
        print("选择错误！")

    #提示用户是否继续？如果选择y，则继续循环
    con=input("是否继续？（Y/N）")
    
else:
    print("程序正常结束！")




























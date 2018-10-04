#使用if-else判断输入的整数的正数还是负数
num1=input("请输入一个整数：")
num1=int(num1)
if num1>0:
    print("输入的是一个正整数：%d"%num1)
else:
    print("输入的是一个负整数：%d"%num1)

#求输入整数的绝对值

num=input("请输入第1个整数：")
num=int(num)

if num<0:
    num=-num

print("绝对值是%d"%num)

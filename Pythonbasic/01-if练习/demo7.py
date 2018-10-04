#if-else练习

str1=input("请输入一个字符串")
num=input("请输入一个正整数：")
x=len(str1) #计算str1字符串长度
num=int(num)

#如果输入的整数num>0 并且 num大于等于用户输入字符串长度
if num>0 and num>=x:
    #使用用户输入的字符串乘以用户输入的整数
    str2=str1 * num   
    print(str2)
else:
    print("输入的字符串为：%s"%str1)
    print("输入的字符串长度为：%d"%x)
    print("输入的整数是%d"%num)

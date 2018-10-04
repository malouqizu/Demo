#enumerate练习
'''
for i,item in enumerate("abcdefg"):
    print("第%d个字符是：%s"%(i+1,item))
    
for i,item in enumerate('软件测试工程师'):
    print("第%d个字符是：%s"%(i+1,item))
'''

#sorted练习
'''
num=[2,4,6,1,10,50,40,30]
for i in sorted(num):
    print(i)
    
'''
'''
#reversed练习
for x in reversed("abcdefg"):
    print(x)
'''

#zip练习
num1=[1,2,3]
num2=['a','b','c']
num3=["张三","李四","王五"]

for x,y,z in zip(num1,num2,num3):
    print("%d,%s,%s"%(x,y,z))

#使用字典存储水果名称和价格，通过for循环进行遍历
#定义水果字典

fruit={"苹果":10,"草莓":15,"西瓜":12}

#通过字典的items()函数，返回每个元素的键和值
#使用变量name和price分别进行存储
for name,price in fruit.items():
    print("水果名称：%s，价格：%s"%(name,price))

#使用字典的keys()函数，返回每个元素的键
for n in fruit.keys():
    print("水果名称：%s"%n)

#使用字典的values()函数，返回每个元素的值
for p in fruit.values():
    print("水果价格：%s"%p)

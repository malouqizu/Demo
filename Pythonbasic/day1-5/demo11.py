fruit={'苹果':10,'草莓':15,'西瓜':12}
for name,price in fruit.items():
    print("%s的价格是%d元！" %(name,price))
    
for name in fruit.keys():
    print(name)

for price in fruit.values():
    print(price)

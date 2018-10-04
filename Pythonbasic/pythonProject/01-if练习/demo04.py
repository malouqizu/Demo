#同一性运算符和成员资格运算符练习

x=y=[1,2,3]
n=1
m=10

if x is y:
    print("x就是y")

if n in x:
    print("n包含在x中")

if m not in y:
    print("m不包含在y中")

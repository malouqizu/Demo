#同一性运算符和成员资格运算符练习

x=y=[1,2,3]
z=[1,2,3]
n=1
m=10

if x is y:
    print("x就是y")

if x is not z:
    print("x不是z")

if n in z:
    print("n包含在z中")

if m not in z:
    print("m不包含在z中")

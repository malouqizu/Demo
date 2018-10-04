#定义一个函数，该函数打印一个元组，元组中的值是1到15之间（包含1和15）的数字的立方
def tup3():
    list1=list()
    for i in range(1,16):
        list1.append(i*i*i)
    print(list1)
    tup1=tuple(list1)
    print(tup1)

tup3()

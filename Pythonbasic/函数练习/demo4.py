#函数进阶
#默认值参数练习1

'''
def hellob(name="python"):
    print("你好，%s" %name)

#调用函数，提供默认值参数
hellob("java")

#调用函数，不给出参数，使用默认参数
hellob()
'''
#默认值参数练习2
#定义带多个默认值参数的函数，
#默认值参数必须放在参数列表最后
def student(name,age,address="北京",nation="汉族"):
    print("姓名：%s，年龄：%d，住址：%s，民族：%s" %(name,age,address,nation))

#调用函数，给出全部参数
student("李明",20,"上海","回族")

#调用函数，只给出前两个参数（使用默认值）
student("李四",30)

#调用函数，给出三个参数
student("小米",17,"天津")












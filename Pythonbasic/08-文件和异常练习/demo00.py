#课中知识点练习
file_name='E:/Python/demo/python/readme.txt'

open(file_name,'x')

file_obj = open(file_name, 'r', encoding='UTF-8')
context = file_obj.read()
print(context)
file_obj.close()

with open(file_name, 'r', encoding='UTF-8') as file_obj1:
    context1 = file_obj1.read()
    # file_obj1.write("hello python test file!")
    print(context1)

with open(file_name, 'rb') as file_obj2:
    context2 = file_obj2.read()
    # file_obj2.write("this is python file for open test!")
    print(context2)

with open(file_name, 'r+', encoding='UTF-8') as file_obj3:
    file_obj3.writelines('hello python test file!\n')
    context31 = file_obj3.read()
    print(context31)

with open(file_name, 'w', encoding='UTF-8') as file_obj3:
    file_obj3.writelines('hello python test file!\n')

with open(file_name, 'w+', encoding='UTF-8') as file_obj3:
    file_obj3.writelines('hello python test file!!!!\n')

with open(file_name, 'a', encoding='UTF-8') as file_obj3:
    file_obj3.writelines('hello python test file!!!!\n')
    file_obj3.seek(0)

with open(file_name, 'a+', encoding='UTF-8') as file_obj3:
    file_obj3.writelines('hello python test file!!!!\n')
    file_obj3.seek(0)
    context1 = file_obj3.read()
    print(context1)



file_name='E:/Python/demo/python/readme.txt'
with open(file_name,'a+') as file_obj:
    file_obj.write("hello python!\n")
    file_obj.flush()
    print(file_obj.write('limengmeng\n'))
    print(file_obj.writelines('hllo hello1'))
    file_obj.seek(0)
    print(file_obj.readlines())





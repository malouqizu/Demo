file_name='E:/Python/demo/python/readme.txt'

file_obj=open(file_name,'a+')
file_obj.write("hello limengmeng!\n")
print(file_obj.tell())
file_obj.seek(file_obj.tell())
print(file_obj.tell())


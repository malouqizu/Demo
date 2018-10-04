#异常知识点学习
file_name='E:/Python/demo/python/readme.txt'

try:
    file=open(file_name,'x')
    file.write('hello python！')
except FileExistsError:
    print("文件已经存在，不能进行修改！")
else:
    print("Content written successfully!")

try:
    file=open(file_name,'x')
    file.write('hello python！')
except FileExistsError:
    print("文件已经存在，不能进行修改！")
except IOError:
    print("Can't find file for writing data!")
else:
    print("Content written successfully!")

try:
    file=open(file_name,'x')
    file.write('hello python！')
except:
    print("文件已经存在，不能进行修改！")
    print("Can't find file for writing data!")
else:
    print("Content written successfully!")

try:
    file = open(file_name, 'x')
    file.write('hello python！')
finally:
    print("无论如何该语句都会得到执行！")

